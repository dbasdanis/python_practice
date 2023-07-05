def square(num):
    for n in range(1,num):
        yield n **2

print(list(square(10)))