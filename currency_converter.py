
def usd_to_eur(amount):
    return amount * 0.85


def usd_to_jpy(amount):
    return amount * 147.00


def usd_to_gbp(amount):
    return amount * 0.74


def usd_to_krw(amount):
    return amount * 1380.00


def usd_to_mxn(amount):
    return amount * 18.50


def usd_to_inr(amount):
    return amount * 87.00


def usd_to_aud(amount):
    return amount * 0.65


def main():
    print("Currency Converter")
    print("------------------")
    print("1. USD → EUR")
    print("2. USD → JPY")
    print("3. USD → GBP")
    print("4. USD → KRW")
    print("5. USD → MXN")
    print("6. USD → INR")
    print("7. USD → AUD")

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

    elif choice == "4":
        result = usd_to_krw(amount)
        print(f"${amount:.2f} USD = ₩{result:.2f} KRW")

    elif choice == "5":
        result = usd_to_mxn(amount)
        print(f"${amount:.2f} USD = ${result:.2f} MXN")

    elif choice == "6":
        result = usd_to_inr(amount)
        print(f"${amount:.2f} USD = ₹{result:.2f} INR")

    elif choice == "7":
        result = usd_to_aud(amount)
        print(f"${amount:.2f} USD = A${result:.2f} AUD")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
