# ke2daira.py

A Python implementation of [ke2daira](https://github.com/ryuichiueda/ke2daira)

## Installation

```
$ pip install ke2daira
```

Requires Python 3.10 or newer.

## Usage

```py
from ke2daira import ke2dairanize

print(ke2dairanize("松平 健")) # "ケツダイラ マン"
```

## Development

Install dependencies with poetry: `poetry sync` \
Run the regular checks: `poetry poe check` \
Run the package build and smoke test: `poetry poe package-check` \
Format code: `poetry poe format` \
Lint and fix code: `poetry poe lint-fix`


## Difference from original ke2daira

`ke2daira.py` only supports switching the head of the first word and the one of the last word.

## License

Apache-2.0
