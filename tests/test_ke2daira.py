from ke2daira import __version__, ke2dairanize


def test_version():
    assert __version__ == "0.1.1"


def test_matsudaira_ken():
    assert ke2dairanize("松平 健") == "ケツダイラ マン"
