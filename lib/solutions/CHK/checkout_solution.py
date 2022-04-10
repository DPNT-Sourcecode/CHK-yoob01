

# noinspection PyUnusedLocal
# skus = unicode string

# prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
# offers = {"A": [3, 130, 5, 200], "B": [2, 45], "E": []}

prices = {"A": [50, 130, 200], "B": [30, 45], "D": [15], "E": [40]}
quantities = {"A": [1, 3, 5], "B": [1, 2], "D": [1], "E": [1]}

def find_best_deal(prices, quantities, number_of_items, sku):
    '''
    We're going to group all deals together, so if we have 12 As then we're going to see how
    many A's we can group into a five deal, then how many to group into 3 and then 1. In general
    given a list of N deals (and assuming that N-1 < N) we can apply this same heuristic
    '''
    _prices = prices[sku]
    _quantity = quantities[sku]
    number = number_of_items[sku]
    # Since we've listed the prices and quantities from lowest to highest
    # but want to group highest to lowest, we need to reverse the quantity
    # Loop over every possible grouping that we have
    counters = {i: 0 for i in _quantity}
    for index, value in enumerate(reversed(_quantity)):
        # Find the "leading term" so if we have 7 A's bought, then 7 // 5 = 1, which means that
        # we can form 1 5 bargin
        leading_term = number // value
        # if the leading term is less than 1, then we can't form any bargins
        if leading_term < 1:
            # so move onto the next in value in the deal
            continue
        # subtract the number of items we've formed a bargin with
        number -= leading_term * value
        # save that leading term
        counters[value] = leading_term
    # We return a dictionary of counters, that maps the deals to the number of those deals we can form
    # So for example, given an 14 A's we can form 2 "5 deals", 1 "3 deal" and 1 "1 deal"
    # so the output would be {5: 2, 3: 1, 1: 1}
    return counters


def checkout(skus):
    '''
    skus: a string eg. "AAB"
    '''
    # First check that all the skus are in the prices dict
    for char in skus:
        if char not in prices.keys():
            return -1
    
    # Now add up all items to find the total
    number_of_items = {}
    for char in skus:
        if char in number_of_items:
            number_of_items[char] += 1
        else:
            number_of_items[char] = 1
    
    total_for_each_sku = {}
    for sku in number_of_items:
        deal_groupings = find_best_deal(prices, quantities, number_of_items, sku)
        running_total = 0
        for grouping in deal_groupings:
            running_total += grouping * deal_groupings[grouping]
        total_for_each_sku[sku] = running_total


    running_total = 0
    for sku in total_for_each_sku:
        running_total += total_for_each_sku[sku]
    
    return running_total

