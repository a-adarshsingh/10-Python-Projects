"""
Unit Converter — converts between units of length, weight, and temperature.
"""

LENGTH_TO_METERS = {
    "mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
    "inch": 0.0254, "foot": 0.3048, "yard": 0.9144, "mile": 1609.344,
}

WEIGHT_TO_GRAMS = {
    "mg": 0.001, "g": 1.0, "kg": 1000.0,
    "oz": 28.3495, "lb": 453.592,
}


def convert_length(value, from_unit, to_unit):
    meters = value * LENGTH_TO_METERS[from_unit]
    return meters / LENGTH_TO_METERS[to_unit]


def convert_weight(value, from_unit, to_unit):
    grams = value * WEIGHT_TO_GRAMS[from_unit]
    return grams / WEIGHT_TO_GRAMS[to_unit]


def convert_temperature(value, from_unit, to_unit):
    # Convert to Celsius first
    if from_unit == "c":
        celsius = value
    elif from_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "k":
        celsius = value - 273.15
    else:
        raise ValueError("Unknown temperature unit")

    if to_unit == "c":
        return celsius
    elif to_unit == "f":
        return celsius * 9 / 5 + 32
    elif to_unit == "k":
        return celsius + 273.15
    else:
        raise ValueError("Unknown temperature unit")


def length_menu():
    print(f"\nAvailable units: {', '.join(LENGTH_TO_METERS)}")
    from_unit = input("From unit: ").strip().lower()
    to_unit = input("To unit: ").strip().lower()
    if from_unit not in LENGTH_TO_METERS or to_unit not in LENGTH_TO_METERS:
        print("Unknown unit.")
        return
    try:
        value = float(input("Value: "))
    except ValueError:
        print("Invalid number.")
        return
    result = convert_length(value, from_unit, to_unit)
    print(f"\n{value} {from_unit} = {result:.4f} {to_unit}")


def weight_menu():
    print(f"\nAvailable units: {', '.join(WEIGHT_TO_GRAMS)}")
    from_unit = input("From unit: ").strip().lower()
    to_unit = input("To unit: ").strip().lower()
    if from_unit not in WEIGHT_TO_GRAMS or to_unit not in WEIGHT_TO_GRAMS:
        print("Unknown unit.")
        return
    try:
        value = float(input("Value: "))
    except ValueError:
        print("Invalid number.")
        return
    result = convert_weight(value, from_unit, to_unit)
    print(f"\n{value} {from_unit} = {result:.4f} {to_unit}")


def temperature_menu():
    print("\nAvailable units: c (Celsius), f (Fahrenheit), k (Kelvin)")
    from_unit = input("From unit: ").strip().lower()
    to_unit = input("To unit: ").strip().lower()
    if from_unit not in ("c", "f", "k") or to_unit not in ("c", "f", "k"):
        print("Unknown unit.")
        return
    try:
        value = float(input("Value: "))
    except ValueError:
        print("Invalid number.")
        return
    result = convert_temperature(value, from_unit, to_unit)
    print(f"\n{value}{from_unit.upper()} = {result:.2f}{to_unit.upper()}")


def main():
    menu = """
1. Length
2. Weight
3. Temperature
4. Exit
"""
    print("=== Unit Converter ===")
    while True:
        print(menu)
        choice = input("Choose a category: ").strip()

        if choice == "1":
            length_menu()
        elif choice == "2":
            weight_menu()
        elif choice == "3":
            temperature_menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
