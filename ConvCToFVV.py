def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Conversion Script")
    print("--------------------------------")

    while True:
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius)}°F")
        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit)}°C")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()