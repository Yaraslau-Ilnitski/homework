a = [2,3,4]
b = [21,"sq",12]
print(id(a),id(b))
b = a
print(id(a),id(b))
b.append("syka")
print(id(b))
