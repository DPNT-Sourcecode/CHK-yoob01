

# noinspection PyUnusedLocal
# skus = unicode string

prices = {"A": 50, "B": 30, "C": 20, "D": 15}
offers = {"A": {3: 130}, "B": {2: 45}}

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
            offer_amount = offers[sku]








