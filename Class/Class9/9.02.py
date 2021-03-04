print_name_2 = lambda name: print(f"Hello,{name}")
print_name_2(["dq","dqd"])


names = lambda names : [print_name_2(name) for name in names]
names(["sasha","vitya"])

