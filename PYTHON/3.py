#Create two variables: price = 599.99 and discount = 0.15
#Calculate and print the final price after discount with 2 decimal places.
price=float(input("Price"))
discount=float(input("Discount"))
discount_price=price*discount
final_price=price-discount_price

print("Final price:",round(final_price,2))