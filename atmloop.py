for i in range(101):
 import random
otp=random.randrange(0000,9999)
print (otp)
print("enter otp")
o=eval(input())
if otp==o:
    amount=20000
    print("enter what you want to do")
    a=eval(input())
    if a==1:
        print("enter the amount you deposit")
        b=eval(input())
        total=b+amount
        print("total amount now")
        print(total)
    elif a==2:
        print("enter the amount to withdraw")
        b=eval(input())
        if b<amount: 
            print("amount is sufficient")
            amount=amount-b
            print("now your total amount is")
            print(amount)
        else:
            print("amount is insufficient")
    else:
        print("your account balance is:")
        print(amount)
else:
    print("invalid otp")