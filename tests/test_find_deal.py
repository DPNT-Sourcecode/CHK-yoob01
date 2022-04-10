from lib.solutions.CHK.checkout_solution import checkout, find_best_deal

prices = {"A": [50, 130, 200], "B": [30, 45], "D": [15], "E": [4]}
quantities = {"A": [1, 3, 5], "B": [1, 2], "D": [1], "E": [1]}

def test_find_deal_3():
    number_of_items = {"A": }
    x = find_best_deal(prices, quantities, number_of_items, sku)