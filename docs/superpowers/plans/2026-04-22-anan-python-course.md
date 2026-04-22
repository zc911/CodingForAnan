# Anan Python Course Website — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a static Python learning website for a 9-year-old, deployable to Cloudflare Pages, with in-browser Python execution (Pyodide + CodeMirror 5) and 14 lessons + 3 projects across 4 learning stages.

**Architecture:** A Python build script (`build.py`) reads Markdown lesson files with custom `python demo` / `python exercise` code block syntax, renders them through Jinja2 templates into static HTML in `dist/`. The frontend uses Pyodide (CDN) for in-browser Python and CodeMirror 5 (CDN) for syntax-highlighted editing — no bundler needed. An `input()` shim lets browser demos handle interactive input via pre-filled fields.

**Tech Stack:** Python 3.11+, Jinja2 3.x, python-markdown, pytest, Pyodide 0.26.4, CodeMirror 5.65, vanilla CSS/JS, Cloudflare Pages

---

## File Map

| File | Responsibility |
|------|---------------|
| `build.py` | Markdown → HTML pipeline, code block parsing, Jinja2 rendering |
| `templates/base.html` | Page shell: CDN links, Pyodide loading bar, site header |
| `templates/lesson.html` | Lesson page: prev/next nav, dual-column layout, complete button |
| `templates/index.html` | Course directory: lesson cards with localStorage progress |
| `static/editor.js` | CodeMirror init, Pyodide run handler, `input()` shim, download button |
| `static/style.css` | Child-friendly visual design |
| `_redirects` | Cloudflare Pages routing |
| `content/NN-slug/lesson.md` | Course content per lesson (Markdown + custom code blocks) |
| `content/NN-slug/meta.txt` | Line 1: lesson title. Line 2: one-line summary |
| `content/NN-slug/exercises/*.py` | Downloadable exercise starters for Thonny |
| `tests/test_build.py` | Unit tests for build script |

---

## Phase 1: Infrastructure

### Task 1: Project Setup

**Files:**
- Create: `requirements.txt`
- Create: `requirements-dev.txt`
- Create: `.gitignore`

- [ ] **Step 1: Create `requirements.txt`**

```
jinja2==3.1.4
markdown==3.7
```

- [ ] **Step 2: Create `requirements-dev.txt`**

```
pytest==8.3.4
```

- [ ] **Step 3: Create `.gitignore`**

```
dist/
__pycache__/
*.pyc
.pytest_cache/
.coverage
```

- [ ] **Step 4: Install dependencies**

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

Expected: packages install without errors.

- [ ] **Step 5: Create directory skeleton**

```bash
mkdir -p templates static/images tests
mkdir -p content/01-hello/exercises
mkdir -p content/02-variables/exercises
mkdir -p content/03-input-output/exercises
mkdir -p content/04-conditionals/exercises
mkdir -p content/05-while/exercises
mkdir -p content/06-for/exercises
mkdir -p content/07-p1-guess-game/exercises
mkdir -p content/08-lists/exercises
mkdir -p content/09-functions/exercises
mkdir -p content/10-strings/exercises
mkdir -p content/11-modules/exercises
mkdir -p content/12-p2-turtle/exercises
mkdir -p content/13-dicts/exercises
mkdir -p content/14-files/exercises
mkdir -p content/15-errors/exercises
mkdir -p content/16-algorithms/exercises
mkdir -p content/17-p3-final/exercises
```

- [ ] **Step 6: Commit**

```bash
git init
git add requirements.txt requirements-dev.txt .gitignore
git commit -m "chore: project setup"
```

---

### Task 2: Build Script — Tests First

**Files:**
- Create: `tests/test_build.py`

- [ ] **Step 1: Write failing tests**

```python
# tests/test_build.py
import pytest
from build import parse_code_blocks, md_to_html_body, render_lesson


def test_demo_block_detected():
    md = '```python demo title="Hello"\nprint("hi")\n```'
    blocks = parse_code_blocks(md)
    assert len(blocks) == 1
    assert blocks[0]['type'] == 'demo'
    assert blocks[0]['title'] == 'Hello'
    assert blocks[0]['code'] == 'print("hi")'


def test_exercise_block_detected():
    md = '```python exercise title="Try it"\nname = "___"\n```'
    blocks = parse_code_blocks(md)
    assert blocks[0]['type'] == 'exercise'
    assert blocks[0]['title'] == 'Try it'


def test_plain_code_block_ignored():
    md = '```python\nx = 1\n```'
    blocks = parse_code_blocks(md)
    assert blocks == []


def test_demo_html_has_run_button():
    md = '```python demo title="Run me"\nprint("hi")\n```'
    html = md_to_html_body(md)
    assert '▶ 运行' in html
    assert 'demo-block' in html


def test_exercise_html_has_download_button():
    md = '```python exercise title="Do it"\nx = 1\n```'
    html = md_to_html_body(md)
    assert '下载到 Thonny' in html
    assert 'exercise-block' in html
```

- [ ] **Step 2: Run to confirm they fail**

```bash
pytest tests/test_build.py -v
```

Expected: `ModuleNotFoundError: No module named 'build'`

- [ ] **Step 3: Commit tests**

```bash
git add tests/test_build.py
git commit -m "test: build script unit tests"
```

---

### Task 3: Build Script Implementation

**Files:**
- Create: `build.py`

- [ ] **Step 1: Create `build.py`**

```python
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
```

- [ ] **Step 2: Run tests — all must pass**

```bash
pytest tests/test_build.py -v
```

Expected: 5 tests PASS.

- [ ] **Step 3: Commit**

```bash
git add build.py
git commit -m "feat: build script with Markdown parser and Jinja2 renderer"
```

---

### Task 4: HTML Templates

**Files:**
- Create: `templates/base.html`
- Create: `templates/lesson.html`
- Create: `templates/index.html`

- [ ] **Step 1: Create `templates/base.html`**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}Anan 的 Python 课程{% endblock %}</title>
  <link rel="stylesheet" href="/static/style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.17/codemirror.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.17/theme/dracula.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.17/codemirror.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.17/mode/python/python.min.js"></script>
  <script src="https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js"></script>
</head>
<body>
  <header class="site-header">
    <a href="/" class="site-logo">🐍 Anan 的 Python 课程</a>
  </header>

  <div id="pyodide-status" class="pyodide-status loading">
    <span>正在加载 Python 环境…</span>
    <div class="progress-bar"><div class="progress-fill"></div></div>
  </div>

  <main>{% block content %}{% endblock %}</main>

  <script src="/static/editor.js"></script>
  {% block scripts %}{% endblock %}
</body>
</html>
```

- [ ] **Step 2: Create `templates/lesson.html`**

```html
{% extends "base.html" %}
{% block title %}第{{ lesson_num }}课：{{ title }}{% endblock %}

{% block content %}
<div class="lesson-nav">
  {% if prev %}
    <a href="/{{ prev.slug }}/" class="nav-btn">← 第{{ prev.num }}课</a>
  {% else %}
    <span class="nav-btn disabled">← 上一课</span>
  {% endif %}
  <span class="lesson-title-nav">第{{ lesson_num }}课：{{ title }}</span>
  {% if next %}
    <a href="/{{ next.slug }}/" class="nav-btn">第{{ next.num }}课 →</a>
  {% else %}
    <span class="nav-btn disabled">下一课 →</span>
  {% endif %}
</div>

<div class="lesson-layout">
  <article class="lesson-body">{{ body | safe }}</article>
  <aside class="cheatsheet">
    <h3>📌 本课要点</h3>
    <div id="cheatsheet-content"></div>
  </aside>
</div>

<div class="lesson-footer">
  <button class="complete-btn" id="complete-btn" data-lesson="{{ lesson_num }}">
    ✅ 标记本课完成
  </button>
</div>
{% endblock %}

{% block scripts %}
<script>
  // Populate cheatsheet from h2 headings
  document.querySelectorAll('.lesson-body h2').forEach(h => {
    const item = document.createElement('div');
    item.className = 'cheatsheet-item';
    item.textContent = h.textContent;
    document.getElementById('cheatsheet-content').appendChild(item);
  });
  // Completion tracking
  const btn = document.getElementById('complete-btn');
  const key = 'lesson_' + btn.dataset.lesson + '_complete';
  if (localStorage.getItem(key)) { btn.textContent = '✅ 已完成！'; btn.classList.add('done'); }
  btn.addEventListener('click', () => {
    localStorage.setItem(key, '1');
    btn.textContent = '✅ 已完成！';
    btn.classList.add('done');
  });
</script>
{% endblock %}
```

- [ ] **Step 3: Create `templates/index.html`**

```html
{% extends "base.html" %}
{% block title %}Anan 的 Python 课程 — 目录{% endblock %}

{% block content %}
<div class="index-hero">
  <h1>欢迎来到 Anan 的 Python 课程！🐍</h1>
  <p>一共 {{ lessons | length }} 节课，每节约 1 小时。加油！</p>
