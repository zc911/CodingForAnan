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
    await setupAsyncInput();
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

// ---- Async input() ----
async function setupAsyncInput() {
  // Expose JS input handler to Python
  window.handlePyodideInput = (promptText) => {
    return new Promise((resolve) => {
      const index = currentRunIndex;
      const container = document.getElementById('inputs-' + index);
      if (!container) { resolve(''); return; }
      container.innerHTML = '';

      if (promptText) {
        const promptEl = document.createElement('div');
        promptEl.className = 'input-prompt';
        promptEl.textContent = promptText;
        container.appendChild(promptEl);
      }

      const field = document.createElement('input');
      field.type = 'text';
      field.className = 'input-field';
      field.placeholder = '输入后按回车 ↵';
      field.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          const val = field.value;
          if (promptText) appendOutput(index, promptText + val);
          container.innerHTML = '';
          resolve(val);
        }
      });
      container.appendChild(field);
      field.focus();
    });
  };

  // Override builtins.input with async version
  await pyodide.runPythonAsync(`
import builtins
async def _input(prompt=''):
    return await __import__('js').window.handlePyodideInput(prompt or '')
builtins.input = _input
`);
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

// ---- Run ----
async function runCode(index) {
  if (!pyodide) return;
  const outputEl = document.getElementById('output-' + index);
  const inputContainer = document.getElementById('inputs-' + index);
  if (outputEl) outputEl.innerHTML = '';
  if (inputContainer) inputContainer.innerHTML = '';
  currentRunIndex = index;

  const cm = editors[index];
  const code = cm ? cm.getValue() : (document.getElementById('editor-' + index) || {}).value || '';

  // Auto-add await before input() calls so they become await points
  const hasInput = /\binput\s*\(/.test(code);
  let finalCode = code;
  if (hasInput) {
    finalCode = code.replace(/\binput\s*\(/g, 'await input(');
  }

  try {
    await pyodide.runPythonAsync(finalCode);
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
