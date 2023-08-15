# ruff: noqa: S101
from ke2daira.kana2mora import katakana2mora


def test_saru() -> None:
    assert katakana2mora("サル") == ["サ", "ル"]


def test_kappa() -> None:
    assert katakana2mora("カッパ") == ["カ", "ッ", "パ"]


def test_chocorate() -> None:
    assert katakana2mora("チョコレート") == [
        "チョ",
        "コ",
        "レ",
        "ー",
        "ト",
    ]


def test_gakkyushinbun() -> None:
    assert katakana2mora("ガッキュウシンブン") == [
        "ガ",
        "ッ",
        "キュ",
        "ウ",
        "シ",
        "ン",
        "ブ",
        "ン",
    ]
