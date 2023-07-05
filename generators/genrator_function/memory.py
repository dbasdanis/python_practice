def all_the_nums():
    num = 0
    while True:
        yield num
        num += 1

for num in all_the_nums():
    print(num)