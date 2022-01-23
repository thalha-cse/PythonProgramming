min_num = int(input("Enter the number:- "))
max_num = int(input("Enter the number:- "))
for num in range(min_num, max_num+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
