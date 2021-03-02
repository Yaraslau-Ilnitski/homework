numb = [1, 2, 2, 12, 56, 6, 12, 74, 123, 54, 11, 12, 13, 14, 15, 16, 17, 18, 19]

def find_greatest(lst):
    greatest = 0
    for i in range(len(lst)):
        if lst[i] > greatest:
            greatest = lst[i]
    return greatest

greatest = find_greatest(numb)

def replace_even_element(lst, numb, divider):
    for i in range(len(lst)):
        if lst[i] % divider == 0:
            lst[i] = numb
    return lst

print(replace_even_element(numb, greatest, 2))
