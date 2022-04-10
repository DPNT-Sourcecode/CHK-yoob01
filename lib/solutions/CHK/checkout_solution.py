

# noinspection PyUnusedLocal
# skus = unicode string

# prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
# offers = {"A": [3, 130, 5, 200], "B": [2, 45], "E": []}

prices = {"A": [50, 130, 200], "B": [30, 45], "D": [15], "E": [4]}
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
    # So for example, given an 14 A's we can form 
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
    for i in number_of_items:
        total_for_each_sku[i] = prices[i] * number_of_items[i]

    # Once we've added up all the different skus, check for special offers
    for sku in number_of_items:
        if sku in offers:
            # if an sku is in an offer then we'll need to find out how many
            # of those offers can be applied... I think? so buying 6A's should be 260
            # Extract the minimum ammount for the offer
            if len(offers[sku]) > 2:
                # if the len of the offers array is greater than 2, we have multiple offers to deal with
                # We'll need to find the best offer to apply, so if we have 12 A, then we could group that as 
                # 4 * 3A or as 2 * 5A + 2A, which one is better? With a huristic we can do this a lot easier
                pass
            # if the number of items bought is larger than the offer amount, apply the discount
            if number_of_items[sku] >= offer_amount:
                if number_of_items[sku] % offers[sku][0] == 0:
                    # if the number of items is just a multiple of the offer amount
                    # then it's easy to see we just need to apply a multiple of the offer
                    multiplier = number_of_items[sku] / offers[sku][0]
                    total_for_each_sku[sku] = offers[sku][1] * multiplier
                else:
                    # When the number of items isn't a multiple, then it's a little harder
                    # say we have 4 items, then we can group this as 1 offer + 1 sku
                    # Likewise if we have 5 items then we can group this as 1 offer + 2 sku

                    # say we have 5 A items, then number_of_skus is going to be 5 - 3 = 2 
                    number_of_skus = number_of_items[sku] % offers[sku][0]
                    number_of_offers = int(number_of_items[sku] / offers[sku][0])
                    total_for_each_sku[sku] = (prices[sku] * number_of_skus) + (offers[sku][1] * number_of_offers)


    running_total = 0
    for sku in total_for_each_sku:
        running_total += total_for_each_sku[sku]
    
    return running_total






