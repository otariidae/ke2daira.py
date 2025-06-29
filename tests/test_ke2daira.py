# ruff: noqa: S101
from ke2daira import __version__, ke2dairanize


def test_version() -> None:
    assert __version__ == "0.2.0"


def test_matsudaira_ken() -> None:
    assert ke2dairanize("松平 健") == "ケツダイラ マン"


def test_paul_maccartney() -> None:
    assert ke2dairanize("ポール マッカートニー") == "マール ポッカートニー"


def test_che_guevara() -> None:
    assert ke2dairanize("チェ ゲバラ") == "ゲ チェバラ"


def test_katou_ai() -> None:
    assert ke2dairanize("加藤 あい") == "アトウ カイ"


@pytest.mark.xfail(reason="快がココロヨと読まれてしまう")
def test_atou_kai() -> None:
    assert ke2dairanize("阿藤 快") == "カトウ アイ"


def test_harry_potter() -> None:
    assert ke2dairanize("ハリー ジェームズ ポッター") == "ポリー ジェームズ ハッター"


def test_genzo() -> None:
    assert ke2dairanize("源蔵") == "ゲンゾウ"
