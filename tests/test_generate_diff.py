from gendiff.generate_diff import generate_diff


def test_generate_diff():
    filepath1 = 'tests/fixtures/file1.json'
    filepath2 = 'tests/fixtures/file2.json'
    correct_answer = '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'
    assert generate_diff(filepath1, filepath2) == correct_answer
