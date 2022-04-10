from lib.solutions.CHK.checkout_solution import checkout, find_best_deal

prices = {"A": [50, 130, 200], "B": [30, 45], "D": [15], "E": [40]}
quantities = {"A": [1, 3, 5], "B": [1, 2], "D": [1], "E": [1]}

def test_checkout():
    # We have 3 A's, 1 B and 2 E's
    # So 130 + 30 + 40 + 40 - 30 (since we have a free B)
    total = checkout("AAABEE")
    assert total == 210

def test_checkout_aa():
    total = checkout("AA")
    assert total == 100

def test_checkout_a():
    total = checkout("A")
    assert total == 50

def test_checkout_abcde():
    total = checkout("ABCDE")
    assert total == 155

def test_checkout_eeb():
    total = checkout("EEB")
    assert total == 80

def test_checkout_eeeb():
    total = checkout("EEEB")
    assert total == 120


def test_checkout_eeeeb():
    total = checkout("EEEEB")
    assert total == 160

def test_checkout_eeeebbb():
    total = checkout("EEEEBBB")
    # 4 * E + B = 4 * 40 + 30 = 160 + 30 = 190
    assert total == 190

def test_checkout_aaeeeebbb():
    total = checkout("AAEEEEBBB")
    # A + 4 * E + B = 50 + 4 * 40 + 30 = 160 + 30 = 190
    assert total == 290

def test_checkout_f():
    total = checkout("F")
    assert total == 10

def test_checkout_ff():
    total = checkout("FF")
    assert total == 10

def test_checkout_fff():
    total = checkout("FFF")
    assert total == 20

def test_checkout_affff():
    total = checkout("AFFFF")
    # A + 4 * F = 50 + 4 * 10 - 2 * 10 (because we get 2 free) = 70
    assert total == 70

def test_checkout_affffe():
    