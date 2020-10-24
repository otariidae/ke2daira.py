from ke2daira import __version__, ke2dairanize


def test_version():
    assert __version__ == "0.1.1"


def test_matsudaira_ken():
    assert ke2dairanize("松平 健") == "ケツダイラ マン"


def test_paul_maccartney():
    assert ke2dairanize("ポール マッカートニー") == "マール ポッカートニー"


def test_che_guevara():
    assert ke2dairanize("チェ ゲバラ") == "ゲ チェバラ"


def test_katou_ai():
    assert ke2dairanize("加藤 あい") == "アトウ カイ"


def test_atou_kai():
    assert ke2dairanize("阿藤 快") == "カトウ アイ"


def test_harry_potter():
    assert ke2dairanize("ハリー ジェームズ ポッター") == "ポリー ジェームズ ハッター"
