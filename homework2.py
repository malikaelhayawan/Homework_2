while True:
    try:
        gross = int(input("Gross: "))
        children = int(input("Children: "))

        if gross < 1000:
            tax = 10
        elif gross < 2000:
            tax = 12
        elif gross < 4000:
            tax = 14
        else:
            tax = 18

        if gross < 2000:
            tax = tax - (children * 1)
        else:
            tax = tax - (children * 0.5)

        net = gross - (gross * tax / 100)

        print("Net:", net)
        break

    except:
        print("Wrong input, try again")
