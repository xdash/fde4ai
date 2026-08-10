#!/usr/bin/env python3
"""sync_book.py — 把书 repo 的章节 md 同步为 VitePress 文档。

用法: python3 sync_book.py <书repo根目录> <站点docs目录>
源目录即书 repo 根（本地: /Users/xdash/Documents/Obsidian_Sync/Writings/fde-book/github）。
章节文件名规范: NN-标题.md；非章节文件（README/VERSION/PDF）跳过并打 warning。
"""
import json
import re
import sys
from pathlib import Path

CHAPTER_RE = re.compile(r'^(\d+)-(.+)\.md$')
BOOK_REPO_URL = 'https://github.com/xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer'


def parse_chapter(filename: str):
    m = CHAPTER_RE.match(filename)
    if not m:
        return None
    return int(m.group(1)), m.group(2)


def inject_frontmatter(text: str, title: str) -> str:
    if text.startswith('---'):
        return text  # 已有 frontmatter，不覆写
    return f'---\ntitle: {title}\n---\n\n' + text


def read_version(src_dir: Path) -> str:
    vf = src_dir / 'VERSION'
    raw = vf.read_text(encoding='utf-8').strip() if vf.exists() else 'unknown'
    return raw if raw.startswith('v') else f'v{raw}'


def write_book_index(book_dir: Path, chapters: list, version: str) -> None:
    lines = [
        '# 《前线部署工程师》开源版\n',
        f'> 当前版本 {version} · 与 [GitHub 仓库]({BOOK_REPO_URL}) 自动同步\n',
        f'免费全文阅读。发现错漏欢迎到 [GitHub]({BOOK_REPO_URL}) 提 Issue 或 PR。\n',
        '## 目录\n',
    ]
    for c in chapters:
        lines.append(f"- [{c['title']}](/book/{c['file'][:-3]})")
    (book_dir / 'index.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def write_sidebar(dest_docs: Path, chapters: list) -> None:
    sidebar = [{'text': c['title'], 'link': f"/book/{c['file'][:-3]}"} for c in chapters]
    out = dest_docs / '.vitepress' / 'book-sidebar.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(sidebar, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def sync(src_dir, dest_docs) -> list:
    src_dir = Path(src_dir)
    dest_docs = Path(dest_docs)
    if not src_dir.is_dir():
        sys.exit(f'❌ 书稿源目录不存在: {src_dir}')
    book_dir = dest_docs / 'book'
    book_dir.mkdir(parents=True, exist_ok=True)

    # 清理旧章节（只清符合命名规范的文件，不碰 index.md 等其他内容）
    for old in book_dir.glob('*.md'):
        if CHAPTER_RE.match(old.name):
            old.unlink()

    chapters = []
    for f in sorted(src_dir.glob('*.md')):
        parsed = parse_chapter(f.name)
        if not parsed:
            print(f'⚠️ 跳过非章节文件: {f.name}')
            continue
        order, title = parsed
        dest = book_dir / f.name
        dest.write_text(inject_frontmatter(f.read_text(encoding='utf-8'), title), encoding='utf-8')
        chapters.append({'order': order, 'title': title, 'file': f.name})
        print(f'✅ 同步: {f.name}')

    if not chapters:
        sys.exit(f'❌ 源目录没有任何章节文件: {src_dir}')

    version = read_version(src_dir)
    write_book_index(book_dir, chapters, version)
    write_sidebar(dest_docs, chapters)
    print(f'📚 共同步 {len(chapters)} 章，版本 {version}')
    return chapters


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit('用法: python3 sync_book.py <书repo根目录> <站点docs目录>')
    sync(sys.argv[1], sys.argv[2])