</div>
<div class="lessons-grid">
  {% for lesson in lessons %}
  <a href="/{{ lesson.slug }}/" class="lesson-card">
    <div class="lesson-num">第 {{ lesson.num }} 课</div>
    <div class="lesson-card-title">{{ lesson.title }}</div>
    <div class="lesson-card-summary">{{ lesson.summary }}</div>
    <div class="lesson-status" data-lesson="{{ lesson.num }}">○ 未开始</div>
  </a>
  {% endfor %}
</div>
{% endblock %}

{% block scripts %}
<script>
  document.querySelectorAll('.lesson-status').forEach(el => {
    if (localStorage.getItem('lesson_' + el.dataset.lesson + '_complete')) {
      el.textContent = '✅ 已完成';
      el.classList.add('done');
      el.closest('.lesson-card').classList.add('completed');
    }
  });
</script>
{% endblock %}
```

- [ ] **Step 4: Verify build runs (0 lessons, no errors)**

```bash
python build.py
```

Expected: `Built 0 lessons → dist/`

- [ ] **Step 5: Commit**

```bash
git add templates/
git commit -m "feat: Jinja2 HTML templates"
```

---

### Task 5: Frontend Editor (editor.js)

**Files:**
- Create: `static/editor.js`

- [ ] **Step 1: Create `static/editor.js`**

```javascript
// static/editor.js
'use strict';

let pyodide = null;
const editors = {};      // blockIndex -> CodeMirror instance
let currentRunIndex = null;

// ---- Pyodide ----
async function loadPyodideAndSetup() {
  const statusEl = document.getElementById('pyodide-status');
  try {
    pyodide = await loadPyodide({
      indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/',
      stdout: (text) => appendOutput(currentRunIndex, text),
      stderr: (text) => appendOutput(currentRunIndex, text, 'error'),
    });
    if (statusEl) {
      statusEl.className = 'pyodide-status ready';
      statusEl.querySelector('span').textContent = '✅ Python 环境已就绪';
      setTimeout(() => { statusEl.style.display = 'none'; }, 2000);
    }
    document.querySelectorAll('.run-btn').forEach(b => b.disabled = false);
  } catch (err) {
    if (statusEl) statusEl.querySelector('span').textContent = '❌ 加载失败，请刷新页面';
  }
}

// ---- Output ----
function appendOutput(index, text, type) {
  const el = document.getElementById('output-' + index);
  if (!el) return;
  const line = document.createElement('div');
  line.className = 'output-line' + (type === 'error' ? ' output-error' : '');
  line.textContent = text;
  el.appendChild(line);
}

// ---- input() shim ----
function countInputCalls(code) {
  return (code.match(/\binput\s*\(/g) || []).length;
}

function renderInputFields(index, count) {
  const container = document.getElementById('inputs-' + index);
  if (!container) return;
  container.innerHTML = '';
  if (count === 0) return;
  const label = document.createElement('div');
  label.className = 'input-label';
  label.textContent = `模拟输入（共 ${count} 个，按顺序填写）：`;
  container.appendChild(label);
  for (let i = 0; i < count; i++) {
    const f = document.createElement('input');
    f.type = 'text';
    f.className = 'input-field';
    f.placeholder = `第 ${i + 1} 个 input() 的值`;
    container.appendChild(f);
  }
}

function getInputValues(index) {
  const container = document.getElementById('inputs-' + index);
  if (!container) return [];
  return Array.from(container.querySelectorAll('.input-field')).map(f => f.value);
}

function buildInputShim(values) {
  return `
import builtins as _b
_q = ${JSON.stringify(values)}
_qi = [0]
def _input(prompt=''):
    i = _qi[0]
    val = _q[i] if i < len(_q) else ''
    _qi[0] += 1
    if prompt: print(prompt + str(val))
    return str(val)
_b.input = _input
`;
}

// ---- Run ----
async function runCode(index) {
  if (!pyodide) return;
  document.getElementById('output-' + index).innerHTML = '';
  currentRunIndex = index;

  const cm = editors[index];
  const code = cm ? cm.getValue() : (document.getElementById('editor-' + index) || {}).value || '';
  const inputCount = countInputCalls(code);
  const inputValues = getInputValues(index);

  if (inputCount > 0 && inputValues.length < inputCount) {
    renderInputFields(index, inputCount);
    appendOutput(index, `⚠️ 请先填写 ${inputCount} 个模拟输入，再点击运行。`, 'error');
    return;
  }

  try {
    await pyodide.runPythonAsync(buildInputShim(inputValues) + '\n' + code);
    if (Math.random() < 0.25) showCelebration();
  } catch (err) {
    appendOutput(index, friendlyError(err.message), 'error');
  }
}

function friendlyError(msg) {
  if (msg.includes('SyntaxError')) return '❌ 语法错误：检查括号和引号是否正确。\n' + msg;
  if (msg.includes('NameError')) return '❌ 变量名错误：是不是有词拼错了？\n' + msg;
  if (msg.includes('IndentationError')) return '❌ 缩进错误：检查每行前面的空格数量。\n' + msg;
  if (msg.includes('TypeError')) return '❌ 类型错误：两种数据类型不能直接操作。\n' + msg;
  return '❌ 出错了：' + msg;
}

// ---- Download ----
function downloadCode(index, filename) {
  const cm = editors[index];
  const code = cm ? cm.getValue() : '';
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([code], { type: 'text/plain' }));
  a.download = filename || `exercise_${index}.py`;
  a.click();
}

// ---- Celebration ----
function showCelebration() {
  const phrases = ['🎉 太棒了！', '✨ 厉害！', '🌟 做到了！', '👏 真棒！'];
  const el = document.createElement('div');
  el.className = 'celebration';
  el.textContent = phrases[Math.floor(Math.random() * phrases.length)];
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 2000);
}

// ---- Init ----
document.addEventListener('DOMContentLoaded', () => {
  // CodeMirror for every textarea.code-editor
  document.querySelectorAll('textarea.code-editor').forEach(ta => {
    const index = ta.id.replace('editor-', '');
    const cm = CodeMirror.fromTextArea(ta, {
      mode: 'python',
      theme: 'dracula',
      lineNumbers: true,
      indentUnit: 4,
      tabSize: 4,
      indentWithTabs: false,
      lineWrapping: true,
      extraKeys: { Tab: (cm) => cm.replaceSelection('    ') },
    });
    editors[index] = cm;
    // Exercise blocks: show input fields based on code content
    if (ta.closest('.exercise-block')) {
      cm.on('change', () => renderInputFields(index, countInputCalls(cm.getValue())));
      renderInputFields(index, countInputCalls(cm.getValue()));
    }
  });

  document.querySelectorAll('.run-btn').forEach(btn => {
    btn.disabled = true;
    btn.addEventListener('click', () => runCode(btn.dataset.index));
  });

  document.querySelectorAll('.download-btn').forEach(btn => {
    btn.addEventListener('click', () => downloadCode(btn.dataset.index, btn.dataset.filename));
  });

  loadPyodideAndSetup();
});
```

- [ ] **Step 2: Commit**

```bash
git add static/editor.js
git commit -m "feat: Pyodide + CodeMirror editor with input() shim"
```

---

### Task 6: CSS Styling

**Files:**
- Create: `static/style.css`

- [ ] **Step 1: Create `static/style.css`**

```css
/* static/style.css */
:root {
  --primary: #2563eb;
  --primary-light: #dbeafe;
  --success: #16a34a;
  --success-light: #dcfce7;
  --bg: #f8fafc;
  --card-bg: #ffffff;
  --text: #1e293b;
  --text-muted: #64748b;
  --border: #e2e8f0;
  --code-bg: #282a36;
  --radius: 12px;
  --font: 'Segoe UI', system-ui, sans-serif;
  --mono: 'JetBrains Mono', 'Fira Code', monospace;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: var(--font); font-size: 18px; line-height: 1.7; color: var(--text); background: var(--bg); }

/* Header */
.site-header { background: var(--primary); padding: 12px 24px; position: sticky; top: 0; z-index: 100; }
.site-logo { color: white; text-decoration: none; font-size: 1.2rem; font-weight: 700; }

