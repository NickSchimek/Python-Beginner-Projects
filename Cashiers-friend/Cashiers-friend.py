def printChange(coin, num, switch):
    if switch == 1:
        print('and')

    print(num, coin)
        
    

def coins(amount):
    '''returns a dictionary of the number of coins needed to be given back as change.
this function assumes the cashier has an unlimited supply of coins.'''
    
    numCoins = {25:0, 10:0, 5:0, 1:0}
    
    for i in (25, 10, 5, 1):
        numCoins[i] = amount//i
        amount = amount - numCoins[i] * i
    
    return numCoins

def inputMoney(switch):
    from decimal import Decimal
    if switch == 0:
        value = '\nEnter Price of Item: '
    else:
        value = 'Enter Amount Paid for Item: '
        
    while True:
        try:
            amount = float(input(value))
            amount = float(round(Decimal(amount),2))
            return amount

        except ValueError:
            print('doh! Not a Valid Input. Please try again.')
        

def calculate():
    ''' price and payment must be a float and will be rounded to the
nearest hundredth'''

    while True:
        while True:
            price = inputMoney(0)
            payment = inputMoney(1)

            if price > payment:
                print('\nInsufficient payment to cover cost of item. Ask for more money!')
                print('You must start over\n')
            else:
                break
            
        if payment == price:
            print('\nPayment is equal to price. No change needed.')
            print('Transaction Complete --> Program will now restart\n')
            
        else:
            change = coins(int(payment*100) - int(price*100))
            moneyTalks = {}
            for i in change:
                if i == 25 and change[i] > 1:
                    moneyTalks['Quarters'] = change[i]
                elif i == 25 and change[i] == 1:
                    moneyTalks['Quarter'] = change[i]
                    
                if i == 10 and change[i] > 1:                   
                    moneyTalks['Dimes'] = change[i]
                elif i == 10 and change[i] == 1:
                    moneyTalks['Dime'] = change[i]
                    
                if i == 5 and change[i] > 1:                
                    moneyTalks['Nickles'] = change[i]
                elif i == 5 and change[i] == 1:
                    moneyTalks['Nickle'] = change[i]
                    
                if i == 1 and change[i] > 1:
                    moneyTalks['Pennies'] = change[i]
                elif i == 1 and change[i] == 1:
                    moneyTalks['Penny'] = change[i]
                
                    
            count = len(moneyTalks)       
            if count == 1:
                count = 2
      
            print('\nPlease hand back the following:\n')
            for i in moneyTalks:
                printChange(i, moneyTalks[i], count)
                count -= 1
if __name__ == "__main__":
    calculate()
