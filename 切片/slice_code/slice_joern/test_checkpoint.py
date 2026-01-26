#!/usr/bin/env python3
"""
快速测试脚本 - 验证断点续传和分chunk保存功能
"""
import os
import json
import sys

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config

def test_checkpoint_files():
    """测试断点文件是否存在和可读"""
    print("Testing checkpoint functionality...")
    
    files_to_check = [
        (config.CHECKPOINT_FILE, "Checkpoint file"),
        (config.PROGRESS_FILE, "Progress file"),
    ]
    
    for file_path, name in files_to_check:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                print(f"✓ {name} exists and is valid")
                print(f"  Content: {json.dumps(data, indent=2)[:200]}...")
            except Exception as e:
                print(f"✗ {name} exists but is corrupted: {e}")
        else:
            print(f"- {name} does not exist (OK for first run)")
    
    print()

def test_chunk_files():
    """测试chunk文件"""
    print("Testing chunk files...")
    
    if not os.path.exists(config.OUTPUT_DIR):
        print(f"- Output directory does not exist: {config.OUTPUT_DIR}")
        return
    
    chunk_files = sorted([f for f in os.listdir(config.OUTPUT_DIR) 
                         if f.startswith('slices_chunk_') and f.endswith('.json')
                         and '_summary' not in f])
    
    if not chunk_files:
        print("- No chunk files found (OK for first run)")
        return
    
    print(f"Found {len(chunk_files)} chunk files:")
    total_items = 0
    
    for chunk_file in chunk_files[:5]:  # 只显示前5个
        chunk_path = os.path.join(config.OUTPUT_DIR, chunk_file)
        try:
            with open(chunk_path, 'r') as f:
                data = json.load(f)
            size_mb = os.path.getsize(chunk_path) / 1024 / 1024
            total_items += len(data)
            print(f"  ✓ {chunk_file}: {len(data)} items, {size_mb:.2f} MB")
        except Exception as e:
            print(f"  ✗ {chunk_file}: Error - {e}")
    
    if len(chunk_files) > 5:
        print(f"  ... and {len(chunk_files) - 5} more files")
    
    print(f"\nTotal items in chunks: {total_items}")
    print()

def test_config():
    """测试配置"""
    print("Configuration:")
    print(f"  CHUNK_SIZE: {config.CHUNK_SIZE}")
    print(f"  ENABLE_CHECKPOINT: {config.ENABLE_CHECKPOINT}")
    print(f"  ENABLE_AST_FIX: {config.ENABLE_AST_FIX}")
    print(f"  ENABLE_MULTIPROCESSING: {config.ENABLE_MULTIPROCESSING}")
    print(f"  NUM_PROCESSES: {config.NUM_PROCESSES}")
    print(f"  OUTPUT_DIR: {config.OUTPUT_DIR}")
    print(f"  DATA_JSON: {config.DATA_JSON}")
    
    # 检查数据文件
    if os.path.exists(config.DATA_JSON):
        with open(config.DATA_JSON, 'r') as f:
            tasks = json.load(f)
        print(f"  Tasks to process: {len(tasks)}")
        
        # 预估时间
        if config.ENABLE_MULTIPROCESSING:
            estimated_hours = len(tasks) * 7.5 / 3600 / config.NUM_PROCESSES
            print(f"  Estimated time ({config.NUM_PROCESSES} processes): {estimated_hours:.1f} hours")
        else:
            estimated_hours = len(tasks) * 7.5 / 3600
            print(f"  Estimated time (single process): {estimated_hours:.1f} hours")
    else:
        print(f"  ✗ DATA_JSON not found: {config.DATA_JSON}")
    
    print()

def main():
    print("=" * 60)
    print("Single File Slicer - Quick Test")
    print("=" * 60)
    print()
    
    test_config()
    test_checkpoint_files()
    test_chunk_files()
    
    print("=" * 60)
    print("Test complete!")
    print("=" * 60)

if __name__ == '__main__':
    main()
