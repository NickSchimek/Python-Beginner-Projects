def bottlesOfBeer():
    num = 99
    while num > 1:
        print(num, 'bottles of beer on the wall,', num, 'bottles of beer.')
        print('Take one down and pass it around,', end=' ')
        num = num - 1
        if num > 1:
            beer = 'bottles'
        else:
            beer = 'bottle'
        print(num, beer, 'of beer on the wall,\n')


    print(num, 'bottle of beer on the wall,', num, 'bottle of beer.')
    print('Take one down and pass it around,', end=' ')
    num = num - 1
    print('No more bottles of beer on the wall,\n')

    print('No more bottles of beer on the wall, no more bottles of beer.')
    num = 99
    print('Go to the store and buy some more,', num, 'bottles of beer on the wall.')
