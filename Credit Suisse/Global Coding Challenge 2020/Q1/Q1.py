# https://www.credit-suisse.com/pwp/hr/en/codingchallenge/#/questions/1

stock_prices = [int(x) for x in input().split()]
no_days = stock_prices[0]
max_profit = None
for i in range(1, no_days+1):
    b_price = stock_prices[i]
    for j in range(i+1, no_days):
        s_price = stock_prices[j]
        profit = s_price - b_price
        if max_profit is None:
            max_profit = profit
        elif profit > max_profit:
            max_profit = profit
print(max_profit)