/* Pyodide status bar */
.pyodide-status { background: var(--primary-light); text-align: center; padding: 8px; font-size: 0.9rem; }
.pyodide-status.ready { background: var(--success-light); color: var(--success); }
.progress-bar { height: 4px; background: #bfdbfe; margin-top: 4px; border-radius: 2px; overflow: hidden; }
.progress-fill { height: 100%; width: 40%; background: var(--primary); animation: pulse 1.5s ease-in-out infinite; }
@keyframes pulse { 0%,100% { width: 20%; } 50% { width: 80%; } }

/* Lesson navigation */
.lesson-nav { display: flex; align-items: center; justify-content: space-between; padding: 12px 24px; background: var(--card-bg); border-bottom: 1px solid var(--border); gap: 12px; }
.nav-btn { padding: 8px 16px; border-radius: 8px; background: var(--primary); color: white; text-decoration: none; font-size: 0.9rem; white-space: nowrap; }
.nav-btn.disabled { background: var(--border); color: var(--text-muted); pointer-events: none; }
.lesson-title-nav { font-weight: 600; text-align: center; flex: 1; }

/* Layout */
.lesson-layout { display: grid; grid-template-columns: 1fr; max-width: 1200px; margin: 0 auto; padding: 24px; gap: 24px; }
@media (min-width: 900px) { .lesson-layout { grid-template-columns: 3fr 1.5fr; } }

/* Body typography */
.lesson-body h1 { font-size: 1.8rem; margin-bottom: 16px; color: var(--primary); }
.lesson-body h2 { font-size: 1.4rem; margin: 28px 0 12px; border-left: 4px solid var(--primary); padding-left: 12px; }
.lesson-body h3 { font-size: 1.1rem; margin: 20px 0 8px; }
.lesson-body p { margin-bottom: 12px; }
.lesson-body ul, .lesson-body ol { margin: 8px 0 12px 24px; }
.lesson-body table { border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 0.95rem; }
.lesson-body th, .lesson-body td { border: 1px solid var(--border); padding: 8px 12px; }
.lesson-body th { background: var(--primary-light); }
.lesson-body code { background: #f1f5f9; padding: 2px 6px; border-radius: 4px; font-family: var(--mono); font-size: 0.9em; color: #be185d; }
.lesson-body blockquote { border-left: 4px solid #fbbf24; background: #fefce8; padding: 12px 16px; margin: 16px 0; border-radius: 0 8px 8px 0; font-style: italic; }

/* Code blocks */
.code-block { margin: 20px 0; border-radius: var(--radius); overflow: hidden; border: 2px solid var(--border); }
.demo-block { border-color: #93c5fd; }
.exercise-block { border-color: #86efac; }
.code-block-header { padding: 10px 16px; font-weight: 600; font-size: 0.95rem; }
.demo-block .code-block-header { background: #dbeafe; color: #1d4ed8; }
.exercise-block .code-block-header { background: #dcfce7; color: #15803d; }
.CodeMirror { font-family: var(--mono) !important; font-size: 15px !important; height: auto !important; min-height: 60px; }
.CodeMirror-scroll { max-height: 400px; }
.code-actions { display: flex; gap: 8px; padding: 8px 12px; background: var(--code-bg); }
.run-btn { padding: 6px 16px; background: #16a34a; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 0.9rem; font-weight: 600; }
.run-btn:disabled { background: #94a3b8; cursor: not-allowed; }
.run-btn:hover:not(:disabled) { background: #15803d; }
.download-btn { padding: 6px 16px; background: #0284c7; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 0.9rem; font-weight: 600; }
.download-btn:hover { background: #0369a1; }

/* input() shim fields */
.code-block-input-area { background: #1e293b; padding: 8px 12px; }
.input-label { color: #94a3b8; font-size: 0.85rem; margin-bottom: 4px; }
.input-field { display: block; width: 100%; padding: 6px 10px; margin-bottom: 4px; background: #334155; border: 1px solid #475569; color: white; border-radius: 6px; font-family: var(--mono); font-size: 0.9rem; }

/* Output */
.output-area { background: #1e293b; padding: 10px 14px; min-height: 32px; font-family: var(--mono); font-size: 14px; color: #e2e8f0; }
.output-line { white-space: pre-wrap; line-height: 1.5; }
.output-error { color: #fca5a5; }

/* Cheatsheet */
.cheatsheet { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; height: fit-content; position: sticky; top: 80px; font-size: 0.9rem; }
.cheatsheet h3 { font-size: 1rem; margin-bottom: 10px; color: var(--primary); }
.cheatsheet-item { padding: 6px 0; border-bottom: 1px solid var(--border); color: var(--text-muted); }

/* Lesson footer */
.lesson-footer { max-width: 1200px; margin: 0 auto; padding: 16px 24px 40px; }
.complete-btn { padding: 12px 24px; background: var(--primary); color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 1rem; font-weight: 600; }
.complete-btn.done { background: var(--success); }

/* Index */
.index-hero { text-align: center; padding: 48px 24px 24px; }
.index-hero h1 { font-size: 2rem; margin-bottom: 8px; color: var(--primary); }
.index-hero p { color: var(--text-muted); }
.lessons-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 16px; max-width: 1200px; margin: 0 auto; padding: 0 24px 48px; }
.lesson-card { background: var(--card-bg); border: 2px solid var(--border); border-radius: var(--radius); padding: 20px; text-decoration: none; color: var(--text); transition: border-color 0.2s, transform 0.15s; display: block; }
.lesson-card:hover { border-color: var(--primary); transform: translateY(-2px); }
.lesson-card.completed { border-color: var(--success); background: var(--success-light); }
.lesson-num { font-size: 0.8rem; color: var(--text-muted); margin-bottom: 4px; }
.lesson-card-title { font-weight: 700; font-size: 1rem; margin-bottom: 6px; }
.lesson-card-summary { font-size: 0.85rem; color: var(--text-muted); margin-bottom: 12px; }
.lesson-status { font-size: 0.8rem; color: var(--text-muted); }
.lesson-status.done { color: var(--success); font-weight: 600; }

/* Celebration animation */
.celebration { position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 3rem; animation: celebrate 2s ease-out forwards; pointer-events: none; z-index: 9999; }
@keyframes celebrate { 0% { opacity: 1; transform: translate(-50%,-50%) scale(0.5); } 60% { transform: translate(-50%,-65%) scale(1.4); } 100% { opacity: 0; transform: translate(-50%,-85%) scale(1); } }
```

- [ ] **Step 2: Commit**

```bash
git add static/style.css
git commit -m "feat: child-friendly CSS design"
```

---

### Task 7: Cloudflare Pages Config

**Files:**
- Create: `_redirects`

- [ ] **Step 1: Create `_redirects`**

```
/* /index.html 200
```

- [ ] **Step 2: Build and confirm `_redirects` appears in dist**

```bash
python build.py
ls dist/
```

Expected output includes `_redirects  index.html  static/`

- [ ] **Step 3: Commit**

```bash
git add _redirects
git commit -m "chore: Cloudflare Pages routing"
```

---

## Phase 2: Course Content

Each lesson task follows the same pattern: create `meta.txt`, `lesson.md`, and a `exercises/NN_name.py` file, then build and commit.

---

### Task 8: Lesson 01 — 计算机是怎么工作的？认识 Python

**Files:**
- Create: `content/01-hello/meta.txt`
- Create: `content/01-hello/lesson.md`
- Create: `content/01-hello/exercises/01_hello.py`

- [ ] **Step 1: Create `meta.txt`**

```
计算机是怎么工作的？认识 Python
第一次见到 Python，写出你的第一行代码
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第1课：计算机是怎么工作的？认识 Python

## 计算机在做什么？

计算机很简单：接收**输入**（比如你敲键盘），**处理**信息，然后给出**输出**（比如显示文字）。

就像你问一个问题（输入），别人想一想（处理），然后告诉你答案（输出）。

## Python 是什么？

Python 是一种**编程语言**——一种人和计算机都能读懂的语言。

你学过的 Scratch 也是编程语言，只不过用积木。Python 用文字代码，更像真正的程序员写的代码。

## 你的第一行 Python 代码

`print()` 让计算机把东西显示在屏幕上。括号里放你想显示的文字，文字要用引号包起来：

```python demo title="Hello, World！"
print("Hello, World!")
```

试着把 `World` 改成你自己的名字，然后点击运行！

```python demo title="打印多行"
print("你好，Anan！")
print("今天开始学 Python 啦！")
print("Let's go! 🚀")
```

## 重要提醒

- 括号 `()` 和引号 `""` 必须是**英文**符号（不能用中文括号）
- Python 区分大小写：`Print` 和 `print` 不一样
- `#` 开头的行是**注释**，计算机会忽略，只是给人看的说明

## 练习

```python exercise title="写出你的自我介绍"
# 用三行 print() 打印：
# 1. 你的名字
# 2. 你的年龄
# 3. 你最喜欢的动物

print("我叫 ___")
print("我今年 ___ 岁")
print("我最喜欢的动物是 ___")
```
````

- [ ] **Step 3: Create `exercises/01_hello.py`**

```python
# 第1课练习：写出你的自我介绍
# 把 ___ 替换成真实内容

print("我叫 ___")
print("我今年 ___ 岁")
print("我最喜欢的动物是 ___")

# 挑战：再加一行，打印你最喜欢的颜色
```

- [ ] **Step 4: Build and verify lesson renders**

```bash
python build.py
```

Expected: `Built 1 lessons → dist/`

Open `dist/01-hello/index.html` in a browser — page should show lesson content with two demo blocks and one exercise block.

- [ ] **Step 5: Commit**

```bash
git add content/01-hello/
git commit -m "content: lesson 01 - hello Python"
```

---

### Task 9: Lesson 02 — 变量和数据类型

**Files:**
- Create: `content/02-variables/meta.txt`
- Create: `content/02-variables/lesson.md`
- Create: `content/02-variables/exercises/02_variables.py`

- [ ] **Step 1: Create `meta.txt`**

```
变量和数据类型
用变量存储信息——就像给盒子贴标签
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第2课：变量和数据类型

## 什么是变量？

想象你有很多盒子，每个盒子贴了标签。你可以把东西放进去，也可以换成别的东西。

在 Python 里，**变量**就是这些盒子。`=` 号表示"把右边的值放进左边的变量"：

```python demo title="创建变量"
name = "Anan"
age = 9
height = 1.35

print(name)
print(age)
print(height)
```

## 四种基本数据类型

| 类型 | 英文 | 例子 | 说明 |
|------|------|------|------|
| 整数 | `int` | `9`, `100` | 没有小数点的数 |
| 小数 | `float` | `1.35`, `3.14` | 有小数点的数 |
| 文字 | `str` | `"Anan"` | 用引号包起来 |
| 真假 | `bool` | `True`, `False` | 只有这两个值 |

```python demo title="查看数据类型"
name = "Anan"
age = 9
height = 1.35
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

## 变量可以计算

```python demo title="用变量做数学"
age = 9
next_year = age + 1
print("明年我", next_year, "岁")

price = 3.5
count = 4
total = price * count
print("总价：", total, "元")
```

## 字符串拼接

用 `+` 把两段文字连在一起：

```python demo title="拼接字符串"
first_name = "An"
last_name = "an"
full_name = first_name + last_name
print("全名：" + full_name)
print("你好，" + full_name + "！")
```

## 练习

```python exercise title="关于我的变量"
# 创建下面这些变量，填入你自己的信息

name = "___"          # 你的名字（str）
age = ___             # 你的年龄（int）
height = ___          # 你的身高，单位米（float，如 1.35）
is_student = ___      # 你是不是学生？True 或 False

print("我叫", name)
print("我", age, "岁")
print("我的身高是", height, "米")
print("我是学生：", is_student)

# 计算10年后的年龄
future_age = age + 10
print("10年后我", future_age, "岁")
```

````

- [ ] **Step 3: Create `exercises/02_variables.py`**

```python
# 第2课练习：变量和数据类型
# 填入你自己的信息

name = "___"
age = 0
height = 0.0
is_student = True

print("我叫", name)
print("我", age, "岁")
print("我的身高是", height, "米")
print("我是学生：", is_student)

# 挑战：计算你和爸爸/妈妈的年龄差
parent_age = 0   # 填入爸爸或妈妈的年龄
age_diff = parent_age - age
print("年龄差：", age_diff, "岁")
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/02-variables/
git commit -m "content: lesson 02 - variables and data types"
```

---

### Task 10: Lesson 03 — 输入与输出

**Files:**
- Create: `content/03-input-output/meta.txt`
- Create: `content/03-input-output/lesson.md`
- Create: `content/03-input-output/exercises/03_input.py`

- [ ] **Step 1: Create `meta.txt`**

```
输入与输出
让程序和你对话——用 input() 接收回答
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第3课：输入与输出

## 让程序问问题

`input()` 让程序暂停，等你输入文字，然后把你输入的内容返回回来。

> **网页提示：** 在下面的演示里，先在"模拟输入"框填好答案，再点击运行。在 Thonny 里程序会真的等你打字！

```python demo title="问名字"
name = input("你叫什么名字？")
print("你好，" + name + "！欢迎来学 Python！")
```

## input() 总是返回字符串

不管你输入数字还是文字，`input()` 拿到的**永远是字符串**。要做数学就需要转换：

```python demo title="把输入转成数字"
age_text = input("你几岁了？")
age = int(age_text)
next_year = age + 1
print("明年你", next_year, "岁！")
```

常用转换：`int("9")` → 整数 9，`float("1.5")` → 小数 1.5

## 自我介绍生成器

```python demo title="自我介绍生成器"
name = input("你的名字：")
age = int(input("你的年龄："))
hobby = input("你的爱好：")

print("大家好！我叫" + name + "，")
print("今年", age, "岁，")
print("我喜欢" + hobby + "。")
```

## 练习（在 Thonny 里运行体验更好）

```python exercise title="自我介绍小程序"
name = input("你叫什么名字？")
age = int(input("你今年几岁？"))
hobby = input("你有什么爱好？")
food = input("你最喜欢吃什么？")

print()
print("===== 自我介绍 =====")
print("大家好！我叫", name + "。")
print("我今年", age, "岁。")
print("我喜欢", hobby + "。")
print("我最喜欢吃", food + "。")
print("很高兴认识大家！")
```
````

- [ ] **Step 3: Create `exercises/03_input.py`**

```python
# 第3课练习：输入与输出
# 在 Thonny 里运行，体验真正的 input()

name = input("你叫什么名字？")
age = int(input("你今年几岁？"))
hobby = input("你有什么爱好？")
food = input("你最喜欢吃什么？")

print()
print("===== 自我介绍 =====")
print("大家好！我叫", name + "。")
print("我今年", age, "岁。")
print("我喜欢", hobby + "。")
print("我最喜欢吃", food + "。")
print("很高兴认识大家！")
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/03-input-output/
git commit -m "content: lesson 03 - input and output"
```

---

### Task 11: Lesson 04 — 条件判断

**Files:**
- Create: `content/04-conditionals/meta.txt`
- Create: `content/04-conditionals/lesson.md`
- Create: `content/04-conditionals/exercises/04_conditionals.py`

- [ ] **Step 1: Create `meta.txt`**

```
条件判断：if / elif / else
让程序根据情况做不同的选择
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第4课：条件判断：if / elif / else

## 程序也要做选择

如果下雨就带伞，不下雨就不带——Python 也能做这种判断：

```python demo title="第一个 if 语句"
weather = "下雨"

if weather == "下雨":
    print("记得带伞！☂️")
else:
    print("今天天气不错！☀️")
```

**注意：** `==` 是"等于"（判断），`=` 是"赋值"（存值）！

## if 语句结构

```
if 条件:
    条件为真时执行（要缩进4个空格！）
elif 另一个条件:
    第二个条件为真时执行
else:
    以上都不满足时执行
```

## 比较运算符

| 符号 | 意思 | 例子 |
|------|------|------|
| `==` | 等于 | `age == 9` |
| `!=` | 不等于 | `age != 10` |
| `>` | 大于 | `score > 60` |
| `<` | 小于 | `score < 60` |
| `>=` | 大于等于 | `score >= 90` |
| `<=` | 小于等于 | `score <= 100` |

```python demo title="成绩等级判断"
score = 85

if score >= 90:
    print("优秀！🌟")
elif score >= 80:
    print("良好！👍")
elif score >= 60:
    print("及格 📚")
else:
    print("需要加油 💪")
```

试试把 `score` 改成不同数字！

## 练习

```python exercise title="奇数还是偶数？"
# % 是取余数运算符：8 % 2 = 0，7 % 2 = 1
number = 7

if number % 2 == 0:
    print(number, "是偶数")
else:
    print(number, "是奇数")
```
````

- [ ] **Step 3: Create `exercises/04_conditionals.py`**

```python
# 第4课练习：条件判断

# 练习1：奇偶数判断
number = int(input("输入一个整数："))
if number % 2 == 0:
    print(number, "是偶数")
else:
    print(number, "是奇数")

# 练习2：成绩等级
score = int(input("输入你的分数（0-100）："))
if score >= 90:
    print("优秀！🌟")
elif score >= 80:
    print("良好！👍")
elif score >= 60:
    print("及格 📚")
else:
    print("需要加油 💪")
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/04-conditionals/
git commit -m "content: lesson 04 - conditionals"
```

---

### Task 12: Lesson 05 — while 循环

**Files:**
- Create: `content/05-while/meta.txt`
- Create: `content/05-while/lesson.md`
- Create: `content/05-while/exercises/05_while.py`

- [ ] **Step 1: Create `meta.txt`**

```
while 循环
让程序反复做同一件事，直到条件不满足
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第5课：while 循环

## 重复做同一件事

如果要打印 1 到 5，不必写 5 行代码：

```python demo title="从1数到5"
count = 1
while count <= 5:
    print(count)
    count = count + 1
print("数完了！")
```

## while 的结构

```
while 条件:
    重复执行的代码（记得改变变量，否则会死循环！）
```

每次循环结束后，Python 回头检查条件：True 继续，False 退出。

## 倒计时

```python demo title="火箭倒计时 🚀"
n = 5
while n > 0:
    print(n, "...")
    n = n - 1
print("🚀 发射！")
```

## 累加求和

```python demo title="1 加到 100"
total = 0
i = 1
while i <= 100:
    total = total + i
    i = i + 1
print("1+2+...+100 =", total)
```

## 练习

```python exercise title="累加到 N"
# 计算 1+2+3+...+N 的和
N = 10   # 改成其他数字试试

total = 0
i = 1
while i <= N:
    total = total + i
    i = i + 1

print("1 + 2 + ... +", N, "=", total)
```
````

- [ ] **Step 3: Create `exercises/05_while.py`**

```python
# 第5课练习：while 循环

# 练习1：倒计时
n = int(input("从几开始倒计时？"))
while n > 0:
    print(n, "...")
    n = n - 1
print("时间到！⏰")

# 练习2：求 1 到 N 的和
N = int(input("计算 1 加到几？"))
total = 0
i = 1
while i <= N:
    total += i
    i += 1
print("结果：", total)
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/05-while/
git commit -m "content: lesson 05 - while loops"
```

---

### Task 13: Lesson 06 — for 循环与 range()

**Files:**
- Create: `content/06-for/meta.txt`
- Create: `content/06-for/lesson.md`
- Create: `content/06-for/exercises/06_for.py`

- [ ] **Step 1: Create `meta.txt`**

```
for 循环与 range()
更简洁的重复——按固定次数循环
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第6课：for 循环与 range()

## for 循环更简洁

上节课的 while 循环要自己管理计数变量，`for` + `range()` 帮你搞定：

```python demo title="for 循环数数"
for i in range(1, 6):
    print(i)
```

`range(1, 6)` 产生 1, 2, 3, 4, 5（不包含6）。

## range() 三种写法

```python demo title="range() 用法"
# range(stop)：从 0 开始
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop)
for i in range(1, 6):
    print(i, end=" ")
print()

# range(start, stop, step)：步长
for i in range(0, 11, 2):
    print(i, end=" ")
print()
```

## 嵌套循环：九九乘法表

```python demo title="九九乘法表（部分）"
for i in range(1, 4):      # 只打印前3行试试
    for j in range(1, 10):
        print(i, "×", j, "=", i*j, "\t", end="")
    print()
```

## 遍历字符串

```python demo title="逐字打印"
name = "Anan"
for char in name:
    print(char)
```

## 练习

```python exercise title="打印星星三角形"
# 目标：
# *
# **
# ***
# ****
# *****

rows = 5
for i in range(1, rows + 1):
    print("*" * i)
```
````

- [ ] **Step 3: Create `exercises/06_for.py`**

```python
# 第6课练习：for 循环

# 练习1：星星三角形
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

# 练习2：打印你名字的每个字母
name = input("输入你的名字（英文）：")
for char in name:
    print(char)

# 挑战：打印九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}×{j}={i*j}", end="\t")
    print()
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/06-for/
git commit -m "content: lesson 06 - for loops"
```

---

### Task 14: 项目一 — 猜数字游戏

**Files:**
- Create: `content/07-p1-guess-game/meta.txt`
- Create: `content/07-p1-guess-game/lesson.md`
- Create: `content/07-p1-guess-game/exercises/guess_game.py`

- [ ] **Step 1: Create `meta.txt`**

```
🎮 项目一：猜数字游戏
综合运用 if、while、random 写出你的第一个完整游戏！
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 🎮 项目一：猜数字游戏

恭喜完成阶段二！现在把 `if`、`while`、`random` 结合起来写一个完整游戏。

## 游戏规则

1. 电脑随机选一个 1-100 的数
2. 玩家不断猜
3. 每次猜完，电脑提示"大了"或"小了"
4. 猜对了，显示猜了几次

## 先试试浏览器演示版（1-20，更容易猜）

```python demo title="猜数字游戏（演示版，范围1-20）"
import random

secret = random.randint(1, 20)
attempts = 0
guess = 0

print("我想了一个 1 到 20 之间的数！")

while guess != secret:
    guess = int(input("你猜："))
    attempts += 1
    if guess < secret:
        print("小了！再试试 ↑")
    elif guess > secret:
        print("大了！再试试 ↓")

print("🎉 猜对了！你猜了", attempts, "次！")
```

## 在 Thonny 里跑完整版

```python exercise title="猜数字游戏（完整版，在 Thonny 运行）"
import random

secret = random.randint(1, 100)
attempts = 0
guess = 0

print("=" * 30)
print("欢迎玩猜数字游戏！")
print("我想了 1 到 100 之间的一个数")
print("=" * 30)

while guess != secret:
    guess = int(input("你猜（1-100）："))
    attempts += 1
    if guess < secret:
        print("小了！↑")
    elif guess > secret:
        print("大了！↓")

print()
print("🎉 猜对了！答案是", secret)
print("你猜了", attempts, "次")
if attempts <= 7:
    print("你真棒，猜的次数很少！🌟")
else:
    print("继续练习，下次会更快！💪")
```

## 挑战

- 加一个最多猜10次的限制，超过就输了
- 游戏结束后问"要再玩一局吗？"
````

- [ ] **Step 3: Create `exercises/guess_game.py`**

```python
# 项目一：猜数字游戏
# 在 Thonny 里运行！

import random

secret = random.randint(1, 100)
attempts = 0
guess = 0

print("=" * 30)
print("欢迎玩猜数字游戏！")
print("我想了 1 到 100 之间的一个数")
print("=" * 30)

while guess != secret:
    guess = int(input("你猜（1-100）："))
    attempts += 1
    if guess < secret:
        print("小了！↑")
    elif guess > secret:
        print("大了！↓")

print("🎉 猜对了！答案是", secret)
print("你猜了", attempts, "次")
if attempts <= 7:
    print("你真棒！🌟")
else:
    print("继续练习！💪")
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/07-p1-guess-game/
git commit -m "content: project 1 - guess the number game"
```

---

### Task 15: Lesson 08 — 列表

**Files:**
- Create: `content/08-lists/meta.txt`
- Create: `content/08-lists/lesson.md`
- Create: `content/08-lists/exercises/08_lists.py`

- [ ] **Step 1: Create `meta.txt`**

```
列表（list）
把多个值放在一起，像一排抽屉
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第8课：列表（list）

## 一个变量存多个值

之前每个变量只能存一个值。**列表**可以存很多个：

```python demo title="创建列表"
fruits = ["苹果", "香蕉", "草莓", "西瓜"]
print(fruits)
print(fruits[0])    # 第1个，下标从0开始
print(fruits[2])    # 第3个
print(len(fruits))  # 列表长度
```

> **注意：** 下标从 **0** 开始！第1个是 `[0]`，第2个是 `[1]`。

## 常用操作

```python demo title="列表操作"
scores = [85, 92, 78, 96, 88]

scores.append(100)        # 在末尾添加
print(scores)

scores.sort()             # 排序（从小到大）
print(scores)

print(max(scores))        # 最大值
print(min(scores))        # 最小值
print(sum(scores))        # 求和
```

## 用 for 遍历列表

```python demo title="遍历列表"
animals = ["🐶 狗", "🐱 猫", "🐰 兔", "🐼 熊猫"]
for animal in animals:
    print("我喜欢", animal)
```

## 练习

```python exercise title="我的购物清单"
shopping = ["苹果", "牛奶", "面包"]

# 1. 打印清单里的第一个和最后一个
print("第一个：", shopping[0])
print("最后一个：", shopping[-1])   # -1 表示最后一个

# 2. 添加"鸡蛋"到清单
shopping.append("鸡蛋")

# 3. 打印完整清单
print("完整清单：")
for item in shopping:
    print("-", item)
```
````

- [ ] **Step 3: Create `exercises/08_lists.py`**

```python
# 第8课练习：列表

# 创建一个存放你喜欢的5种食物的列表
foods = ["___", "___", "___", "___", "___"]

print("我喜欢的食物：")
for food in foods:
    print("-", food)

print("共", len(foods), "种")
print("第一种：", foods[0])
print("最后一种：", foods[-1])

# 再加一种
foods.append("___")
print("加了一种后：", foods)
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/08-lists/
git commit -m "content: lesson 08 - lists"
```

---

### Task 16: Lesson 09 — 函数

**Files:**
- Create: `content/09-functions/meta.txt`
- Create: `content/09-functions/lesson.md`
- Create: `content/09-functions/exercises/09_functions.py`

- [ ] **Step 1: Create `meta.txt`**

```
函数（def）
给代码起名字，需要时直接调用——避免重复写
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第9课：函数（def）

## 为什么需要函数？

如果你要在程序里好几处打印欢迎语，不用每次都写一遍：

```python demo title="定义并调用函数"
def greet(name):
    print("你好，" + name + "！欢迎来学 Python！")

greet("Anan")
greet("小明")
greet("小红")
```

函数用 `def` 定义，括号里是**参数**（接收外部传入的值）。

## 有返回值的函数

```python demo title="计算面积"
def area(length, width):
    result = length * width
    return result

room = area(4, 5)
print("房间面积：", room, "平方米")
print("桌子面积：", area(1.2, 0.6), "平方米")
```

`return` 把计算结果"返回"给调用者。

## 函数让代码更清晰

```python demo title="判断成绩等级（用函数）"
def grade(score):
    if score >= 90:
        return "优秀 🌟"
    elif score >= 80:
        return "良好 👍"
    elif score >= 60:
        return "及格 📚"
    else:
        return "加油 💪"

for s in [95, 82, 67, 45]:
    print(s, "分 →", grade(s))
```

## 练习

```python exercise title="温度转换函数"
def celsius_to_fahrenheit(c):
    # 公式：°F = °C × 1.8 + 32
    f = c * 1.8 + 32
    return f

print(celsius_to_fahrenheit(0))    # 应该输出 32.0
print(celsius_to_fahrenheit(100))  # 应该输出 212.0
print(celsius_to_fahrenheit(37))   # 体温
```
````

- [ ] **Step 3: Create `exercises/09_functions.py`**

```python
# 第9课练习：函数

def celsius_to_fahrenheit(c):
    return c * 1.8 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8

# 测试
print("0°C =", celsius_to_fahrenheit(0), "°F")
print("100°C =", celsius_to_fahrenheit(100), "°F")
print("98.6°F =", round(fahrenheit_to_celsius(98.6), 1), "°C")

# 挑战：写一个函数，判断一个数是不是质数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for num in range(2, 20):
    if is_prime(num):
        print(num, "是质数")
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/09-functions/
git commit -m "content: lesson 09 - functions"
```

---

### Task 17: Lesson 10 — 字符串操作

**Files:**
- Create: `content/10-strings/meta.txt`
- Create: `content/10-strings/lesson.md`
- Create: `content/10-strings/exercises/10_strings.py`

- [ ] **Step 1: Create `meta.txt`**

```
字符串操作
文字也能玩花样——切割、查找、替换
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第10课：字符串操作

## 字符串是字符的列表

字符串里的每个字符都有下标，可以用 `[]` 取出：

```python demo title="访问字符"
name = "Anan"
print(name[0])       # 'A'
print(name[-1])      # 'n'（最后一个）
print(name[1:3])     # 'na'（切片）
print(len(name))     # 4
```

## 常用字符串方法

```python demo title="字符串方法"
s = "  Hello, Python!  "

print(s.upper())          # 全大写
print(s.lower())          # 全小写
print(s.strip())          # 去掉两端空格
print(s.replace("Python", "Anan"))  # 替换
print(s.count("l"))       # 统计'l'出现次数
print("Hello" in s)       # 检查是否包含
```

## f-string：更方便的格式化

```python demo title="f-string 格式化"
name = "Anan"
age = 9
score = 95.5

print(f"我叫{name}，今年{age}岁，得了{score}分")
print(f"明年我{age + 1}岁")
```

## 练习

```python exercise title="文字小游戏"
word = "Python"

# 1. 倒着打印
print(word[::-1])

# 2. 统计元音字母数量
vowels = "aeiouAEIOU"
count = 0
for char in word:
    if char in vowels:
        count += 1
print(f"'{word}' 里有 {count} 个元音字母")

# 3. 判断回文
test = "racecar"
if test == test[::-1]:
    print(f"'{test}' 是回文！")
else:
    print(f"'{test}' 不是回文")
```
````

- [ ] **Step 3: Create `exercises/10_strings.py`**

```python
# 第10课练习：字符串操作

name = input("输入你的名字（英文）：")

print(f"正着：{name}")
print(f"倒着：{name[::-1]}")
print(f"大写：{name.upper()}")
print(f"长度：{len(name)} 个字母")

# 统计元音
vowels = "aeiouAEIOU"
vowel_count = sum(1 for c in name if c in vowels)
print(f"元音字母数：{vowel_count}")

# 回文判断
if name.lower() == name.lower()[::-1]:
    print(f"哇！'{name}' 是回文名字！")
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/10-strings/
git commit -m "content: lesson 10 - string operations"
```

---

### Task 18: Lesson 11 — 模块与 import

**Files:**
- Create: `content/11-modules/meta.txt`
- Create: `content/11-modules/lesson.md`
- Create: `content/11-modules/exercises/11_modules.py`

- [ ] **Step 1: Create `meta.txt`**

```
模块与 import
使用 Python 自带的工具箱——random、math 等
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第11课：模块与 import

## 什么是模块？

Python 自带了很多"工具箱"（模块），用 `import` 打开就能用里面的工具。

## random 模块

```python demo title="random 模块"
import random

print(random.randint(1, 10))       # 1到10的随机整数
print(random.random())             # 0到1之间的随机小数

fruits = ["苹果", "香蕉", "草莓", "西瓜"]
print(random.choice(fruits))       # 随机选一个

random.shuffle(fruits)             # 随机打乱顺序
print(fruits)
```

## math 模块

```python demo title="math 模块"
import math

print(math.pi)              # 圆周率 π
print(math.sqrt(16))        # 开平方根
print(math.ceil(3.2))       # 向上取整 → 4
print(math.floor(3.8))      # 向下取整 → 3
print(math.pow(2, 10))      # 2的10次方
```

## 随机出题小程序

```python demo title="随机加法出题"
import random

num1 = random.randint(1, 20)
num2 = random.randint(1, 20)
answer = int(input(f"{num1} + {num2} = ？"))

if answer == num1 + num2:
    print("✅ 答对了！")
else:
    print(f"❌ 答错了，正确答案是 {num1 + num2}")
```

## 练习

```python exercise title="用 random 做一道乘法题"
import random

a = random.randint(2, 9)
b = random.randint(2, 9)
answer = int(input(f"{a} × {b} = ？"))

if answer == a * b:
    print("🎉 答对了！太棒了！")
else:
    print(f"再想想，{a} × {b} = {a * b}")
```
````

- [ ] **Step 3: Create `exercises/11_modules.py`**

```python
# 第11课练习：模块

import random
import math

# 练习1：随机乘法出题（连续5题）
print("=== 数学小测验 ===")
correct = 0
for i in range(5):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    answer = int(input(f"第{i+1}题：{a} × {b} = ？"))
    if answer == a * b:
        print("✅ 答对了！")
        correct += 1
    else:
        print(f"❌ 正确答案是 {a * b}")

print(f"\n5题答对了 {correct} 题！")

# 练习2：计算圆的面积
r = float(input("输入圆的半径："))
area = math.pi * r * r
print(f"面积 = {area:.2f}")   # :.2f 表示保留2位小数
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/11-modules/
git commit -m "content: lesson 11 - modules and import"
```

---

### Task 19: 项目二 — turtle 绘图

**Files:**
- Create: `content/12-p2-turtle/meta.txt`
- Create: `content/12-p2-turtle/lesson.md`
- Create: `content/12-p2-turtle/exercises/turtle_art.py`

- [ ] **Step 1: Create `meta.txt`**

```
🎨 项目二：turtle 绘图
用代码画出你自己的图案！
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 🎨 项目二：turtle 绘图

`turtle` 模块让你控制一只"小乌龟"在屏幕上画画——它走过的路就是画出的线。

> **注意：** `turtle` 需要在 Thonny 里运行（需要窗口），不能在网页里演示。把下面的代码下载到 Thonny！

## 基本命令

| 命令 | 说明 |
|------|------|
| `forward(n)` | 向前走 n 步 |
| `backward(n)` | 向后走 n 步 |
| `right(角度)` | 向右转 |
| `left(角度)` | 向左转 |
| `penup()` | 抬起画笔（移动不画线） |
| `pendown()` | 放下画笔 |
| `color("red")` | 设置颜色 |
| `speed(1~10)` | 设置速度 |

## 画一个正方形

```python exercise title="正方形（在 Thonny 运行）"
import turtle

t = turtle.Turtle()
t.speed(5)
t.color("blue")

for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

## 画一朵花

```python exercise title="旋转花朵（在 Thonny 运行）"
import turtle

t = turtle.Turtle()
t.speed(10)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(36):
    t.color(colors[i % len(colors)])
    t.forward(100)
    t.right(170)

turtle.done()
```

## 你的任务

选一个（或自己设计！）：
1. 用 `turtle` 画出你名字的首字母
2. 画一个五角星 ⭐（提示：每次转 144 度，画5次）
3. 画一栋小房子（正方形 + 三角形屋顶）
````

- [ ] **Step 3: Create `exercises/turtle_art.py`**

```python
# 项目二：turtle 绘图
# 在 Thonny 里运行！

import turtle

t = turtle.Turtle()
t.speed(8)

# 画五角星
t.color("gold")
t.begin_fill()
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

# 在星星旁边写名字
t.penup()
t.goto(-60, -180)
t.pendown()
t.color("purple")
t.write("Anan ⭐", font=("Arial", 24, "bold"))

turtle.done()
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/12-p2-turtle/
git commit -m "content: project 2 - turtle drawing"
```

---

### Task 20: Lesson 13 — 字典

**Files:**
- Create: `content/13-dicts/meta.txt`
- Create: `content/13-dicts/lesson.md`
- Create: `content/13-dicts/exercises/13_dicts.py`

- [ ] **Step 1: Create `meta.txt`**

```
字典（dict）
用名字查找数据，而不是用数字下标
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第13课：字典（dict）

## 用名字而不是数字查数据

列表用数字下标：`fruits[0]`。字典用**键**（名字）查找**值**：

```python demo title="创建字典"
student = {
    "name": "Anan",
    "age": 9,
    "grade": "三年级",
    "hobby": "画画"
}

print(student["name"])
print(student["age"])
print(student["hobby"])
```

## 增加、修改、删除

```python demo title="修改字典"
scores = {"语文": 95, "数学": 88, "英语": 92}

scores["科学"] = 90        # 添加新键值对
scores["数学"] = 96        # 修改已有的值
del scores["英语"]         # 删除

print(scores)
print("科目数量：", len(scores))
```

## 遍历字典

```python demo title="遍历字典"
scores = {"语文": 95, "数学": 88, "科学": 90}

for subject, score in scores.items():
    print(f"{subject}：{score} 分")
```

## 练习

```python exercise title="单词本"
vocab = {
    "apple": "苹果",
    "cat": "猫",
    "book": "书"
}

# 查找单词
word = "apple"
if word in vocab:
    print(f"{word} 的中文是：{vocab[word]}")

# 添加新单词
vocab["dog"] = "狗"
vocab["pen"] = "钢笔"

print("单词本里共有", len(vocab), "个单词")
for eng, chn in vocab.items():
    print(f"  {eng} = {chn}")
```
````

- [ ] **Step 3: Create `exercises/13_dicts.py`**

```python
# 第13课练习：字典

# 建立一个关于你自己的字典
me = {
    "name": "___",
    "age": 0,
    "hobby": "___",
    "favorite_food": "___",
    "best_subject": "___"
}

print("=== 关于我 ===")
for key, value in me.items():
    print(f"{key}: {value}")

# 简单的单词测试
vocab = {"sun": "太阳", "moon": "月亮", "star": "星星", "cloud": "云"}

print("\n=== 英语小测验 ===")
for word, meaning in vocab.items():
    answer = input(f"'{word}' 是什么意思？")
    if answer.strip() == meaning:
        print("✅ 正确！")
    else:
        print(f"❌ 正确答案是：{meaning}")
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/13-dicts/
git commit -m "content: lesson 13 - dictionaries"
```

---

### Task 21: Lesson 14 — 文件读写

**Files:**
- Create: `content/14-files/meta.txt`
- Create: `content/14-files/lesson.md`
- Create: `content/14-files/exercises/14_files.py`

- [ ] **Step 1: Create `meta.txt`**

```
文件读写
让程序记住事情——把数据保存到文件里
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第14课：文件读写

之前程序关闭后，所有数据都消失了。用文件可以把数据**永久保存**。

> **注意：** 文件操作在 Thonny 里运行，会在你的电脑上真正创建文件。

## 写入文件

```python exercise title="写日记（在 Thonny 运行）"
# 'w' 模式：写入（会覆盖原有内容）
with open("diary.txt", "w", encoding="utf-8") as f:
    f.write("今天学了文件读写！\n")
    f.write("Python 越来越好玩了。\n")

print("日记已保存！")
```

## 读取文件

```python exercise title="读日记（在 Thonny 运行）"
with open("diary.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("日记内容：")
print(content)
```

## 追加内容

```python exercise title="追加日记（在 Thonny 运行）"
# 'a' 模式：追加（在末尾添加，不覆盖）
with open("diary.txt", "a", encoding="utf-8") as f:
    new_line = input("今天还想写什么？")
    f.write(new_line + "\n")

print("追加成功！")
```

## 文件模式总结

| 模式 | 说明 |
|------|------|
| `"r"` | 读取（文件必须存在） |
| `"w"` | 写入（覆盖原内容） |
| `"a"` | 追加（在末尾添加） |
````

- [ ] **Step 3: Create `exercises/14_files.py`**

```python
# 第14课练习：文件读写
# 在 Thonny 里运行

# 1. 写入一个购物清单
items = []
print("输入购物清单（输入 q 结束）：")
while True:
    item = input("- ")
    if item.lower() == "q":
        break
    items.append(item)

with open("shopping.txt", "w", encoding="utf-8") as f:
    for item in items:
        f.write(item + "\n")
print("购物清单已保存到 shopping.txt！")

# 2. 读取并显示
print("\n购物清单内容：")
with open("shopping.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("✓", line.strip())
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/14-files/
git commit -m "content: lesson 14 - file read and write"
```

---

### Task 22: Lesson 15 — 错误处理

**Files:**
- Create: `content/15-errors/meta.txt`
- Create: `content/15-errors/lesson.md`
- Create: `content/15-errors/exercises/15_errors.py`

- [ ] **Step 1: Create `meta.txt`**

```
错误处理：try / except
让程序更聪明——出错时优雅地处理，而不是崩溃
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第15课：错误处理：try / except

## 程序出错时

如果用户输入了不是数字的内容，`int()` 会报错，程序崩溃：

```python demo title="会崩溃的程序"
age = int(input("输入年龄："))   # 如果输入 "abc" 就会崩溃
print("你", age, "岁")
```

## try / except 救场

```python demo title="优雅处理错误"
try:
    age = int(input("输入年龄："))
    print("你", age, "岁")
except ValueError:
    print("❌ 请输入数字！")
```

`try` 里放可能出错的代码，`except` 里放出错后的处理。

## 常见错误类型

| 错误 | 原因 |
|------|------|
| `ValueError` | 类型转换失败（如 `int("abc")`） |
| `FileNotFoundError` | 文件不存在 |
| `IndexError` | 列表下标超出范围 |
| `KeyError` | 字典中找不到键 |
| `ZeroDivisionError` | 除以零 |

```python demo title="处理多种错误"
numbers = [10, 20, 30]

try:
    index = int(input("输入下标（0-2）："))
    result = 100 / numbers[index]
    print("结果：", result)
except ValueError:
    print("❌ 请输入整数")
except IndexError:
    print("❌ 下标超出范围（只有0、1、2）")
except ZeroDivisionError:
    print("❌ 不能除以零")
```

## 练习

```python exercise title="安全的输入函数"
def safe_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ 请输入整数，重试：")

age = safe_int_input("输入你的年龄：")
print("你", age, "岁")
```
````

- [ ] **Step 3: Create `exercises/15_errors.py`**

```python
# 第15课练习：错误处理

def safe_int_input(prompt):
    """一直问直到用户输入合法整数"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ 请输入整数，重试：")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "❌ 不能除以零"

# 测试
a = safe_int_input("输入被除数：")
b = safe_int_input("输入除数：")
print(f"{a} ÷ {b} = {safe_divide(a, b)}")
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/15-errors/
git commit -m "content: lesson 15 - error handling"
```

---

### Task 23: Lesson 16 — 算法思维

**Files:**
- Create: `content/16-algorithms/meta.txt`
- Create: `content/16-algorithms/lesson.md`
- Create: `content/16-algorithms/exercises/16_algorithms.py`

- [ ] **Step 1: Create `meta.txt`**

```
算法思维：排序与查找
聪明地解决问题——计算机科学家的思考方式
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 第16课：算法思维：排序与查找

## 什么是算法？

**算法**就是解决问题的步骤清单。就像做蛋炒饭的菜谱，一步一步来。

## 线性查找

在列表里找一个数——从头开始一个个看：

```python demo title="线性查找"
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i    # 找到了，返回下标
    return -1           # 没找到

numbers = [3, 7, 1, 9, 4, 6, 2, 8, 5]
result = linear_search(numbers, 9)
print(f"找到 9，在第 {result} 个位置（下标从0开始）")
print(f"查找了 {numbers.index(9) + 1} 次")
```

## 冒泡排序

像泡泡从水底浮上来一样，大的数逐渐"浮"到后面：

```python demo title="冒泡排序（带步骤展示）"
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

data = [5, 3, 8, 1, 9, 2, 7, 4, 6]
print("排序前：", data)
sorted_data = bubble_sort(data.copy())
print("排序后：", sorted_data)
```

## Python 内置排序（更厉害的算法）

```python demo title="Python 内置 sort"
data = [5, 3, 8, 1, 9, 2]
data.sort()
print("从小到大：", data)
data.sort(reverse=True)
print("从大到小：", data)
```

## 算法的效率

查找10个数：最多看10次。查找100个数：最多看100次。这叫 **O(n)**。

好的算法能大大减少步骤。这就是为什么程序员要学算法！

## 练习

```python exercise title="找最大值（不用 max()）"
def my_max(lst):
    biggest = lst[0]
    for num in lst:
        if num > biggest:
            biggest = num
    return biggest

numbers = [3, 7, 1, 9, 4, 6, 2]
print("最大值：", my_max(numbers))
print("验证：", max(numbers))
```
````

- [ ] **Step 3: Create `exercises/16_algorithms.py`**

```python
# 第16课练习：算法思维

# 练习1：自己实现 min()
def my_min(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

# 练习2：统计列表中某个值出现的次数
def count_occurrences(lst, target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count

# 测试
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("列表：", data)
print("最小值：", my_min(data))
print("5 出现了", count_occurrences(data, 5), "次")

# Python 排序 vs 自己的冒泡排序
import time

big_list = list(range(1000, 0, -1))  # 1000到1倒序

start = time.time()
sorted(big_list)
print(f"Python 内置排序用时：{time.time()-start:.6f} 秒")
```

- [ ] **Step 4: Build and commit**

```bash
python build.py
git add content/16-algorithms/
git commit -m "content: lesson 16 - algorithm thinking"
```

---

### Task 24: 项目三 — 自选综合项目

**Files:**
- Create: `content/17-p3-final/meta.txt`
- Create: `content/17-p3-final/lesson.md`
- Create: `content/17-p3-final/exercises/p3_quiz.py`
- Create: `content/17-p3-final/exercises/p3_diary.py`
- Create: `content/17-p3-final/exercises/p3_calculator.py`

- [ ] **Step 1: Create `meta.txt`**

```
🛠️ 项目三：自选综合项目
选一个你最感兴趣的，用学过的所有知识完成它！
```

- [ ] **Step 2: Create `lesson.md`**

````markdown
# 🛠️ 项目三：自选综合项目

恭喜！你已经学完了所有课程！现在选一个你最感兴趣的项目来完成。

---

## 选项 A：知识小测验系统

出10道题，自动判分，支持任意科目：

```python exercise title="选项 A：知识小测验（在 Thonny 运行）"
# 在 p3_quiz.py 里完成完整版
import random

questions = [
    ("Python 用什么命令打印输出？", "print"),
    ("列表的第一个元素下标是多少？", "0"),
    ("定义函数用什么关键字？", "def"),
    ("循环用什么关键字？", "for"),
    ("True 和 False 是什么数据类型？", "bool"),
]

random.shuffle(questions)
score = 0

print("=== Python 知识小测验 ===\n")
for i, (question, answer) in enumerate(questions, 1):
    user = input(f"第{i}题：{question} ").strip().lower()
    if user == answer.lower():
        print("✅ 正确！")
        score += 1
    else:
        print(f"❌ 正确答案是：{answer}")
    print()

print(f"你答对了 {score}/{len(questions)} 题！")
```

---

## 选项 B：个人日记本

可以写日记、查看历史、搜索关键词：

```python exercise title="选项 B：日记本（在 Thonny 运行）"
# 在 p3_diary.py 里完成完整版
# 功能：1-写日记 2-查看所有 3-搜索 4-退出
import datetime

DIARY_FILE = "my_diary.txt"

def write_entry():
    date = datetime.date.today()
    content = input("今天想写什么？\n> ")
    with open(DIARY_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n【{date}】\n{content}\n")
    print("✅ 日记已保存！")

def read_all():
    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("还没有日记，快去写第一篇！")

while True:
    print("\n1. 写日记  2. 查看所有  3. 退出")
    choice = input("选择：")
    if choice == "1": write_entry()
    elif choice == "2": read_all()
    elif choice == "3": break
```

---

## 选项 C：智能计算器

支持加减乘除，有历史记录，能处理错误输入：

```python exercise title="选项 C：计算器（在 Thonny 运行）"
# 在 p3_calculator.py 里完成完整版
history = []

def calculate(expression):
    try:
        result = eval(expression)   # eval 可以计算字符串里的数学表达式
        history.append(f"{expression} = {result}")
        return result
    except ZeroDivisionError:
        return "❌ 不能除以零"
    except Exception:
        return "❌ 无效的表达式"

print("=== 智能计算器 ===")
print("输入数学表达式（如 3 + 4 * 2），输入 q 退出，输入 h 查看历史")

while True:
    expr = input("\n计算：").strip()
    if expr.lower() == "q":
        break
    elif expr.lower() == "h":
        print("计算历史：")
        for item in history:
            print(" ", item)
    else:
        print("=", calculate(expr))
```
````

- [ ] **Step 3: Create exercise files**

`exercises/p3_quiz.py`:
```python
# 项目三：知识小测验系统
# 在这里完成你的完整版——加更多题目，加计时，加难度等级！
import random

questions = [
    ("Python 用什么命令打印输出？", "print"),
    ("列表的第一个元素下标是多少？", "0"),
    ("定义函数用什么关键字？", "def"),
    ("True 和 False 是什么类型？", "bool"),
    ("模块导入用什么关键字？", "import"),
]

random.shuffle(questions)
score = 0
print("=== Python 知识小测验 ===\n")
for i, (q, a) in enumerate(questions, 1):
    ans = input(f"第{i}题：{q} ").strip().lower()
    if ans == a.lower():
        print("✅ 正确！")
        score += 1
    else:
        print(f"❌ 正确答案：{a}")
print(f"\n最终得分：{score}/{len(questions)}")
```

`exercises/p3_diary.py`:
```python
# 项目三：个人日记本
import datetime

FILE = "my_diary.txt"

def write():
    date = datetime.date.today()
    content = input("今天想写什么？\n> ")
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(f"\n【{date}】\n{content}\n")
    print("✅ 已保存！")

def read_all():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("还没有日记！")

while True:
    print("\n1-写日记  2-查看  3-退出")
    c = input("选择：")
    if c == "1": write()
    elif c == "2": read_all()
    elif c == "3": break
```

`exercises/p3_calculator.py`:
```python
# 项目三：智能计算器
history = []

def calculate(expr):
    try:
        result = eval(expr)
        history.append(f"{expr} = {result}")
        return result
    except ZeroDivisionError:
        return "❌ 不能除以零"
    except Exception:
        return "❌ 无效表达式"

print("=== 智能计算器 === （q退出，h历史）")
while True:
    expr = input("计算：").strip()
    if expr == "q": break
    elif expr == "h":
        for item in history: print(" ", item)
    else:
        print("=", calculate(expr))
```

- [ ] **Step 4: Final build — verify all 17 lessons appear**

```bash
python build.py
```

Expected: `Built 17 lessons → dist/`

Open `dist/index.html` — should show 17 lesson cards across 4 stages.

- [ ] **Step 5: Final commit**

```bash
git add content/17-p3-final/
git commit -m "content: project 3 - final self-selected project"
```

---

## Phase 3: Deployment

### Task 25: Deploy to Cloudflare Pages

- [ ] **Step 1: Push repo to GitHub**

```bash
git remote add origin https://github.com/<your-username>/CodingForAnan.git
git push -u origin main
```

- [ ] **Step 2: Create Cloudflare Pages project**

1. Go to Cloudflare Dashboard → Pages → Create a project
2. Connect to your GitHub repo `CodingForAnan`
3. Build settings:
   - **Build command:** `pip install -r requirements.txt && python build.py`
   - **Build output directory:** `dist`
   - **Root directory:** `/` (leave blank)
4. Deploy!

- [ ] **Step 3: Verify deployment**

Visit your Cloudflare Pages URL (e.g., `https://coding-for-anan.pages.dev`).

Expected: Course home page loads, navigation works, lesson pages load, Pyodide runs Python code.

---

## Self-Review Checklist

After writing this plan, checked against the spec:

- **Spec §2 Architecture:** ✅ build.py, Jinja2, Pyodide, CodeMirror, CDN, Cloudflare Pages — all covered.
- **Spec §3 Course Outline:** ✅ All 14 lessons + 3 projects with correct ordering (01-17).
- **Spec §4 Code Blocks:** ✅ Demo blocks (run-btn only), Exercise blocks (run-btn + download-btn), Pyodide loading strategy, `input()` shim.
- **Spec §5 Page Design:** ✅ Index with localStorage progress, lesson layout (dual-column), sticky cheatsheet, prev/next nav, complete button, celebration animation.
- **Spec §6 Content Format:** ✅ ` ```python demo title="..." ` and ` ```python exercise title="..." ` syntax, build.py parses and renders both.
- **Type consistency:** `render_lesson(md_text, lesson_num, title, prev, next_lesson)` defined in Task 3 and used consistently in tests (Task 2). Template variable `next` in Jinja2 matches `next_lesson` passed via `render()`.
- **No placeholders:** All code blocks contain complete, runnable Python/HTML/CSS/JS. No TBD/TODO found.
