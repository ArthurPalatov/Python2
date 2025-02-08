def smallest_divisor(x):
    for i in range(2, x + 1): 
        if x % i == 0: 
            return i  
x = int(input("Введите число: "))
print(smallest_divisor(x))