#!/usr/bin/env python3
"""
知识库索引自动更新脚本
扫描 entries/ 目录下所有算法条目，自动更新 INDEX.md 和 README.md
"""

import os
import re
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MATH_DIR = BASE_DIR / "数学建模"
ENTRIES_DIR = MATH_DIR / "entries"
INDEX_FILE = MATH_DIR / "INDEX.md"
ROOT_INDEX = BASE_DIR / "INDEX.md"
README_FILE = BASE_DIR / "README.md"

# 分类图标
CATEGORY_ICONS = {
    "评价模型": "🏆",
    "预测模型": "🔮",
    "优化模型": "⚡",
    "分类模型": "🧩",
    "聚类模型": "🔗",
    "降维算法": "📉",
    "智能算法": "🧠",
    "统计与时间序列": "📊"
}

# 分类显示名称
CATEGORY_DISPLAY = {
    "评价模型": "🏆 评价模型",
    "预测模型": "🔮 预测模型",
    "优化模型": "⚡ 优化模型",
    "分类模型": "🧩 分类模型",
    "聚类模型": "🔗 聚类模型",
    "降维算法": "📉 降维算法",
    "智能算法": "🧠 智能算法 / 启发式算法",
    "统计与时间序列": "📊 统计与时间序列"
}


def parse_frontmatter(content):
    """解析 markdown 文件的 YAML frontmatter"""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    frontmatter = {}
    for line in match.group(1).strip().split('\n'):
        m = re.match(r'^(\w+):\s*(.+)$', line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            # 处理引号
            val = val.strip('"').strip("'")
            # 处理列表 [a, b, c]
            if val.startswith('[') and val.endswith(']'):
                val = [v.strip().strip('"').strip("'") for v in val[1:-1].split(',')]
            frontmatter[key] = val
    return frontmatter


def scan_entries():
    """扫描所有算法条目，返回按分类组织的字典"""
    entries = []
    for f in sorted(ENTRIES_DIR.glob("*.md")):
        content = f.read_text(encoding='utf-8')
        meta = parse_frontmatter(content)
        if not meta.get('title'):
            continue
        entries.append({
            'file': f.name,
            'title': meta.get('title', f.stem),
            'category': meta.get('category', '未分类'),
            'tags': meta.get('tags', []),
            'difficulty': meta.get('difficulty', '⭐'),
            'description': extract_description(content)
        })
    
    # 按分类分组
    categorized = {}
    for e in entries:
        cat = e['category']
        if cat not in categorized:
            categorized[cat] = []
        categorized[cat].append(e)
    
    # 按固定分类顺序排序
    ordered = {}
    for cat in CATEGORY_DISPLAY:
        if cat in categorized:
            ordered[cat] = categorized[cat]
    # 未列出的分类也加上
    for cat in categorized:
        if cat not in ordered:
            ordered[cat] = categorized[cat]
    
    return ordered, entries


def extract_description(content):
    """从内容中提取简短说明（从原理部分提取第一句话）"""
    # 跳过 frontmatter
    body = re.sub(r'^---.*?---\n*', '', content, flags=re.DOTALL)
    # 找第一段有意义的文字
    lines = body.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('!') and \
           not line.startswith('```') and len(line) > 10:
            # 去除 markdown 格式
            clean = re.sub(r'[#*$_{}\[\]\\]', '', line)
            clean = re.sub(r'$$', '', clean)
            clean = clean.strip()
            if len(clean) > 8:
                return clean[:60] + ('...' if len(clean) > 60 else '')
    return ''


def build_category_table(cat, entries):
    """为单个分类生成表格"""
    display = CATEGORY_DISPLAY.get(cat, cat)
    lines = [f"### {display}"]
    lines.append(f"| 算法 | 难度 | 说明 |")
    lines.append(f"|------|------|------|")
    for e in entries:
        desc = e['description'] or ''
        fname = e['file']
        # README 中路径不同
        lines.append(f"| [{e['title']}](./entries/{fname}) | {e['difficulty']} | {desc} |")
    return '\n'.join(lines)


def build_category_table_readme(cat, entries):
    """为 README 生成单个分类表格"""
    display = CATEGORY_DISPLAY.get(cat, cat)
    lines = [f"### {display}（{len(entries)}条）"]
    lines.append(f"| 算法 | 难度 | 说明 |")
    lines.append(f"|------|------|------|")
    for e in entries:
        desc = e['description'] or ''
        fname = e['file']
        lines.append(f"| [{e['title']}](数学建模/entries/{fname}) | {e['difficulty']} | {desc} |")
    return '\n'.join(lines)


def update_index_md(categorized, total):
    """更新 数学建模/INDEX.md"""
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 构建新的分类表格部分
    tables = []
    for cat in CATEGORY_DISPLAY:
        if cat in categorized:
            tables.append(build_category_table(cat, categorized[cat]))
        else:
            display = CATEGORY_DISPLAY.get(cat, cat)
            tables.append(f"### {display}\n| 算法 | 难度 | 说明 |\n|------|------|------|\n| _(待添加)_ | | |")
    
    # 替换分类表格区域（从第一个 ### 到 ## 📊 板块统计之前）
    table_start = content.find("### 🏆")
    table_end = content.find("## 📊 板块统计")
    
    if table_start != -1 and table_end != -1:
        new_content = content[:table_start] + '\n'.join(tables) + '\n\n' + content[table_end:]
        
        # 更新统计数字
        new_content = re.sub(r'- 算法总数: \*\*\d+\*\*', f'- 算法总数: **{total}**', new_content)
        
        with open(INDEX_FILE, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ 已更新 {INDEX_FILE.relative_to(BASE_DIR)}")
    else:
        print(f"⚠️ 无法定位 INDEX.md 中的表格区域")


def update_root_index(total):
    """更新根目录 INDEX.md 中的总条目数"""
    with open(ROOT_INDEX, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新数学建模行的条目数
    content = re.sub(
        r'(\| 📐 \[数学建模\].*?\]\(.*?\) \| )\d+( \|)',
        f'\\g<1>{total}\\g<2>',
        content
    )
    
    with open(ROOT_INDEX, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 已更新 {ROOT_INDEX.relative_to(BASE_DIR)}")


def update_readme(categorized, total):
    """更新 README.md"""
    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新结构部分的条目数
    content = re.sub(
        r'算法条目（共 \d+ 条）',
        f'算法条目（共 {total} 条）',
        content
    )
    
    # 更新分类表格区域
    table_start = content.find("### 🏆")
    table_end = content.find("---\n\n## 📖")
    
    if table_start != -1 and table_end != -1:
        tables = []
        for cat in CATEGORY_DISPLAY:
            if cat in categorized:
                tables.append(build_category_table_readme(cat, categorized[cat]))
            else:
                display = CATEGORY_DISPLAY.get(cat, cat)
                tables.append(f"### {display}（0条）\n| 算法 | 难度 | 说明 |\n|------|------|------|\n| _(待添加)_ | | |")
        
        new_content = content[:table_start] + '\n'.join(tables) + '\n\n' + content[table_end:]
        
        with open(README_FILE, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ 已更新 {README_FILE.relative_to(BASE_DIR)}")
    else:
        print(f"⚠️ 无法定位 README.md 中的表格区域")


def print_summary(categorized, total):
    """打印更新摘要"""
    print("\n" + "=" * 50)
    print("📊 知识库更新摘要")
    print("=" * 50)
    for cat, entries in categorized.items():
        icon = CATEGORY_ICONS.get(cat, '📁')
        print(f"  {icon} {cat}: {len(entries)} 条")
    print(f"\n  总计: {total} 条算法")
    print("=" * 50)


def main():
    print("🔍 正在扫描算法条目...")
    categorized, all_entries = scan_entries()
    total = len(all_entries)
    
    print(f"   找到 {total} 条算法\n")
    
    print("📝 更新索引文件...")
    update_index_md(categorized, total)
    update_root_index(total)
    update_readme(categorized, total)
    
    print_summary(categorized, total)
    print("\n✨ 所有文件已更新完成！（未推送至 GitHub）")


if __name__ == '__main__':
    main()
