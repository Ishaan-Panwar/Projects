#calculator

print("This calculator can perform basic arithmetic operations")
arithmetic = input("What operation would you perform :  ")
if arithmetic.lower() == "addition":
     addend_one = input("The first addend : ")
     addend_two = input("The second addend : ")
     Sum = int(addend_one) + int(addend_two)
     print(f"The sum is {Sum}")
if arithmetic.lower() == "subtraction":
    minuend = input("What is the minuend : ")
    subtrahend = input("What is the subtrahend : ")
    Difference = int(minuend) - int(subtrahend)
    print(f"The difference is {Difference}")
if arithmetic.lower() == "multiplication":
    multiplicand = input("What is the multiplicand : ")
    multiplier = input("What is the multiplier : ")
    Product = int(multiplicand)*int(multiplier)
    print(f"The product is {Product}")
if arithmetic.lower() == "division":
    dividend = input("What is the dividend : ")
    divisor = input("What is the divisor : ")
    Quotient = int(dividend)/int(divisor)
    Remainder = int(dividend)%int(divisor)
    print(f"The quotient is {Quotient} and the remainder is {Remainder}")
    
