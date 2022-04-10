from lib.solutions.CHK.checkout_solution import checkout, find_best_deal, remove_sku, buy_get_free

def test_remove_sku_affee():
    output = remove_sku("AFFEE", buy_get_free, {"A": 1, "F": 2, "E": 2})
    assert output == "AFFEE"

def test_remove_sku_affeeffb():
    output = remove_sku("AFFEEFFB", buy_get_free, {"A": 1, "F": 4, "E": 2, "B": 1})
    assert output == "AEEFF"

def test_remove_sku_ff():
    output = remove_sku("FF", buy_get_free, {"A": 1, "F": 2})
    assert output == "FF"

def test_remove_sku_abcdef():
    output = remove_sku("ABCDEF", buy_get_free, {"A": 1, "F": 1, "E": 1, "B": 1, "C": 1, "D": 1})
    assert output == "ABCDEF"

def test_remove_sku_ffff():
    output = remove_sku("FFFF", buy_get_free, {"F": 4})
    assert output == "FF"

