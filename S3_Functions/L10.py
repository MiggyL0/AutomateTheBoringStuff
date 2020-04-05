def spam():
    global eggs
    eggs = 'hello'
    print(eggs)

eggs = 42
spam()
print(eggs)