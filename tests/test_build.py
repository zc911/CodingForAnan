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
