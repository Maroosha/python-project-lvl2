### Hexlet tests and linter status:
[![Actions Status](https://github.com/Maroosha/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Maroosha/python-project-lvl2/actions)
[![Actions Status](https://github.com/Maroosha/python-project-lvl1/workflows/run-linter/badge.svg)](https://github.com/Maroosha/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/Maroosha/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/Maroosha/python-project-lvl2/test_coverage)


<h3> Package description</h3>
Compare two .JSON and/or .YAML (.YLM) files: check updates in file contents, if any.


<h3> Output formats</h3>
Get data difference between two files in three available output formats:

1) stylish,

2) plain,

3) json.

<strong>STYLISH</strong>

Default format.

<code>gendiff path/to/file1 path/to/file2</code>

Data difference description keys:
|Key     |Meaning    
|--------|--------------------------------------------------|
|+       |key-value pair is present only in the second file |
|-       |key-value pair is present only in the first file  |
|space   |key-value pair is present in the both files       |

<strong>PLAIN</strong>

A plain descriptive format with only changed key-value pairs shown.

<code>gendiff -f plain path/to/file1 path/to/file2</code>

_Property "SomeProperty" was removed_

_Property "SomeProperty" was added with value: "SomeValue"_

_Property "SomeProperty" was updated. From Value1 to Value2_

If a value is a dictionary, it is displayed as "[complex value]".

<strong>JSON</strong>

A usual json format.

<code>gendiff -f json path/to/file1 path/to/file2</code>


<h3> Installation</h3>
<code>pip install git+https://github.com/Maroosha/python-project-lvl2.git</code>


<h3> Help and usage</h3>

<code>gendiff -h</code>

<code>gendiff --format path/to/file1 path/to/file2</code>


## Demo

### Compare two flat JSON and/or YAML files: stylish format
[![asciicast](https://asciinema.org/a/457543.svg)](https://asciinema.org/a/457543)

### Compare two nested JSON and/or YAML files: stylish format
[![asciicast](https://asciinema.org/a/457743.svg)](https://asciinema.org/a/457743)

### Compare two JSON and/or YAML files: plain format
[![asciicast](https://asciinema.org/a/457745.svg)](https://asciinema.org/a/457745)

### Compare two JSON and/or YAML files: json format
[![asciicast](https://asciinema.org/a/462330.svg)](https://asciinema.org/a/462330)
