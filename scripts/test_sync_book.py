import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from sync_book import inject_frontmatter, parse_chapter, sync


def make_src(tmp_path, files: dict) -> Path:
    src = tmp_path / 'book-repo'
    src.mkdir()
    for name, content in files.items():
        (src / name).write_text(content, encoding='utf-8')
    return src


def test_parse_chapter_standard():
    assert parse_chapter('01-第1章-FDE的崛起.md') == (1, '第1章-FDE的崛起')


def test_parse_chapter_rejects_non_chapter():
    assert parse_chapter('README.md') is None
    assert parse_chapter('VERSION') is None


def test_inject_frontmatter_adds_title():
    out = inject_frontmatter('# 正文', '第1章')
    assert out.startswith('---\ntitle: 第1章\n---\n\n# 正文')


def test_inject_frontmatter_keeps_existing():
    src = '---\ntitle: 已有\n---\n# 正文'
    assert inject_frontmatter(src, '别的') == src


def test_sync_full(tmp_path):
    src = make_src(tmp_path, {
        '00-自序.md': '# 自序',
        '01-第1章-FDE的崛起.md': '# 第1章',
        'README.md': 'readme',
        'VERSION': '1.0.23',
    })
    docs = tmp_path / 'site' / 'docs'
    chapters = sync(src, docs)

    assert [c['order'] for c in chapters] == [0, 1]
    book = docs / 'book'
    assert (book / '00-自序.md').read_text(encoding='utf-8').startswith('---\ntitle: 自序')
    sidebar = json.loads((docs / '.vitepress' / 'book-sidebar.json').read_text(encoding='utf-8'))
    assert sidebar == [
        {'text': '自序', 'link': '/book/00-自序'},
        {'text': '第1章-FDE的崛起', 'link': '/book/01-第1章-FDE的崛起'},
    ]
    index = (book / 'index.md').read_text(encoding='utf-8')
    assert 'v1.0.23' in index


def test_sync_missing_source_exits(tmp_path):
    with pytest.raises(SystemExit):
        sync(tmp_path / '不存在', tmp_path / 'docs')
