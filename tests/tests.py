from package_kw_5.modul import get_employers

def test_imployrs():
    result = get_employers()
    assert result is not None
