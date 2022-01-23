min_num = int(input("Enter the number:- "))
max_num = int(input("Enter the number:- "))
for num in range(min_num, max_num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp // 10
    if num == sum:
        print(num)
