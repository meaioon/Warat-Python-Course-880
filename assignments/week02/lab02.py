"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used

"""

choiceforuser = input("1 Thai Baht --> US Dollar, 2 US Dollar --> Thai Baht : ")
estamount = float(input("Estimate Amount : "))
if choiceforuser == "1":
    print(f"{estamount} Thai Baht = {estamount / 35.5} US Dollar")
elif choiceforuser == "2":
    print(f"{estamount} US Dollar = {estamount * 35.5} Thai Baht")