a = 1

def global_variable(param):
    a = param + 1
    return a

print(a)

a = global_variable(a)

print(a)