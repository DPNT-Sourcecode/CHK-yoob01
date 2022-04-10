from lib.solutions.CHK.checkout_solution import checkout, find_best_deal

prices = {"A": [50, 130, 200], "B": [30, 45], "D": [15], "E": [40]}
quantities = {"A": [1, 3, 5], "B": [1, 2], "D": [1], "E": [1]}

def test_checkout():
    # We have 3 A's, 1 B and 2 E's
    # So 130 + 30 + 40 + 40 - 30 (since we have a free B)
    total = checkout("AAABEE")
    assert total == 210

def test_checkout_abcde():
    total = checkout("ABCDE")
    assert total == 155

def test_checkout_eeb():
    total = checkout("EEB")
    assert total == 80

