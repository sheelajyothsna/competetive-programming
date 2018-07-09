import random

def rand5():
    return random.randint(1, 5)

# def rand7():

#     # Implement rand7() using rand5()
#     rand = ( rand5() - 1 ) * 5 + rand5()
#     while ( rand > 21 ):
#         rand = ( rand5() - 1 ) * 5 + rand5()
#     return rand%7+1

def rand7():
    r = rand5() + rand5() * 5 - 6
    return (r % 7) + 1 if r < 21 else rand7()

print 'Rolling 7-sided die...'
print rand7()
