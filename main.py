'''
(I) Python files required to generate dataset are:
- main.py
- test1.py, test2.py and test3.py have various functions and imported by main.py 
- test4.py contains the unit tests for the output csv files 

   To run : python -m main

(II) Output files are :
- products.csv - 20 unique product_ids with categories
- order_by_customer.csv - 1,000 grocery orders by 20 customers
  Assumptions: please note that each order can include up 3 x product_ids.
               The max number of sold units for each product_id is 4 
  Therefore, the number of rows/records is estimated to be 1,000 x ((1+2+3)/3) = 2,000 rows/records

- historical_orders.csv - contains the sorted order_by_customer.csv in chronological order and customer_id
- subtotal.csv - is the running subtotal for all customers in the previous year (365 days)

(III) To run unit tests:  python -m test4
   If all tests are successful, the generated csv files/dataset are ready to use

'''
import sys
import random
import pandas as pd
import test1
import test2
import test3


#
# (A) Parametrize the Dataset Generation according to the requirements:
#

NUM_CUSTOMER = 20
NUM_PRODUCT = 20
NUM_ORDER = 1000
NUM_DAY = 365
LIST_CATEGORY = ["cooked", "breakfast", "reduced", None]


#
# (B).1 Generating unique number of customer_id according to NUM_CUSTOMER
# Output is a customer_list (a list) with customer_id as an item
#
# Perform testing of uniqueness of customer_id generated and 
# if not, will retry up to 10 generations
#
unique_generation = 0
num_generation = 0
customer_list = []

while unique_generation == 0 and num_generation < 10:
    
    for i in range (0, NUM_CUSTOMER, 1): 
        customer_id = test1.customer_id_gen()
        customer_list.append(customer_id)

    #
    # Testing of the unique of customer_id
    # in the customer_list
    # If not unique customer_id, will generate again 
    # 
    unique_customer_no = len(set(customer_list))
    
    if unique_customer_no == NUM_CUSTOMER:
        unique_generation = 1
    else:
        customer_list=[]
        num_generation += 1
        print("Generation of unique customer_id failed. Will have another try")

# check if unique generation of customer_id is successful or not
if unique_generation == 0:
    print("Failed to generate a list of unique customer_id after 10 trials")
    sys.exit(1)

#
# (B).2 Generating unique number of product_id according to NUM_PRODUCT
# Output is a product_list (a list) with product_id as each item
#
# Perform testing of uniqueness of product_id generated and 
# if not, will retry up to 10 generations
#

unique_generation = 0
num_generation = 0
product_list = []

print("Unique product_ids are being generated")

while unique_generation == 0:
    
    for i in range (0, NUM_PRODUCT, 1):

        category=LIST_CATEGORY[random.randint(0, 3)]
        product_id = test1.product_id_gen(category)

        #
        # Testing of product_id generation
        # Exit if LIST_CATEGORY is corrupted
        #
        if type(product_id) == type(None):
            print("No product_id is generated. Please check validity of the LIST_CATEGORY")
            sys.exit(3)
        else:
            product_list.append(product_id)

    #
    # Testing of the unique of product_id
    # in the product_list
    #
    unique_product_no = len(set(product_list))

    if unique_product_no == NUM_PRODUCT:
        unique_generation = 1
    else:
        product_list=[]
        num_generation += 1


# check if unique generation of product_id is successful or not
if unique_generation == 0:
    print("Failed to generate a list of unique product_id")
    sys.exit(2)

#
# (C) create a 'products' dimension table for product_list with category
#     with lookup to LIST_CATEGORY
#     the dimension table output is products.csv  

current_index = 0
product_dimension_table = []

for i in product_list:
    if i[0] == "z":
        category = None
    elif i[0] == "c":
        category = "cooked" 
    elif i[0] == "b":
        category = "breakfast"
    else:
        category = "reduced"
    
    record ={"product_id":i, "product_category":category}
    product_dimension_table.append(record)

print("Product Dimension table is generated successfully as follows:")    
print(product_dimension_table)

df = pd.DataFrame.from_dict(product_dimension_table)
df.set_index("product_id", inplace=True)
print(df.index.nunique())
print(len(df))
print(df.product_category.describe())
df.to_csv("products.csv")

#
# (D) The function will generate 1,000 orders (NUM_ORDER = 1000) 
#     happended within the previous year (365 days).
#
#     Each order consists of at least one or more product_id and the associated quantity.
#     To facilitate the following dataset generation, a generated order is flattened 
#     to whole single product_id and quantity associated
#     Each record within the same order, has the following schema/fields:
#     - unique order_id from 1 to 1000
#     - unique customer_id 
#     - a date within the last year (365 days) this order is made/completed - key/value
#     - product_id - randomly picked up from product_list
#     - quantity - quantity of the product in this order
#
#      Additional assumptions:
#      - each order will have a maximum of 3 product_id's (max 3 rows to constitute an order)
#      - the assumed maximum of quantity is 4 (valid range is 1-4) for each product_id in a record/sub-order
#
#       The output is historical_orders.csv -
#       - sorted first by order_date and second by customer_id
#       - since NUM_ORDER = 1000 and MAX_PRODUCTS = 3
#         the average no. of generated rows is 1000 * avg(1,2,3) = 2000 rows
#

MAX_QUANTITY = 4
MAX_PRODUCTS = 3

historical_orders = test2.order_gen(customer_list, product_list, MAX_QUANTITY, MAX_PRODUCTS, NUM_ORDER, NUM_DAY)

df = pd.DataFrame.from_dict(historical_orders)

df.set_index("order_id", inplace=True)


# overwrite previous one if exists
df.to_csv("historical_orders.csv")


# (E) Final part is to generate running subtotal per customer after each order (consist of multiple records / each record for 1 product_id)
#     Please note that as the prev_xxx_count and this_order_xxx_count exclude those under 'None' category
#  
#     The output is subtotal.csv - sorted record first on customer_id and order_id (which is order chronologically)


subtotal_per_customer = test3.subtotal_gen(historical_orders)

df = pd.DataFrame.from_dict(subtotal_per_customer)
df.to_csv("subtotal.csv")


#
# (F) Unit Testing - check the following
#
#     Please use the test4.py to perform the unit testing on the output files
#     command : python -m test4
#
#     This is the end of the required dataset generation
#

