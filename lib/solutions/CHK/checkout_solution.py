

# noinspection PyUnusedLocal
# skus = unicode string

prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
offers = {"A": [3, 130, 5, 200], "B": [2, 45], "E": []}

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
                # 4 * 3A or as 2 * 5A + 2A, which one is better? This looks like a DP rod cutting problem.
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






