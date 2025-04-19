a = 1

def global_variable():
    global a
    a = a + 10

global_variable()

print(a)