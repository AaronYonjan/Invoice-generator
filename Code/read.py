
# function to read the laptop information from a file
def ReadingLaptopText():
    with open("Laptops.txt","r") as file:
        laptop_dict= {}
        num = 1
        for line in file:
            line = line.replace("\n","")
            laptop_dict.update({num:line.split(",")})
            num = num + 1
    return laptop_dict
#function to print the purchase invoice details
def Purchase_invoice_details(invoice_purchase):
    with open(invoice_purchase, "r") as file:
        contents = file.read()
        print(contents)
    
#function to print the sale invoice details
def Sale_invoice_details(invoice_sale):
    with open(invoice_sale, "r") as file:
        contents = file.read()
        print(contents)

#function to print the list of available laptops
def available_laptops():
    # Define the headers of the table
    print("-"*100)
    headers = ["S.N.", "Laptop Name", "Company Name", "Price", "Quantity", "Graphics", "CPU"]

    # Print the headers of the table
    print("{: <5} {: <20} {: <20} {: <10} {: <10} {: <20} {: <10}".format(*headers))

    # Print the separator line
    print("-" * 100)

    # Open the file containing the list of laptops and print the data in a table
    with open("Laptops.txt", "r") as file:
        n = 0
        for line in file:
            laptop_data = line.strip().split(",")
            price = "$"+laptop_data[2]
            laptop_data[2] = price
            n += 1
            print("{: <5} {: <20} {: <20} {: <10} {: <10} {: <20} {: <10}".format(n, *laptop_data))
    print("-"*100 + "\n")



    