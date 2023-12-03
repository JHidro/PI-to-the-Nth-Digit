import mpmath
import mpmath as mp

# 1002 since it'll be 998 digits after the decimal point if I remove the 3.
mpmath.mp.dps = 1002
pi_list = list(str(mp.pi))
# Removes 3 and . to give a more accurate answer
del pi_list[0]
del pi_list[0]

# checks to see if the input is a letter or special character, gives prompt instead of error
try:
    n = input('Enter a number: ')
    int(n)
except:
    pass

def negCheck():
    while True:
        list(n)
        # Checks to see if input is negative
        if '-' in n:
            print('Sorry, negative numbers are not allowed.')
            break
        try:
            if int(n) <= 1001:
                print(pi_list[int(n) - 1])
                break
            elif int(n) >= 1001:
                print('Sorry, your number is too high, please enter a number lower than 1001.')
                break
            else:
                print('Sorry, your input is Invalid')
                break
        except:
            print('Invalid Input, make sure your input is a whole number.')
            break



negCheck()




