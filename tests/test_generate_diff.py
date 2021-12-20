from gendiff.gendiff import generate_diff
from gendiff.formatters.formats import JSON, STYLISH, PLAIN
from tests.fixtures.correct_answers import FILE_STYLISH
from tests.fixtures.correct_answers import RECURSIVE_FILE_STYLISH
from tests.fixtures.correct_answers import FILE_PLAIN
from tests.fixtures.correct_answers import RECURSIVE_FILE_PLAIN
from tests.fixtures.correct_answers import FILE_JSON
from tests.fixtures.correct_answers import RECURSIVE_FILE_JSON
import typing


def test_gendif_type():
    assert isinstance(generate_diff, typing.Callable)


def test_generate_diff_stylish():
    filepath1 = 'tests/fixtures/file1.yml'
    filepath2 = 'tests/fixtures/file2.yml'
    filepath3 = 'tests/fixtures/file1.yaml'
    filepath4 = 'tests/fixtures/file2.yaml'
    filepath5 = 'tests/fixtures/file1.json'
    filepath6 = 'tests/fixtures/file2.json'
    assert generate_diff(filepath1, filepath2, STYLISH) == FILE_STYLISH
    assert generate_diff(filepath3, filepath4, STYLISH) == FILE_STYLISH
    assert generate_diff(filepath5, filepath6, STYLISH) == FILE_STYLISH


def test_generate_diff_recursive_stylish():
    filepath1 = 'tests/fixtures/file1_recursive.json'
    filepath2 = 'tests/fixtures/file2_recursive.json'
    filepath3 = 'tests/fixtures/file1_recursive.yaml'
    filepath4 = 'tests/fixtures/file2_recursive.yaml'
    assert generate_diff(filepath1, filepath2, STYLISH) == RECURSIVE_FILE_STYLISH
    assert generate_diff(filepath3, filepath4, STYLISH) == RECURSIVE_FILE_STYLISH


def test_generate_diff_plain():
    filepath1 = 'tests/fixtures/file1.yml'
    filepath2 = 'tests/fixtures/file2.yml'
    filepath3 = 'tests/fixtures/file1.yaml'
    filepath4 = 'tests/fixtures/file2.yaml'
    filepath5 = 'tests/fixtures/file1.json'
    filepath6 = 'tests/fixtures/file2.json'
    assert generate_diff(filepath1, filepath2, PLAIN) == FILE_PLAIN
    assert generate_diff(filepath3, filepath4, PLAIN) == FILE_PLAIN
    assert generate_diff(filepath5, filepath6, PLAIN) == FILE_PLAIN


def test_generate_diff_recursive_plain():
    filepath1 = 'tests/fixtures/file1_recursive.json'
    filepath2 = 'tests/fixtures/file2_recursive.json'
    filepath3 = 'tests/fixtures/file1_recursive.yaml'
    filepath4 = 'tests/fixtures/file2_recursive.yaml'
    assert generate_diff(filepath1, filepath2, PLAIN) == RECURSIVE_FILE_PLAIN
    assert generate_diff(filepath3, filepath4, PLAIN) == RECURSIVE_FILE_PLAIN


def test_generate_diff_json():
    filepath1 = 'tests/fixtures/file1.yml'
    filepath2 = 'tests/fixtures/file2.yml'
    filepath3 = 'tests/fixtures/file1.yaml'
    filepath4 = 'tests/fixtures/file2.yaml'
    filepath5 = 'tests/fixtures/file1.json'
    filepath6 = 'tests/fixtures/file2.json'
    assert generate_diff(filepath1, filepath2, JSON) == FILE_JSON
    assert generate_diff(filepath3, filepath4, JSON) == FILE_JSON
    assert generate_diff(filepath5, filepath6, JSON) == FILE_JSON


def test_generate_diff_recursive_json():
    filepath1 = 'tests/fixtures/file1_recursive.json'
    filepath2 = 'tests/fixtures/file2_recursive.json'
    filepath3 = 'tests/fixtures/file1_recursive.yaml'
    filepath4 = 'tests/fixtures/file2_recursive.yaml'
    assert generate_diff(filepath1, filepath2, JSON) == RECURSIVE_FILE_JSON
    assert generate_diff(filepath3, filepath4, JSON) == RECURSIVE_FILE_JSON
