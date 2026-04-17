def convert_length():
    # Input length in feet
    feet = float(input("Enter length in feet: "))
    
    # List of conversion names
    units = ["inches", "yards", "miles", "millimetres", "centimetres", "meters", "kilometres"]
    
    # Corresponding conversion factors
    conversions = [
        12,          # inches
        1/3,         # yards
        1/5280,      # miles
        304.8,       # millimetres
        30.48,       # centimetres
        0.3048,      # meters
        0.0003048    # kilometres
    ]
    
    # Display options
    print("\nChoose conversion:")
    for i in range(len(units)):
        print(f"{i+1}. {units[i]}")
    
    # User choice
    choice = int(input("Enter your choice (1-7): "))
    
    # Perform conversion
    if 1 <= choice <= len(units):
        result = feet * conversions[choice - 1]
        print(f"Length from feet to {units[choice - 1]} = {result}")
    else:
        print("Invalid choice")


# Run the program
convert_length()
