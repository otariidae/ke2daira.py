# ruff: noqa: S101
from importlib.metadata import version

import pytest

from ke2daira import __version__, ke2dairanize


def test_version() -> None:
    assert __version__ == version("ke2daira")


@pytest.mark.parametrize(
    ("src", "expected"),
    [
        ("松平 健", "ケツダイラ マン"),
        ("ポール マッカートニー", "マール ポッカートニー"),
        ("チェ ゲバラ", "ゲ チェバラ"),
        ("加藤 あい", "アトウ カイ"),
        ("ハリー ジェームズ ポッター", "ポリー ジェームズ ハッター"),
        ("源蔵", "ゲンゾウ"),
    ],
)
def test_ke2dairanize(src: str, expected: str) -> None:
    assert ke2dairanize(src) == expected


@pytest.mark.xfail(reason="快がココロヨと読まれてしまう")
def test_atou_kai() -> None:
    assert ke2dairanize("阿藤 快") == "カトウ アイ"
