#Meal price calculator
print("       Meal Price Calculator       ")
print("Calculate your meal cost with ease. ")
child_meal = float(input("Enter the price for child's meal: $"))
adult_meal = float(input("Enter the price for the adult meal: $"))
number_of_child = int(input("Enter the number of children: "))
number_of_adults = int(input("Enter the number of adults: "))

# calculate meal sub total
child_subtotal = number_of_child * child_meal
adult_subtotal = number_of_adults * adult_meal
meal_price_subtotal = child_subtotal + adult_subtotal
print(f"\nSubtotal: ${meal_price_subtotal:.2f}\n")

# calculate the sales tax and total
sales_tax_rate = float(input("Enter a sales tax rate(e.g, 6 or 6.5 for 6 percent or 6.5%): "))
sales_tax = (meal_price_subtotal * sales_tax_rate)/ 100
print(f"\nSales Tax: ${sales_tax:.2f}")
total = meal_price_subtotal + sales_tax
print(f"\nTotal: ${total:.2f}\n")

payment_amount = float(input("Enter amount to pay: $"))
change = payment_amount - total
print(f"\nChange: ${change:.2f}\n")

print("\n" + "=" * 40)
print("              MEAL RECEIPT")
print("=" * 40)

print(f"Children:              {number_of_child}")
print(f"Adults:                {number_of_adults}")
print()
print(f"Subtotal:          ${meal_price_subtotal:.2f}")
print(f"Sales Tax:          ${sales_tax:.2f}")
print("-" * 40)
print(f"TOTAL:             ${total:.2f}")
print()
print(f"Payment:            ${payment_amount:.2f}")
print(f"Change:              ${change:.2f}")
print("=" * 40)
print("   Thank you for your purchase!   ")
print("=" * 40)