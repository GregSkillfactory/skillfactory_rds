print('Угадаю число от 1 до -')
uppBrd = int(input())
from random import random
num = int(random() * uppBrd)
print('Загадано число от 1 до', uppBrd, 'Это -', num)

num1 = 0
num2 = uppBrd
count = 0
mid = 0
while num != mid:
    count += 1
    mid = int((num1 + num2) / 2)
    if num > mid:
        num1 = mid
    elif num < mid:
        num2 = mid

print("Вы угадали число {num} за {count} попыток.")
