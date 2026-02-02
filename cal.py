import random

for i in range(1, 10**18):   # infinite loop

    print("\n🧮 CALCULATOR MENU 🧮")
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press 5 for Exit")

    # Generate OTP
    otp = random.randint(1000, 9999)
    print("\nYour OTP is:", otp)

    user_otp = int(input("Enter OTP: "))

    if user_otp == otp:
        print("✅ OTP Verified")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result =", a + b)

        elif choice == 2:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result =", a - b)

        elif choice == 3:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result =", a * b)

        elif choice == 4:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            if b == 0:
                print("❌ Cannot divide by zero")
            else:
                print("Result =", a / b)

        elif choice == 5:
            print("🙏 Calculator Closed")
            break

        else:
            print("❌ Invalid Choice")

    else:
        print("❌ Invalid OTP")