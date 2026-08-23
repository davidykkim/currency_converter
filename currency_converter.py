def usd_to_eur(amount):
    return amount * 0.85


def usd_to_jpy(amount):
    return amount * 147.00


def usd_to_gbp(amount):
    return amount * 0.74


def main():
    print("Currency Converter")
    print("------------------")
    print("1. USD → EUR")
    print("2. USD → JPY")
    print("3. USD → GBP")

    choice = input("Choose a conversion: ")
    amount = float(input("Enter amount in USD: "))

    if choice == "1":
        result = usd_to_eur(amount)
        print(f"${amount:.2f} USD = €{result:.2f} EUR")

    elif choice == "2":
        result = usd_to_jpy(amount)
        print(f"${amount:.2f} USD = ¥{result:.2f} JPY")

    elif choice == "3":
        result = usd_to_gbp(amount)
        print(f"${amount:.2f} USD = £{result:.2f} GBP")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
