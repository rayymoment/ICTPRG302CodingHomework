# Creating variables to hold the user's invoice number, sales amount and sales tax.
sales_amount=int(input("Please input the sales amount: "))
invoice_number=int(input("Please enter your invoice number."))

# Making sure invoice number is within 1,000 and 8,000
if invoice_number<1000 or invoice_number>8000:

else:
    print("Invalid invoice number, please try again.")
    breakpoint()

# Making sure sales amount is non-negative.
if sales_amount >= -1:
    continue
else:
    print("Invalid sales amount, please try again.")
