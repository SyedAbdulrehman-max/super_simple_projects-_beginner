# Get user input
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

def calculate_bmi():
    if height > 0:
        # Ask user the unit
        unit = int(input("Height unit - Meter or Centimeters (1 for meters / 2 for cm): "))
        
        # Convert if needed
        if unit == 1:
            height_m = height  # Already in meters
        elif unit == 2:
            height_m = height / 100  # Convert cm to meters
        else:
            print("Invalid choice for unit!")
            return
        
        # BMI calculation
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 1)  # Round to 1 decimal
        
        # Classify BMI
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"
        
        # Print result
        print(f"Your BMI is {bmi}. Category: {category}")
    else:
        print("Height must be greater than 0.")

# Call the function
calculate_bmi()
