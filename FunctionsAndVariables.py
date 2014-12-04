a = 3
b = 7
def function():
    a = 8
    b = 4
    print("Local Variable a:", a)
    print("Local Variable b:", b)
function()
print("Global Variable a:", a)
print("Global Variable b:", b)
