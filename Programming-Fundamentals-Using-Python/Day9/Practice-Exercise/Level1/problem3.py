#PF-Prac-3
def create_new_dictionary(prices):
    return {k:prices[k] for k in prices if prices[k]>200}


prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))
