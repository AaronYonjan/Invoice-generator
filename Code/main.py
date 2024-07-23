# Import the necessary modules
import datetime
import read
import write
import operation

# Get the current time
time = datetime.datetime.now()
# Read the laptop data from the text file and store it in a dictionary  
laptop_dict = read.ReadingLaptopText()

# Print the shop header
operation.shop_header()

# Start the main loop
loop = True
while loop == True:
    # Print the task options
    print("1. Customer's sale service.")
    print("2. Order laptops from the manufacture.")
    print("3. Exit the store. \n")

    # Prompt the user to select a task
    while True:
        try:
            task = int(input("You're in control. Select a number to indicate the task you'd like to do: "))
            break
        except:
            print()
            print("We're sorry, but the task you entered is not valid. Please enter a numeric value.\n")

    print()

    # If the user selects option 1, start the sale process
    if task == 1:

        #Prompt the admin to enter the customer name
        name = input("Enter the name of the customer: ")
        while not name:
            print()
            print("Name cannot be empty.\n")
            name = input("Enter the name of the customer: ")
        
        # Prompt the admin to enter the customer's phone number
        phone_num = input("Enter customer's phone no: ")
        while len(phone_num) != 10 or not phone_num.isdigit():
            print()
            print("Phone number must be a 10-digit number.\n")
            phone_num = input("Enter your phone no: ")
        phone_num = int(phone_num)
        
        boughtlaptops= []
        continueValue = True
        while continueValue:
            # Print the available laptops
            read.available_laptops()
            #Get the details of the selected laptop
            laptop_data, price, quantity, current_quantity, laptop_choice = operation.get_laptop_details(laptop_dict)
            
            # Calculate the total price of the laptop
            BrandName = laptop_data[1]
            laptopName = laptop_data[0]
            userQuantiy = quantity
            unitPrice = int(price)
            totalPrice = int(unitPrice) * int(userQuantiy)

            # Add the laptop to the list of bought laptops
            boughtlaptops.append((BrandName,laptopName,userQuantiy,f"${unitPrice}",f"${totalPrice}"))

            # Generate the invoice filename
            invoice_sale = f"Sold_{time.strftime('%Y %B %d_%H-%M-%S')}.txt"
            
            # Update the laptop dictionary with the new quantity
            laptop_dict[laptop_choice][3] = str(current_quantity - quantity)
            print("Laptop stock updated.\n")

            # Write the updated quantity back to the txt file
            write.WritingUpdatedtxt(laptop_dict)

             # Ask the user if they want to purchase another laptop
            while True:
                answer = input("Does Customer want to purchase another laptop? (y/n): ")
                if answer.lower() == "n": 
                    # Generate the sale invoice and print it
                    write.MakingSaleInvoice(name,phone_num,boughtlaptops,time,invoice_sale)
                    read.Sale_invoice_details(invoice_sale)
                    continueValue = False
                    break
                elif answer.lower() == "y":
                    break
                else:
                    print("Invalid option!") 
                    continue
    
    # If the admin selects option 2, start the Purchase process
    elif task == 2:

        #Prompt the admin to enter the  name
        name = input("Enter your name admin: ")
        while not name:
            print()
            print("Name cannot be empty.\n")
            name = input("Enter your name admin: ")
        
        laptopsOrder = []
        continueValue = True
        while continueValue:
            # Print the available laptops
            read.available_laptops()
            #Get the details of the selected laptop
            laptop_data, price, quantity, current_quantity, laptop_choice = operation.get_laptop_detail(laptop_dict)
            
            # Calculate the total price of the laptop
            BrandName = laptop_data[1]
            laptopName = laptop_data[0]
            userQuantiy = quantity
            unitPrice = int(price)
            totalPrice = int(unitPrice) * int(userQuantiy)

            # Add the laptop to the list of laptops order
            laptopsOrder.append((BrandName,laptopName,userQuantiy,f"${unitPrice}",f"${totalPrice}"))

            # Generate the invoice filename
            invoice_purchase= f"Order_{time.strftime('%Y %B %d_%H-%M-%S')}.txt"
            
            # Update the laptop dictionary with the new quantity
            laptop_dict[laptop_choice][3] = str(current_quantity + quantity)
            print("Laptop stock updated.\n")

            # Write the updated quantity back to the txt file
            write.WritingUpdatedtxt(laptop_dict)

            # Ask the admin to purchase another laptop
            while True:
                answer = input("Admin, do you want to order another laptop? (y/n): ")
                if answer.lower() == "n": 
                    write.MakingPurchaseInvoice(name,laptopsOrder,time,invoice_purchase)    
                    read.Purchase_invoice_details(invoice_purchase)
                    continueValue = False
                    break
                elif answer.lower() == "y":
                    break
                else:
                    print("Invalid option! Please input the valid option") 
                    continue     
    
    #if admin selects option 3 , program will terminate
    elif task == 3:
        print("We appreciate your visit admin!")
        loop = False
    else:
        print("Opps! Invalid task, please enter a valid task.\n")
