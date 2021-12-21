from gendiff.gendiff import generate_diff
from gendiff.formatters.formats import JSON, STYLISH, PLAIN
import pytest
import typing


FLAT_JSON1 = 'tests/fixtures/file1.json'
FLAT_JSON2 = 'tests/fixtures/file2.json'
FLAT_YAML1 = 'tests/fixtures/file1.yaml'
FLAT_YAML2 = 'tests/fixtures/file2.yaml'
FLAT_YML1 = 'tests/fixtures/file1.yml'
FLAT_YML2 = 'tests/fixtures/file2.yml'
NESTED_JSON1 = 'tests/fixtures/file1_nested.json'
NESTED_JSON2 = 'tests/fixtures/file2_nested.json'
NESTED_YAML1 = 'tests/fixtures/file1_nested.yaml'
NESTED_YAML2 = 'tests/fixtures/file2_nested.yaml'
ANSWER_JSON_FLAT = 'tests/fixtures/answer_json_flat'
ANSWER_JSON_NESTED = 'tests/fixtures/answer_json_nested'
ANSWER_PLAIN_FLAT = 'tests/fixtures/answer_plain_flat'
ANSWER_PLAIN_NESTED = 'tests/fixtures/answer_plain_nested'
ANSWER_STYLISH_FLAT = 'tests/fixtures/answer_stylish_flat'
ANSWER_STYLISH_NESTED = 'tests/fixtures/answer_stylish_nested'


def test_gendif_type():
    assert isinstance(generate_diff, typing.Callable)


def get_correct_answer(path_to_answer):
    with open(path_to_answer) as file:
        answer = file.read()
    return answer


@pytest.mark.parametrize('file1, file2, format_name, answer', [
    (FLAT_JSON1, FLAT_JSON2, STYLISH, ANSWER_STYLISH_FLAT),
    (FLAT_YML1, FLAT_YML2, STYLISH, ANSWER_STYLISH_FLAT),
    (FLAT_YAML1, FLAT_YAML2, STYLISH, ANSWER_STYLISH_FLAT),
    (NESTED_JSON1, NESTED_JSON2, STYLISH, ANSWER_STYLISH_NESTED),
    (NESTED_YAML1, NESTED_YAML2, STYLISH, ANSWER_STYLISH_NESTED),
    (FLAT_JSON1, FLAT_JSON2, PLAIN, ANSWER_PLAIN_FLAT),
    (FLAT_YML1, FLAT_YML2, PLAIN, ANSWER_PLAIN_FLAT),
    (FLAT_YAML1, FLAT_YAML2, PLAIN, ANSWER_PLAIN_FLAT),
    (NESTED_JSON1, NESTED_JSON2, PLAIN, ANSWER_PLAIN_NESTED),
    (NESTED_YAML1, NESTED_YAML2, PLAIN, ANSWER_PLAIN_NESTED),
    (FLAT_JSON1, FLAT_JSON2, JSON, ANSWER_JSON_FLAT),
    (FLAT_YML1, FLAT_YML2, JSON, ANSWER_JSON_FLAT),
    (FLAT_YAML1, FLAT_YAML2, JSON, ANSWER_JSON_FLAT),
    (NESTED_JSON1, NESTED_JSON2, JSON, ANSWER_JSON_NESTED),
    (NESTED_YAML1, NESTED_YAML2, JSON, ANSWER_JSON_NESTED),
])
def test_generate_diff(file1, file2, format_name, answer):
    assert generate_diff(file1, file2, format_name) == get_correct_answer(answer)