# https://www.credit-suisse.com/pwp/hr/en/codingchallenge/#/questions/2

String = [int(x) for x in input().split()]
stock_prices = String[1:]
no_days = String[0]
profit = 0

for i in range(no_days-1):
    if stock_prices[i+1] > stock_prices[i]:
        profit += stock_prices[i+1] - stock_prices[i]

print(profit)