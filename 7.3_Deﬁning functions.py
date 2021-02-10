def greeting(): 
    print("Hello World!")

greeting()
x = greeting()

def square(x): 
    return x * x

for i in range(5): 
    i_squared = square(i) 
    print(i, '*', i, '=', i_squared)


def upperAndLower(string): 
    return string.upper(), string.lower()
    
testword = 'Banana'

uppercase, lowercase = upperAndLower(testword)
print(testword, 'in lowercase:', lowercase, 'and in uppercase', uppercase)






