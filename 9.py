month = ("January", "Februrary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (15000, 28400, 30000, 23500, 20000, 16000, 28000, 25000, 24000, 25300, 19000, 60000)

max_profit = max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)




max_profit_month = month[max_profit_index]
print("The maximum profit of Rupees " + str(max_profit)+ " was recorded in the month of " + str(max_profit_month))



min_profit = min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)

min_profit_month = month[min_profit_index]
print("The minimum profit of Rupees " + str(min_profit)+" was recorded in the month of " +str(min_profit_month))