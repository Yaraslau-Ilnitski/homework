def unique(lst):
    seem = {}
    for i in lst:
        if not i in seem:  # если нет в словаре
            seem[i] = 1  # положим
            continue
        seem[i] += 1
    return  seem
print(unique([1,2,2,3,4,5,5,5,6,7]))
