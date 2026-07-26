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
    
    # CSS 样式：中文字体 + 代码块 + 表格样式
    css = """
    <style>
    body { font-family: 'WenQuanYi Micro Hei', 'Noto Sans CJK SC', sans-serif; font-size: 14px; line-height: 1.7; }
    h1, h2, h3, h4 { font-family: 'WenQuanYi Micro Hei', 'Noto Sans CJK SC', sans-serif; }
    code { font-family: 'Courier New', monospace; font-size: 13px; background: #f4f4f4; padding: 2px 5px; border-radius: 3px; }
    pre { background: #f8f8f8; border: 1px solid #ddd; border-radius: 5px; padding: 12px; overflow-x: auto; }
    pre code { background: none; padding: 0; }
    table { border-collapse: collapse; width: 100%; margin: 10px 0; }
    th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: left; }
    th { background: #f0f0f0; font-weight: bold; }
    blockquote { border-left: 4px solid #4a90d9; margin: 10px 0; padding: 8px 15px; background: #f9f9f9; }
    img { max-width: 100%; }
    .math { color: #333; }
    </style>
    </head>
    """
    
    # 先生成 HTML，再转 PDF（以便嵌入 CSS）
    html_path = output_path.with_suffix('.html')
    cmd_html = [
        'pandoc', str(filepath),
        '-f', 'markdown', '-t', 'html',
        '--mathml', '--standalone',
        '-o', str(html_path)
    ]
    
    subprocess.run(cmd_html, capture_output=True, text=True, timeout=30)
    
    # 在 </head> 前插入 CSS
    if html_path.exists():
        html_content = html_path.read_text(encoding='utf-8')
        html_content = html_content.replace('</head>', css)
        html_path.write_text(html_content, encoding='utf-8')
    
    cmd = [
        'wkhtmltopdf',
        '--encoding', 'utf-8',
        '--enable-local-file-access',
        str(html_path),
        str(output_path)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    
    # 清理临时 HTML
    if html_path.exists():
        html_path.unlink()
    
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
