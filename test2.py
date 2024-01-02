'''
test2.py will be imported by main.py to generate unique orders by customers
'''
import random
import datetime
import hashlib
#
# (A) order_gen function is called by main.py 
#     returning the list of orders sorted first by order_date and second by customer_id
#

def order_gen(customer_list, product_list, quantity, products, no_order, no_day)-> "order_dataset":
'''
 generate customer orders
'''
    order_dataset = []
    unique_order_list = []

#
#    Generate the unique combination of customer_id and order_date
#    
    customer_ls = customer_list
    product_ls = product_list
    no_day_allowed = no_day
    no_order_allowed = no_order
    no_quantity = quantity
    no_products = products 
    current_order_no = 0


    while current_order_no < no_order_allowed: 
        customer_and_date = cust_date_gen(customer_ls, no_day_allowed)

        if customer_and_date not in unique_order_list:
            unique_order_list.append(customer_and_date)
            print(len(unique_order_list))
            current_order_no += 1
        else:
            print(len(unique_order_list))
    
    
    sorted_order_list = sorted(unique_order_list, key=lambda x:((x[1], "%Y-%m-%d"), (x[0], "%S")))
    
    # print("sorted_order_list is: \n")
    # print(sorted_order_list)
    
    #
    # sorted_order_list - date first and then by customer_id
    #
    # Input is unique_order_list[]
    #      
    # Generate flatten records with product_id and quantity for each order_id
    #
    current_order_no = 0
    generated_orders = []

    
    while current_order_no < no_order_allowed:
        # assuming a random 1 - 3 products for an order
        no_products=random.randint(1,3)
        purchased_products = []
        current_index = 0
        
        while current_index < no_products:
            purchased_products.append(product_ls[random.randint(0,len(product_ls)-1)])  
            current_index +=1
        

        #
        # generate quantity for each purchased product
        # 
        current_index = 0
        purchased_quantity = []
        while current_index < len(purchased_products):
            purchased_quantity.append(random.randint(1,no_quantity))  
            current_index +=1
        
        #
        # Generate full record(s) per order_id
        #             

        inner_index = 0
        for i in purchased_products:
            quant = purchased_quantity[inner_index]
            customer = sorted_order_list[current_order_no][0]
            order = current_order_no + 1
            order_date = sorted_order_list[current_order_no][1]
            record = {"order_id":order, "customer_id":customer, "order_date":order_date, "product_id":i, "quantity":quant}
            # print(record)
            inner_index +=1

            generated_orders.append(record)
            # print(historical_orders)
        
        current_order_no +=1
        
    # print(generated_orders)
        
    return generated_orders
    
#
# (B) cust_date_gen function is called by order_gen function 
#     returning the unique combination of customer_id and order_date for each order
#

def cust_date_gen(customer_list, no_day):

    present = datetime.datetime.now()
    present_timestamp = present.timestamp()
    print(present)
    # print(present_timestamp)

    # Generate a random number between 0 and no_day and multiple the number by 86400 (seconds in a day)
    random_day = random.randint(0, no_day) * 86400
    
    # Subtract the random number from the Unix timestamp of the present timestamp
    random_date_timestamp = present_timestamp - random_day

    # Convert the resulting Unix timestamp back to a datetime
    random_date = datetime.datetime.fromtimestamp(random_date_timestamp)

    # Print the random date
    # print(random_date)
    
    # extract date
    only_date = random_date.date()
    # print(only_date)
    customer_ls = customer_list
    customer_index = len(customer_ls)- 1
    customer_selected = customer_ls[random.randint(0,customer_index)]
    
    # print(customer_selected)
    customer_and_date_selected =[customer_selected, only_date]
    
    return customer_and_date_selected

#
# this is the end of test2.py
#