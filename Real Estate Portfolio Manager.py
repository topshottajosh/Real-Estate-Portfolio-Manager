# Portfolio Intialization
portfolio = []

# Welcome Message
print("Welcome to Lovell Portfolio Manager!")

# Menu While Loop
while True:
    print("\nLovell Portfolio Manager Operations:")
    print("1. Add a Property")
    print("2. Display Real Estate Portfolio")
    print("3. Calculate Total Rent Income")
    print("4. Exit Portfolio Manager")
    menu = input("What Operation Would You Like to Do: ")
    print()

    # "Lovell Portfolio Manager" Match Statement
    match(menu):
        # "Add a Property" Case Statement
        case("1"):
            name = input("Enter Property's Name: ")
            address = input("Enter Property's Address: ")
            tenants = int(input("Enter Number of Tenants: "))
            prop_type = input("Enter Property Type (Single/Multi-Family, Apartment, Commercial): ")
            installment = float(input("Enter Tenants Monthly Rent Installment: "))
            portfolio.append((name, address, tenants, prop_type, installment))
            print("\nThis Property has been added.")

        # "Display Real Estate Portfolio" Case Statement
        case("2"):
            for estate in portfolio:
                print(f"{estate[0]}: ")
                print(f"Address: {estate[1]}")
                print(f"Tenants: {estate[2]:,}")
                print(f"Property Type: {estate[3]}")
                print(f"Rent: ${estate[4]:,.2f}\n")

        # "Calculate Total Rent Income" Case Statement
        case("3"):
            total_rent = []
            for estate in portfolio:
                rent = estate[4] * estate[2]
                total_rent.append(rent)
            print(f"Your Portfolio's Total Gross Income: ${sum(total_rent):,.2f}")

        # "Exit Portfolio Manager" Case Statement
        case("4"):
            print("Thank You for using Lovell Portfolio Manager!!")
            print(("Before you go, Here's Your Portfolio Summary:\n"))
            print(f"Number of Properties: {len(portfolio)}")
            print(f"Portfolio's Gross Income: ${sum(total_rent):,.2f}")
            break

        # "Invalid Operation" Case Statement
        case _:
            print("Invalid Operation, Please Refer Back to Lovell Portfolio Manager Operation's Guide.")