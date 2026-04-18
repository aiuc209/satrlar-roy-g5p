import pytest

def sort_lines_by_word_count(lines):
    return sorted(lines, key=lambda line: len(line.split()))

def test_sort_lines_by_word_count():
    lines = ["hello world", "a", "hello world again", "two words"]
    expected = ["a", "two words", "hello world", "hello world again"]
    assert sort_lines_by_word_count(lines) == expected

def test_sort_lines_by_word_count_empty_list():
    lines = []
    expected = []
    assert sort_lines_by_word_count(lines) == expected

def test_sort_lines_by_word_count_single_element():
    lines = ["hello world"]
    expected = ["hello world"]
    assert sort_lines_by_word_count(lines) == expected

def test_sort_lines_by_word_count_duplicates():
    lines = ["hello world", "hello world", "a"]
    expected = ["a", "hello world", "hello world"]
    assert sort_lines_by_word_count(lines) == expected
