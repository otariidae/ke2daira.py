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
Validate project metadata: `poetry check --strict` \
Run type check: `poetry run mypy --strict .` \
Run tests: `poetry run pytest` \
Format code: `poetry run ruff format .` \
Lint and fix code: `poetry run ruff check --fix .`


## Difference from original ke2daira

`ke2daira.py` only supports switching the head of the first word and the one of the last word.

## License

Apache-2.0
