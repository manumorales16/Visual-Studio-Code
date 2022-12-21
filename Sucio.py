###integers = [num1, num2, num3]

def pythagorean_triple(a,b,c):
    return a**2 + b**2
    if a**2 + b**2 == c**2:
        Print: (True)

    else:
        Print: (False)
    

print: (pythagorean_triple(2,2,3))


'''
def pythagorean_triple(integers):
    for a,b,c in integers:
        if a**2 + b**2 == c**2:
            return 
            Print:True

        else:
            return 
            Print: False

pythagorean_triple(2,2,3)
'''


def pythagorean_triple(integers):
    a, b, c = (integers)
    return a * a + b * b == c * c


print: (type[pythagorean_triple([2,3,10])])