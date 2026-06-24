#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
警告标注工具 - Flask Web服务
"""

from flask import Flask, render_template, jsonify, request, send_file
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# 配置文件路径
DATA_FILE = 'inconsistent_labels.json'
ANNOTATIONS_FILE = 'annotations.json'

def load_warnings():
    """加载警告数据"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def load_annotations():
    """加载标注数据"""
    if os.path.exists(ANNOTATIONS_FILE):
        with open(ANNOTATIONS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_annotations(annotations):
    """保存标注数据"""
    with open(ANNOTATIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(annotations, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """主页"""
    return render_template('index.html')

@app.route('/api/warnings')
def get_warnings():
    """获取所有警告数据"""
    try:
        warnings = load_warnings()
        annotations = load_annotations()
        
        # 合并标注数据到警告中
        for warning in warnings:
            warning_id = str(warning['id'])
            if warning_id in annotations:
                warning['manual_annotation'] = annotations[warning_id]
        
        return jsonify({
            'success': True,
            'data': warnings,
            'total': len(warnings)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/annotations', methods=['GET'])
def get_annotations():
    """获取所有标注"""
    try:
        annotations = load_annotations()
        return jsonify({
            'success': True,
            'data': annotations
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/annotate', methods=['POST'])
def annotate():
    """添加或更新标注"""
    try:
        data = request.get_json()
        warning_id = str(data.get('id'))
        label = data.get('label')
        
        if not warning_id or not label:
            return jsonify({
                'success': False,
                'error': '缺少必要参数'
            }), 400
        
        # 加载现有标注
        annotations = load_annotations()
        
        # 更新标注
        annotations[warning_id] = {
            'label': label,
            'timestamp': datetime.now().isoformat()
        }
        
        # 保存
        save_annotations(annotations)
        
        return jsonify({
            'success': True,
            'message': '标注成功'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/export')
def export_data():
    """导出标注数据"""
    try:
        warnings = load_warnings()
        annotations = load_annotations()
        
        # 合并数据
        export_data = []
        for warning in warnings:
            warning_copy = warning.copy()
            warning_id = str(warning['id'])
            if warning_id in annotations:
                warning_copy['manual_annotation'] = annotations[warning_id]['label']
                warning_copy['annotation_timestamp'] = annotations[warning_id]['timestamp']
            else:
                warning_copy['manual_annotation'] = None
                warning_copy['annotation_timestamp'] = None
            export_data.append(warning_copy)
        
        # 生成文件名
        filename = f'annotated_warnings_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        filepath = os.path.join('/tmp', filename)
        
        # 保存到临时文件
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)
        
        return send_file(
            filepath,
            mimetype='application/json',
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/stats')
def get_stats():
    """获取统计信息"""
    try:
        warnings = load_warnings()
        annotations = load_annotations()
        
        # 统计不同标签的数量
        stats = {
            'total': len(warnings),
            'annotated': len(annotations),
            'unannotated': len(warnings) - len(annotations),
            'labels': {
                'TP': 0,
                'FP': 0,
                'Unknown': 0
            }
        }
        
        for ann in annotations.values():
            label = ann.get('label')
            if label in stats['labels']:
                stats['labels'][label] += 1
        
        return jsonify({
            'success': True,
            'data': stats
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/delete_annotation/<int:warning_id>', methods=['DELETE'])
def delete_annotation(warning_id):
    """删除标注"""
    try:
        annotations = load_annotations()
        warning_id_str = str(warning_id)
        
        if warning_id_str in annotations:
            del annotations[warning_id_str]
            save_annotations(annotations)
            return jsonify({
                'success': True,
                'message': '标注已删除'
            })
        else:
            return jsonify({
                'success': False,
                'error': '标注不存在'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/file')
def get_file_content():
    """获取文件内容"""
    file_path = request.args.get('path')
    if not file_path:
        return jsonify({'success': False, 'error': '缺少文件路径'}), 400
    
    # 安全检查：确保文件在项目目录或允许的目录内
    # 这里简化为只检查文件是否存在
    if not os.path.exists(file_path):
        return jsonify({'success': False, 'error': '文件未找到'}), 404
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return jsonify({'success': True, 'content': content})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 警告标注工具服务启动中...")
    print("=" * 60)
    print(f"📂 数据文件: {DATA_FILE}")
    print(f"💾 标注文件: {ANNOTATIONS_FILE}")
    print(f"🌐 访问地址: http://localhost:5000")
    print("=" * 60)
    print("按 Ctrl+C 停止服务")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
