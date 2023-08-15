from typing import Iterator

class Token:
    reading: str
    surface: str

class Tokenizer:
    def __init__(  # noqa: PLR0913
        self: Tokenizer,
        udic: str = ...,
        *,
        udic_enc: str = ...,
        udic_type: str = ...,
        max_unknown_length: int = ...,
        wakati: bool = ...,
        mmap: bool = ...,
        dotfile: str = ...,
    ) -> None: ...
    def tokenize(
        self: Tokenizer,
        text: str,
        *,
        wakati: bool = ...,
        baseform_unk: bool = ...,
        dotfile: str = ...,
    ) -> Iterator[Token]: ...

class WakatiModeOnlyException(Exception): ...  # noqa: N818
