# print("A"))

# a = 5 + "aj"

# x=-1
# if x < 0:
#     raise Exception("X should be positive")
# print("x is Posivite")

# try:
#     a = 5 / 0
# except Exception as e:
#     print("an error occured -- ", e)


# try:
#     a = 5 / 0
# except ZeroDivisionError as e :
#     print("an error occured --", e)
# finally:
#     print("Code end... ")


class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
def testValue(x):
    if( x > 100):
        raise ValueTooHighError("Value is too high.")
    elif x < 5:
        raise ValueTooSmallError("value is too small", x)
    else:
        print(x)

try:
    testValue(0)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)     













