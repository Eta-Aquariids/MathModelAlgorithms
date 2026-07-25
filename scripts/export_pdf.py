#!/usr/bin/env python3
"""
知识库 PDF 导出脚本
将 Markdown 算法条目转换为 PDF 文件

用法:
  python3 scripts/export_pdf.py                        # 导出所有条目
  python3 scripts/export_pdf.py 层次分析法             # 导出指定条目
  python3 scripts/export_pdf.py 线性规划 逻辑回归      # 导出多个
  python3 scripts/export_pdf.py --all                  # 同上，导出全部
  python3 scripts/export_pdf.py --list                 # 列出所有可导出的条目
  python3 scripts/export_pdf.py --output ./my_pdfs     # 指定输出目录
"""

import os
import sys
import subprocess
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENTRIES_DIR = BASE_DIR / "数学建模" / "entries"
OUTPUT_DIR = BASE_DIR / "pdf_output"


def list_entries():
    """列出所有条目"""
    files = sorted(ENTRIES_DIR.glob("*.md"))
    print("可导出的算法条目：")
    for f in files:
        name = f.stem
        title = extract_title(f)
        print(f"  {name:30s}  {title}")
    print(f"\n共 {len(files)} 条")


def extract_title(filepath):
    """从 frontmatter 提取标题"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'^title:\s*"(.+)"', content, re.MULTILINE)
    return m.group(1) if m else filepath.stem


def convert_single(filepath, output_dir):
    """将单个 md 文件转换为 pdf"""
    name = filepath.stem
    output_path = output_dir / f"{name}.pdf"
    
    cmd = [
        'pandoc', str(filepath),
        '-f', 'markdown',
        '--mathml',
        '--pdf-engine=wkhtmltopdf',
        '-o', str(output_path)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    
    if output_path.exists():
        size = output_path.stat().st_size
        status = "✅" if size > 1000 else "⚠️"
        print(f"  {status} {name:30s}  {size//1024:4d} KB")
        return True
    else:
        print(f"  ❌ {name:30s}  转换失败")
        if result.stderr:
            # 只显示非噪音的错误
            for line in result.stderr.split('\n'):
                if 'Error' in line or 'error' in line or 'Fatal' in line:
                    print(f"     错误: {line}")
        return False


def convert_all(filters=None, output_dir=None):
    """转换所有（或指定的）条目"""
    if output_dir is None:
        output_dir = OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    
    files = sorted(ENTRIES_DIR.glob("*.md"))
    
    if filters:
        files = [f for f in files if f.stem in filters]
    
    if not files:
        print("未找到匹配的条目")
        return
    
    print(f"📄 正在转换 {len(files)} 个条目 → {output_dir}/\n")
    
    success = 0
    for f in files:
        if convert_single(f, output_dir):
            success += 1
    
    print(f"\n{'='*50}")
    print(f"完成: {success}/{len(files)} 成功")
    print(f"输出目录: {output_dir.resolve()}")


def main():
    args = sys.argv[1:]
    
    # 解析输出目录参数
    output_dir = OUTPUT_DIR
    if '--output' in args:
        idx = args.index('--output')
        if idx + 1 < len(args):
            output_dir = Path(args[idx + 1])
            args = args[:idx] + args[idx+2:]
    
    if not args or '--all' in args:
        convert_all(output_dir=output_dir)
    elif '--list' in args:
        list_entries()
    else:
        # 将参数作为条目名称过滤
        convert_all(filters=args, output_dir=output_dir)


if __name__ == '__main__':
    main()
