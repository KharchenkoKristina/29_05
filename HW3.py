num = int(input("Введіть 5-х значне число: "))

revers = 0
revers += (num % 10) * 10000
num //= 10
revers += (num % 10) * 1000
num //= 10
revers += (num % 10) * 100
num //= 10
revers += (num % 10) * 10
num //= 10
revers += (num % 10) * 1

print(revers)
