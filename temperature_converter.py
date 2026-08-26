def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""

    # Convert input temperature to Celsius
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        return None

    # Convert Celsius to target unit
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return (celsius * 9 / 5) + 32
    elif to_unit == "K":
        return celsius + 273.15
    else:
        return None


print("===== Temperature Converter =====")
print("C = Celsius | F = Fahrenheit | K = Kelvin")

try:
    value = float(input("Enter temperature: "))
    from_unit = input("Enter input unit (C/F/K): ").upper()
    to_unit = input("Enter output unit (C/F/K): ").upper()

    result = convert_temperature(value, from_unit, to_unit)

    if result is None:
        print("Invalid temperature unit.")
    else:
        print(f"\n{value}°{from_unit} = {result:.2f}°{to_unit}")

except ValueError:
    print("Please enter a valid numerical temperature.")
