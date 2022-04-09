

# noinspection PyUnusedLocal
# skus = unicode string

prices = {"A": 50, "B": 30, "C": 20, "D": 15}
offers = {"3A": 130, "2B": 45}

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
    
    





