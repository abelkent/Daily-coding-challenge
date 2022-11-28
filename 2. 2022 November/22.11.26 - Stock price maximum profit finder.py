"""
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and selling that stock once. 
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, 
since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

def stock_profit(array):
    #Defines empty output array
    outputs = list()

    #Loops through each value in array as "starting value"
    for starting_index in range(len(array)):
        starting_value = array[starting_index]
        #Initial profit set to zero
        profit = 0
        for following_index in range(starting_index+1, len(array)):
            #For each value, if potential profit is greater than current profit, profit is replaced with new potential profit
            if profit < (array[following_index] - starting_value):
                profit = (array[following_index] - starting_value)
    
        #Maximum potential profit appended to output array
        outputs.append(profit)
    
    #Maximum array value returned
    return(max(outputs))

print(stock_profit([9, 11, 8, 5, 7, 10]))
