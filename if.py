pin = 1234
print("Vvedite porzalujsta vasz pin kod:")
user_pin = int(input())

if pin == user_pin:
    print("Kakuju summy wy hotite snjac")
else:
    print("Oszibka, vvedite korrectnyj pin code. U vas ostalos 2e popytki.")
    user_pin = int(input())
    if pin == user_pin:
        print("Kakuju summy wy hotite snjac")
    else:
        print("Oszibka, vvedite korrectnyj pin code. U vas ostalos 1a popytka.")
        user_pin = int(input())
        if pin == user_pin:
            print("Kakuju summy wy hotite snjac")
        else:
            print("Vasza karta zablokirowana. Pozalujsta obratites w bank.")

