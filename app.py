def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price  # Return original price if discount is less than 20%

# Prompt user for input, calculate and display final price.
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(price, discount_percent)
    print(f"Final price after discount: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numerical values.")
