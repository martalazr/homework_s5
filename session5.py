print("Hello! Let's calculate your net salary")

try:
    gross = float(input("What is your gross salary? "))
    children = int(input("How many children do you have? "))
except ValueError:
    print("Your input was invalid. Try again. ")
else:
    if gross < 1000:
        tax = 0.1 * gross
    elif gross < 2000:
        tax = 0.12 * gross
        tax_cut = 0.01 * gross * children
    elif gross < 4000:
        tax = 0.14 * gross
        tax_cut = 0.01 * gross * children
    else:
        tax = 0.18 * gross
        tax_cut = 0.005 * gross * children


net = gross + tax_cut - tax
print("Your net salary is ", net)

