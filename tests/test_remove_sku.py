from lib.solutions.CHK.checkout_solution import checkout, find_best_deal, remove_sku, buy_get_free

def test_remove_sku_affee():
    output = remove_sku("AFFEE", buy_get_free)
    assert output == "AFEE"

def test_remove_sku_affeeffb():
    output = remove_sku("AFFEEFFB", buy_get_free)
    assert output == "AEEFF"

def test_remove_sku_ff():
    output = remove_sku("FF", buy_get_free)
    assert output == "F"

def test_remove_sku_abcdef():
    output = remove_sku("ABCDEF", buy_get_free)
    assert output == "ABCDEF"

def test_remove_sku_ffff():
    output = remove_sku("FFFF", buy_get_free)
    assert output == "FF"
