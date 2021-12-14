from gendiff.generate_diff import generate_diff


CORRECT_ANSWER_PLAIN_FILE = '''{
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
}'''

CORRECT_ANSWER_RECURSIVE_FILE = '''{
      common: {
        + follow: false
          setting1: Value 1
        - setting2: 200
        - setting3: true
        + setting3: null
        + setting4: blah blah
        + setting5: {
              key5: value5
          }
          setting6: {
              doge: {
                - wow: 
                + wow: so much
              }
              key: value
            + ops: vops
          }
      }
      group1: {
        - baz: bas
        + baz: bars
          foo: bar
        - nest: {
              key: value
          }
        + nest: str
      }
    - group2: {
          abc: 12345
          deep: {
              id: 45
          }
      }
    + group3: {
          deep: {
              id: {
                  number: 45
              }
          }
          fee: 100500
      }
}'''


def test_generate_diff_json():
    filepath1 = 'tests/fixtures/file1.json'
    filepath2 = 'tests/fixtures/file2.json'
    assert generate_diff(filepath1, filepath2) == CORRECT_ANSWER_PLAIN_FILE


def test_generate_diff_yml():
    filepath1 = 'tests/fixtures/file1.yml'
    filepath2 = 'tests/fixtures/file2.yml'
    filepath3 = 'tests/fixtures/file1.yaml'
    filepath4 = 'tests/fixtures/file2.yaml'
    assert generate_diff(filepath1, filepath2) == CORRECT_ANSWER_PLAIN_FILE
    assert generate_diff(filepath3, filepath4) == CORRECT_ANSWER_PLAIN_FILE


def test_generate_diff_json_recursive():
    filepath1 = 'tests/fixtures/file1_recursive.json'
    filepath2 = 'tests/fixtures/file2_recursive.json'
    assert generate_diff(filepath1, filepath2) == CORRECT_ANSWER_RECURSIVE_FILE



def test_generate_diff_yaml_recursive():
    filepath1 = 'tests/fixtures/file1_recursive.yaml'
    filepath2 = 'tests/fixtures/file2_recursive.yaml'
    assert generate_diff(filepath1, filepath2) == CORRECT_ANSWER_RECURSIVE_FILE
