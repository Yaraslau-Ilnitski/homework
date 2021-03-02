a = int(input('Enter a number here:\n'))

def sum_of_numbers(num):
    sum = 1
    for i in range(num+1):
        if i > 1:
            i = 1 / i
            sum += i
    print(sum)

sum_of_numbers(a)