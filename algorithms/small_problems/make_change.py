def make_change(target_amount):
    coins = [200,100,50,20,10,5,2,1]
    count = 0
    values = []
    for coin in coins:
        while target_amount >= coin:
            target_amount = target_amount - coin
            values.append(coin)
            count += 1
    
    return count, values

print(make_change(24))
print(make_change(163))