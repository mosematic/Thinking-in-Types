# practicing string formatting

# print customer order
customer: str = 'James'
pizza_base: str = 'Thin'
pizza_size: int = 13
topping: str = 'chicken'
extra_cheese: bool = False
price: float = 10.6

# -------------------------------------------------------
# alternative 1 - using print function
# -------------------------------------------------------

print(f'Recieved order from: {customer}')
print(
    f'Pizza Base: {pizza_base}, Size: {pizza_size} inches, Toppings: {topping}')
print(f'Is extra cheese required: {extra_cheese}')
print(f'Total Bill: {price}')


# ------------------------------------
# alternative 2- using formatted string
# ------------------------------------

order_details: str = f"""
Recieved order from: {customer}
Pizza Base: {pizza_base}, Size: {pizza_size} inches, Toppings: {topping}
Is extra cheese required: {extra_cheese}
Total Bill: {price}
"""
print(f'{order_details}')
