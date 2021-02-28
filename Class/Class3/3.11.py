a = input().split('@')
if len(a) == 2:
    if a[1] == "gmail.com":
        print(a[0])
    else:
        print(f"{a[1]} is not supported")
else:
    print("Enter valid mail!")