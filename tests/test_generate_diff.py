from gendiff.generate_diff import generate_diff


CORRECT_ANSWER = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_generate_diff_json():
    filepath1 = 'tests/fixtures/file1.json'
    filepath2 = 'tests/fixtures/file2.json'
    assert generate_diff(filepath1, filepath2) == CORRECT_ANSWER


def test_generate_diff_yml():
    filepath1 = 'tests/fixtures/file1.yml'
    filepath2 = 'tests/fixtures/file2.yml'
    assert generate_diff(filepath1, filepath2) == CORRECT_ANSWER
