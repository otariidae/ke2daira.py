from typing import Iterator, Union

class Token:
    reading: str
    surface: str

class Tokenizer:
    def __init__(
        self,
        udic: str = ...,
        *,
        udic_enc: str = ...,
        udic_type: str = ...,
        max_unknown_length: int = ...,
        wakati: bool = ...,
        mmap: bool = ...,
        dotfile: str = ...
    ) -> None: ...
    def tokenize(
        self,
        text: str,
        *,
        wakati: bool = ...,
        baseform_unk: bool = ...,
        dotfile: str = ...
    ) -> Iterator[Token]: ...

class WakatiModeOnlyException(Exception): ...
