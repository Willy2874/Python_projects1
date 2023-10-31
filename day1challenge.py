#cost_of_item = 100
#selling_price = 150
#no_of_units = 5

#print((selling_price - cost_of_item) * no_of_units )


cost_of_item = float (input('Enter the initial cost:'))
selling_price = float (input('Enter the selling price:'))
no_of_units = float (input('Enter the number of units sold:'))

#print((selling_price - cost_of_item) * no_of_units )

def profit_computation(buying, selling, units): #function declaration (parameters)
    #function definition
    profit = (selling - buying) * units
    return profit 

print(profit_computation(cost_of_item, selling_price, no_of_units)) #function call


    







