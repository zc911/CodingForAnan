# build.py
import re
import os
import shutil
from pathlib import Path
import markdown as md_lib
from jinja2 import Environment, FileSystemLoader

CONTENT_DIR = Path("content")
DIST_DIR = Path("dist")
TEMPLATES_DIR = Path("templates")

_CODE_BLOCK_RE = re.compile(
    r'```python\s+(demo|exercise)\s+title="([^"]+)"\n(.*?)```',
    re.DOTALL
)


def parse_code_blocks(md_text):
    """Return list of dicts with keys: type, title, code."""
    return [
        {'type': m.group(1), 'title': m.group(2), 'code': m.group(3).strip()}
        for m in _CODE_BLOCK_RE.finditer(md_text)
    ]


def _html_escape(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _render_code_block(block):
    code = _html_escape(block['code'])
    idx = block['index']
    if block['type'] == 'demo':
        return (
            f'<div class="code-block demo-block">'
            f'<div class="code-block-header">📖 演示：{block["title"]}</div>'
            f'<textarea class="code-editor" id="editor-{idx}">{code}</textarea>'
            f'<div class="code-actions">'
            f'<button class="run-btn" data-index="{idx}">▶ 运行</button>'
            f'</div>'
            f'<div class="code-block-input-area" id="inputs-{idx}"></div>'
            f'<div class="output-area" id="output-{idx}"></div>'
            f'</div>'
        )
    else:
        filename = f"exercise_{idx:02d}.py"
        return (
            f'<div class="code-block exercise-block">'
            f'<div class="code-block-header">✏️ 练习：{block["title"]}</div>'
            f'<textarea class="code-editor" id="editor-{idx}">{code}</textarea>'
            f'<div class="code-actions">'
            f'<button class="run-btn" data-index="{idx}">▶ 运行</button>'
            f'<button class="download-btn" data-index="{idx}" data-filename="{filename}">💾 下载到 Thonny</button>'
            f'</div>'
            f'<div class="code-block-input-area" id="inputs-{idx}"></div>'
            f'<div class="output-area" id="output-{idx}"></div>'
            f'</div>'
        )


def md_to_html_body(md_text):
    """Convert Markdown to HTML. Custom code blocks become interactive widgets."""
    counter = [0]
    placeholders = {}

    def replace_block(match):
        idx = counter[0]
        counter[0] += 1
        key = f'CODEBLOCK{idx}CODEBLOCK'
        placeholders[key] = {
            'type': match.group(1),
            'title': match.group(2),
            'code': match.group(3).strip(),
            'index': idx,
        }
        return key

    processed = _CODE_BLOCK_RE.sub(replace_block, md_text)
    html = md_lib.markdown(processed, extensions=['fenced_code', 'tables'])

    for key, block in placeholders.items():
        widget = _render_code_block(block)
        html = html.replace(f'<p>{key}</p>', widget)
        html = html.replace(key, widget)

    return html


def render_lesson(md_text, lesson_num, title, prev, next_lesson):
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    template = env.get_template("lesson.html")
    return template.render(
        body=md_to_html_body(md_text),
        lesson_num=lesson_num,
        title=title,
        prev=prev,
        next=next_lesson,
    )


def _load_lessons():
    lessons = []
    for lesson_dir in sorted(CONTENT_DIR.iterdir()):
        if not lesson_dir.is_dir():
            continue
        lesson_md = lesson_dir / "lesson.md"
        if not lesson_md.exists():
            continue
        meta = lesson_dir / "meta.txt"
        lines = meta.read_text(encoding='utf-8').splitlines() if meta.exists() else []
        title = lines[0] if lines else lesson_dir.name
        summary = lines[1] if len(lines) > 1 else ""
        num_str = lesson_dir.name.split('-')[0]
        num = int(''.join(filter(str.isdigit, num_str))) if any(c.isdigit() for c in num_str) else 0
        lessons.append({
            'num': num,
            'slug': lesson_dir.name,
            'title': title,
            'summary': summary,
            'md': lesson_md.read_text(encoding='utf-8'),
        })
    return lessons


def build():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir()

    if Path("static").exists():
        shutil.copytree("static", DIST_DIR / "static")

    redirects = Path("_redirects")
    if redirects.exists():
        shutil.copy(redirects, DIST_DIR / "_redirects")

    lessons = _load_lessons()
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))

    for i, lesson in enumerate(lessons):
        prev = lessons[i - 1] if i > 0 else None
        nxt = lessons[i + 1] if i < len(lessons) - 1 else None
        html = render_lesson(lesson['md'], lesson['num'], lesson['title'], prev, nxt)
        out_dir = DIST_DIR / lesson['slug']
        out_dir.mkdir()
        (out_dir / "index.html").write_text(html, encoding='utf-8')
        ex_dir = CONTENT_DIR / lesson['slug'] / "exercises"
        if ex_dir.exists():
            shutil.copytree(ex_dir, out_dir / "exercises")

    index_tmpl = env.get_template("index.html")
    (DIST_DIR / "index.html").write_text(
        index_tmpl.render(lessons=lessons), encoding='utf-8'
    )
    print(f"Built {len(lessons)} lessons → {DIST_DIR}/")


if __name__ == "__main__":
    build()
