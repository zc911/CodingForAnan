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
