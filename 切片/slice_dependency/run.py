#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速运行脚本 - 带进度监控和性能统计
"""

import sys
import time
from pathlib import Path

# 添加到路径
sys.path.insert(0, str(Path(__file__).parent))

from slice_analyzer import SliceAnalyzer

def format_time(seconds):
    """格式化时间"""
    if seconds < 60:
        return f"{seconds:.2f}秒"
    elif seconds < 3600:
        return f"{seconds/60:.2f}分钟"
    else:
        return f"{seconds/3600:.2f}小时"

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║      高性能代码切片和依赖分析工具                            ║
║      采用"先全量索引/建图，再批量查询"模式                    ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    # 配置
    base_dir = Path(__file__).parent
    input_dir = base_dir / 'input'
    output_dir = base_dir / 'output'
    
    # 检查输入
    if not input_dir.exists():
        print(f"❌ 错误: 输入目录不存在: {input_dir}")
        return
    
    data_file = input_dir / 'data.json'
    if not data_file.exists():
        print(f"❌ 错误: 数据文件不存在: {data_file}")
        return
    
    repo_dir = input_dir / 'repository'
    if not repo_dir.exists():
        print(f"❌ 错误: 代码仓库目录不存在: {repo_dir}")
        return
    
    print(f"📁 输入目录: {input_dir}")
    print(f"📊 数据文件: {data_file.name} ({data_file.stat().st_size / 1024 / 1024:.2f} MB)")
    print(f"📦 代码仓库: {repo_dir.name} ({len(list(repo_dir.iterdir()))} 个项目)")
    print(f"💾 输出目录: {output_dir}")
    print()
    
    # 询问是否继续
    print("⚠️  注意: 索引构建可能需要较长时间（取决于项目规模）")
    response = input("是否继续? [Y/n]: ").strip().lower()
    if response and response not in ['y', 'yes', '是']:
        print("已取消")
        return
    
    print()
    
    # 创建分析器
    analyzer = SliceAnalyzer(str(input_dir), str(output_dir))
    
    # 执行分析
    total_start = time.time()
    
    try:
        # 阶段1: 构建索引
        stage1_start = time.time()
        analyzer.build_index()
        stage1_time = time.time() - stage1_start
        print(f"\n⏱️  阶段1耗时: {format_time(stage1_time)}")
        
        # 阶段2: 批量处理
        stage2_start = time.time()
        analyzer.process_entries(batch_size=1000)
        stage2_time = time.time() - stage2_start
        print(f"\n⏱️  阶段2耗时: {format_time(stage2_time)}")
        
        # 阶段3: 合并结果
        stage3_start = time.time()
        analyzer.merge_results()
        stage3_time = time.time() - stage3_start
        print(f"\n⏱️  阶段3耗时: {format_time(stage3_time)}")
        
        # 总结
        total_time = time.time() - total_start
        print("\n" + "=" * 60)
        print(f"✅ 全部完成! 总耗时: {format_time(total_time)}")
        print("=" * 60)
        print(f"\n📄 结果文件: {output_dir / 'final_results.json'}")
        
        # 显示失败条目
        failed_file = output_dir / 'failed_entries.json'
        if failed_file.exists():
            print(f"⚠️  失败条目: {failed_file}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断")
        print("注意: 已处理的批次结果已保存在output目录")
    except Exception as e:
        print(f"\n\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
