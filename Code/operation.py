
# Function to get laptop details for customer purchase
def get_laptop_details(laptop_dict):
    while True:      
        try:
            laptop_choice = int(input("Enter the S.N. of the laptop that customer wants to buy: "))
             # Check if laptop choice is valid
            if laptop_choice not in laptop_dict:
                print()
                print("Invalid S.N. Please enter a valid S.N.\n")
                continue     
        except:
            print()
            print("We're sorry, but the S.N you entered is not valid. Please enter a numeric value.\n")
            continue
         # Get laptop data from dictionary
        laptop_data = laptop_dict[laptop_choice]

        # Get current quantity of the selected laptop
        current_quantity = int(laptop_data[3])

        # Ask the customer how many laptops they want to buy
        while True:
            try:
                quantity = int(input("Enter the quantity that customer wants to buy: "))
                # Check if requested quantity is availabl
                if quantity <= 0 or quantity > current_quantity:
                    print()
                    print("Sorry, the requested quantity is not available in our shop.\n")
                    
                else:
                    break
            except:
                print()
                print("We're sorry, but the quantity you entered is not valid. Please enter a numeric value.\n")

        # Get price of the selected laptop
        price = laptop_data[2]
        break

    return laptop_data, price, quantity ,current_quantity,laptop_choice

# Function to get laptop details for manufacturer purchase
def get_laptop_detail(laptop_dict):
    while True:
        try:
            laptop_choice = int(input("Enter the S.N. of the laptop you want to purchase from the manufacturer: "))
            # Check if laptop choice is valid
            if laptop_choice not in laptop_dict:
                print()
                print("Invalid S.N. Please enter a valid S.N.\n")
                continue
        except:
            print("We're sorry, but the S.N you entered is not valid. Please enter a numeric value.\n")
            continue

        # Get laptop data from dictionary    
        laptop_data = laptop_dict[laptop_choice]

        # Ask the customer how many laptops they want to buy
        while True:
            try:
                quantity = int(input("Enter the quantity you want to purchase: "))
                # Check if requested quantity is valid
                if quantity <= 0 :
                    print()
                    print("Sorry admin!. The quantity is invalid\n")
                else:
                    current_quantity = int(laptop_data[3])
                    break
            except:
                print()
                print("We're sorry, but the quantity you entered is not valid. Please enter a numeric value.\n")
                continue

        # Get price of the selected laptop
        price = laptop_data[2]
        break
    return laptop_data, price, quantity ,current_quantity,laptop_choice
    

company_name = "Pacific Technology"
location = "Ocean Boulevard Street, South Carolina, USA"
phone_number = "555-1234"
email = "PacificTech1995@gmail.com"

# Shop header function to display company information
def shop_header():
    print("*" * 210)
    print(f"{' ' * 90}{company_name}")
    print(f"{' ' * 80}{location}")
    print(f"{' ' * 77}Phone: {phone_number} Email: {email}")
    print("*" * 210)
    print()
    print("Welcome back, admin! Your expertise and attention to detail keep our PC store running smoothly.\n")

# Function to create header for invoice file
def invoice_header(file):
    file.write(f"{'-'*90}\n")
    file.write(f"{' ' * 40}{company_name}\n")
    file.write(f"{' ' * 30}{location}\n")
    file.write(f"{' ' * 27}Phone: {phone_number} Email: {email}\n")
    file.write(f"{'-'*90}\n\n")
    
    


