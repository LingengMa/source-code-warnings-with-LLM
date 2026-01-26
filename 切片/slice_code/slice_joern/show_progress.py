#!/usr/bin/env python3
"""
快速查看切片进度
用法: python show_progress.py
"""
import os
import json
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config


def format_time(iso_string):
    """格式化时间字符串"""
    try:
        dt = datetime.fromisoformat(iso_string)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return iso_string


def show_progress():
    """显示进度"""
    if not os.path.exists(config.PROGRESS_FILE):
        print("No progress file found.")
        print("Run the slicer first: python single_file_slicer.py")
        return
    
    try:
        with open(config.PROGRESS_FILE, 'r') as f:
            progress = json.load(f)
        
        total = progress.get('total_tasks', 0)
        processed = progress.get('processed', 0)
        success = progress.get('success', 0)
        failed = progress.get('failed', 0)
        percentage = progress.get('progress_percentage', 0)
        
        print("\n" + "=" * 60)
        print("切片进度")
        print("=" * 60)
        print(f"总任务数:     {total:,}")
        print(f"已处理:       {processed:,} / {total:,}")
        print(f"进度:         {percentage:.2f}%")
        print("-" * 60)
        print(f"成功:         {success:,}")
        print(f"失败:         {failed:,}")
        
        if success + failed > 0:
            success_rate = success / (success + failed) * 100
            print(f"成功率:       {success_rate:.2f}%")
        
        print("-" * 60)
        print(f"最后更新:     {format_time(progress.get('timestamp', 'N/A'))}")
        
        # 估算剩余时间 (如果有足够的数据)
        if processed > 100:
            # 简单估算: 假设处理速度恒定
            remaining = total - processed
            print(f"剩余任务:     {remaining:,}")
        
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"Error loading progress: {e}")


def show_chunks():
    """显示chunk信息"""
    if not os.path.exists(config.OUTPUT_DIR):
        print("No output directory found.")
        return
    
    chunk_files = sorted([f for f in os.listdir(config.OUTPUT_DIR) 
                         if f.startswith('slices_chunk_') and f.endswith('.json')
                         and '_summary' not in f])
    
    if not chunk_files:
        print("No chunk files found yet.")
        return
    
    print("\n" + "=" * 60)
    print(f"Chunk 文件 (共 {len(chunk_files)} 个)")
    print("=" * 60)
    
    total_items = 0
    total_size = 0
    
    for i, chunk_file in enumerate(chunk_files):
        chunk_path = os.path.join(config.OUTPUT_DIR, chunk_file)
        try:
            with open(chunk_path, 'r') as f:
                data = json.load(f)
            
            size_mb = os.path.getsize(chunk_path) / 1024 / 1024
            total_items += len(data)
            total_size += size_mb
            
            # 只显示前5个和后5个
            if i < 5 or i >= len(chunk_files) - 5:
                print(f"{chunk_file}: {len(data):4d} items, {size_mb:6.2f} MB")
            elif i == 5:
                print(f"... ({len(chunk_files) - 10} more files) ...")
                
        except Exception as e:
            print(f"{chunk_file}: Error - {e}")
    
    print("-" * 60)
    print(f"总计: {total_items:,} items, {total_size:.2f} MB")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    show_progress()
    show_chunks()
