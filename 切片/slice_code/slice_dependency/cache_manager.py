#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增量索引支持 - 避免重复构建索引
"""

import json
import pickle
from pathlib import Path
import time
import hashlib

class IndexCache:
    """索引缓存管理器"""
    
    def __init__(self, cache_dir: str = '.cache'):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.index_file = self.cache_dir / 'function_index.pkl'
        self.meta_file = self.cache_dir / 'index_meta.json'
    
    def get_project_signature(self, project_path: Path) -> str:
        """计算项目签名（基于修改时间）"""
        try:
            # 获取最新修改时间
            c_files = []
            for ext in ['.c', '.h', '.cpp', '.cc', '.cxx']:
                c_files.extend(list(project_path.rglob(f'*{ext}')))
            
            if not c_files:
                return ""
            
            # 使用最新修改时间和文件数量作为签名
            latest_mtime = max(f.stat().st_mtime for f in c_files[:100])  # 采样前100个文件
            file_count = len(c_files)
            signature = f"{latest_mtime}_{file_count}"
            return hashlib.md5(signature.encode()).hexdigest()
        except:
            return ""
    
    def load_index(self, repository_dir: Path):
        """加载缓存的索引"""
        if not self.index_file.exists() or not self.meta_file.exists():
            return None, {}
        
        try:
            # 加载元数据
            with open(self.meta_file, 'r') as f:
                meta = json.load(f)
            
            # 检查项目签名
            print("检查索引缓存...")
            projects = list(repository_dir.iterdir())
            signatures_changed = False
            
            for project_dir in projects:
                if not project_dir.is_dir():
                    continue
                
                current_sig = self.get_project_signature(project_dir)
                cached_sig = meta.get('signatures', {}).get(project_dir.name, '')
                
                if current_sig != cached_sig:
                    signatures_changed = True
                    break
            
            if signatures_changed:
                print("  项目已更新，需要重新构建索引")
                return None, {}
            
            # 加载索引
            print("  加载缓存的索引...")
            with open(self.index_file, 'rb') as f:
                indexer = pickle.load(f)
            
            print(f"  ✓ 成功加载索引 (创建于 {meta.get('created_at', 'unknown')})")
            return indexer, meta
            
        except Exception as e:
            print(f"  加载索引失败: {e}")
            return None, {}
    
    def save_index(self, indexer, repository_dir: Path):
        """保存索引到缓存"""
        try:
            print("\n保存索引到缓存...")
            
            # 计算所有项目签名
            projects = list(repository_dir.iterdir())
            signatures = {}
            for project_dir in projects:
                if project_dir.is_dir():
                    signatures[project_dir.name] = self.get_project_signature(project_dir)
            
            # 保存元数据
            meta = {
                'created_at': time.strftime('%Y-%m-%d %H:%M:%S'),
                'signatures': signatures,
                'project_count': len(signatures)
            }
            
            with open(self.meta_file, 'w') as f:
                json.dump(meta, f, indent=2)
            
            # 保存索引
            with open(self.index_file, 'wb') as f:
                pickle.dump(indexer, f, protocol=pickle.HIGHEST_PROTOCOL)
            
            print(f"  ✓ 索引已保存 (大小: {self.index_file.stat().st_size / 1024 / 1024:.2f} MB)")
            
        except Exception as e:
            print(f"  保存索引失败: {e}")
