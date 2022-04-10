from lib.solutions.CHK.checkout_solution import checkout, find_best_deal

prices = {"A": [50, 130, 200], "B": [30, 45], "D": [15], "E": [4]}
quantities = {"A": [1, 3, 5], "B": [1, 2], "D": [1], "E": [1]}

def test_find_deal_14():
    number_of_items = {"A": 14}
    # best deal should be {5: 2, 3: 1, 1: 1}
    x = find_best_deal(prices, quantities, number_of_items, "A")
    assert len(x) == 3
    assert x[5] == 2
    assert x[3] == 1
    assert x[1] == 1