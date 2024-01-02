import hashlib
import random

#
# Task 1:
# (A) Additional assumptions:
# 
# Requirements on length and format of order_id, customer_id and product_id are not stated.
# These assumptions are used:
# - order_id (in test2.py) will be an integer from 0 to 999 in increment of 1.
# - customer_id will be a unique randomized token/string of 12 hexadecimal digit (0-f)
# - product_id will be a string consists of a character (either "c", "b", "r" or "z") followed by a unique 7 digit number (0-9)
#   as first character will be used to identify the category:
#   - c - cooked food
#   - b - breakfast food
#   - r - reduced food
#   - z - Null / None / Others 
#

#
# Task 1:
# (B) customer_id_gen function is called by main.py 
#     returning a list of customer_id
#

def customer_id_gen()-> "customer_id":
    """
    This function will generate tokenized 12 character string as customer_id  
    A random seed is used, can be replaced by the actual customer name
    """
    
    customer_info = str(random.randint(0, 9999))    
    raw_customer_id = hashlib.sha256(customer_info.encode()).hexdigest()
    customer_id = raw_customer_id[:12]
    print(f"The generated unique customer id is {customer_id}")

    return customer_id


#
# Task 1:
# (C) product_id_gen function is called by main.py 
#
#     returning a list of customer_id

def product_id_gen(cat)-> "product_id":
    """
    This function will generate unique 10 digit number as customer_id  
    A random seed is used, can be replaced by the actual customer_name
    """

    if type(cat) == type(None):
        product_prefix = "z"
    elif cat == "cooked":
        product_prefix = "c"                
    elif cat == "breakfast":
        product_prefix = "b"
    elif cat == "reduced":
        product_prefix = "r"
    else:
        return  # exit without returning product_id
   
    product_number = str(random.randint(1000000, 9999999))
       
    product_id = product_prefix + product_number
    print(f"The generated unique customer id is {product_id}")

    return product_id


#
# this is the end of test1.py
#
     