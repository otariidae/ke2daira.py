# Python port of https://github.com/otariidae/kana2mora

from __future__ import annotations

SUTEKANA = {"ァ", "ィ", "ゥ", "ェ", "ォ", "ャ", "ュ", "ョ", "ヮ"}


def katakana2mora(kana: str) -> list[str]:
    chars = list(kana)
    moras: list[str] = []
    for char in chars:
        if char in SUTEKANA:
            previous_char = "" if len(moras) == 0 else moras.pop()
            mora = previous_char + char
            moras.append(mora)
            continue
        moras.append(char)
    return moras
