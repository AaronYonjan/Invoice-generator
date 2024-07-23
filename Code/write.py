import operation

'''This function creates a purchase invoice for a set of laptops
and saves it to a file'''
def MakingPurchaseInvoice(name,laptopsOrder,time,invoice_purchase):
    # Open the file in write mode
    with open(invoice_purchase, "w") as file:
        total_amount = 0
        # Calculate the total amount for all laptops in the order
        for i in laptopsOrder:
            total_amount += int(i[3].replace('$',''))
        # Calculate the VAT and gross amounts
        vat_rate = 0.13
        vat_amount = int(total_amount * vat_rate)
        gross_amount = int(total_amount + vat_amount)
        # Write the header and order details to the file
        operation.invoice_header(file)
        file.write(f"Admin Name: {name}\n")
        file.write(f"Ordered time: {time.strftime('%Y %B %d_%H-%M-%S')}\n\n")
        file.write(f"{'-'*90}\n")
        headers = ("Laptop Brand","Item Name" ,"Total Quantity", "Unit Price", "Total")
        file.write("{:<20}{:<20}{:<20}{:<20}{:<10}\n".format(*headers))
        file.write(f"{'-'*90}\n")
        for laptop in laptopsOrder:
            details = (laptop[0], laptop[1], laptop[2], laptop[3],laptop[4])
            file.write("{:<20}{:<20}{:<20}{:<20}{:<10}\n".format(*details))
        file.write(f"{'-'*90}\n\n")
        file.write(f"Total amount: ${total_amount}\n")
        file.write(f"VAT amount (13%): ${vat_amount}\n")
        file.write(f"Gross Amount: ${gross_amount}\n")
        file.write(f"Admin {name} authorized this transaction.\n")
        file.write(f"{'-'*90}\n")
        

''' This function creates a sale invoice for a set of laptops
 and saves it to a file'''
def MakingSaleInvoice(name,phone_num,boughtlaptops,time,invoice_sale):
    # Open the file in write mode
    with open(invoice_sale, "w") as file:
        total = 0 
        shippingCost = 100
        # Calculate the total cost for all laptops in the order
        for i in boughtlaptops:
            total+= int(i[3].replace('$',''))
        # Calculate the grand total (including shipping)
        grandTotal = total + shippingCost
        # Write the header and order details to the file
        operation.invoice_header(file)
        file.write(f"Customer Name: {name}\n")
        file.write(f"Phone no: {phone_num}\n")
        file.write(f"Sold time: {time.strftime('%Y %B %d_%H-%M-%S')}\n\n")
        header = ("Laptop Brand", "Item Name", "Total Quantity", "Unit Price", "Total")
        file.write(f"{'-'*90}\n")
        file.write("{:<20}{:<20}{:<20}{:<20}{:<10}\n".format(*header))
        file.write(f"{'-'*90}\n")
        for laptop in boughtlaptops:
            details = (laptop[0], laptop[1], laptop[2], laptop[3], laptop[4])
            file.write("{:<20}{:<20}{:<20}{:<20}{:<10}\n".format(*details))
        file.write(f"{'-'*90}\n\n")    
        file.write(f"Shipping Cost: ${shippingCost}\n")
        file.write(f"Grand Total: ${grandTotal}\n")
        file.write(f"{'-'*90}\n")


def WritingUpdatedtxt(laptop_dict) :
     # open the file 'Laptops.txt' in write mode
    with open("Laptops.txt", "w") as file:
         # loop through each laptop information in the laptop dictionary
        for laptop_info in laptop_dict.values():
            # join the laptop information with commas and add a newline character
            line = ",".join(laptop_info) + "\n"
            # write the line to the file
            file.write(line)
    
