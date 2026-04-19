from importlib.metadata import PackageNotFoundError, version

from .main import ke2dairanize

__all__ = ["__version__", "ke2dairanize"]


def __getattr__(name: str) -> str:
    if name != "__version__":
        msg = f"module {__name__!r} has no attribute {name!r}"
        raise AttributeError(msg)

    try:
        return version("ke2daira")
    except PackageNotFoundError as exc:
        msg = "Package metadata for 'ke2daira' is unavailable."
        raise RuntimeError(msg) from exc
