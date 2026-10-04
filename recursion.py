
#     n * (n-1)!
# #winding 
#     6! = 6 * 5! = 6*120 = 720
#     5! = 5 * 4! 
#     4! = 4 * 3!
#     3! = 3 * 2!
#     2! = 2 * 1!
#     1! = 1 * 0!
#     0! = 1 #basecase
# # unwinding 
#     1! = 1 * 1  = 1
#     2! = 2 * 1  = 2
#     3! = 3 * 2  = 6    
#     4! = 4 * 6  = 24
#     5! = 5 * 24 = 120
#     6! = 6 * 120 = 720

# def factorial (n):
#     if (n == 0):
#         return 1
#     else:
#         return n * factorial(n-1)
# num = int(input("please enter a positive integer: \n"))
# print ("the factorial of", num , "is", factorial(num))

# def compound_interest(principal, rate, years):
#     if years == 0:
#         return principal
#     else:
#         return compound_interest(principal * (1 + rate), rate, years - 1)
# principal = float(input("Enter principal: "))
# rate = float(input("Enter interest rate (as decimal): "))
# years = int(input("Enter number of years: "))

# amount = compound_interest(principal, rate, years)

# print("Final amount =", amount)

# def fibonacci(pos):
#     if (pos == 0):
#         return 0
#     elif (pos == 1):
#         return 1
#     else:
#         return fibonacci(pos-1 ) + fibonacci(pos-2)
# num = int(input("please enter your positive interger for the posistion of the value you want: \n"))
# print ("your value in the fibonacci sequence at position",num,"is",fibonacci(num))

def power(base,exponent):
    if (exponent ==0): #basecase
        return 1    #anything power 0 is 1 
    else:
        return base * power(base,(exponent -1))

base = int(input("please entter the base number as a whole interger:\n"))
exponent = int(input("please enter the exponent you want to be used along side your base number:\n"))
print ("your base:", base ,"to the power of:", exponent ,"is", power(base,exponent))

# def tribonacci(pos):
#     if (pos == 0):
#         return 0
#     elif (pos == 1):
#         return 1
#     elif (pos == 2):
#         return 1 
#     else:
#          return tribonacci(pos-1 ) + tribonacci(pos-2) + tribonacci(pos-3)
# num = int(input("please enter your positive interger for the posistion of the value you want: \n"))
# print ("your value in the fibonacci sequence at position",num,"is",tribonacci(num))
