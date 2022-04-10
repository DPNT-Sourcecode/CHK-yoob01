from lib.solutions.CHK.checkout_solution import checkout, find_best_deal, remove_sku, buy_get_free

def test_remove_sku_affee():
    output = remove_sku("AFFEE", buy_get_free)
    assert output == "AFEE"

def test_remove_sku_affeeffb():
    output = remove_sku("AFFEEFFB", buy_get_free)
    assert output == "AEEFF"