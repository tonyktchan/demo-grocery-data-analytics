'''
test3.py is used to generate the subtotal of orders by each customer
'''
import pandas as pd

#
# (A) subtotal_gen function is called by main.py
#     returning the final list of running sub_total, sorted by customer_id and order_id
#     each row represents the previous subtotal of 'cooked, breakfast, reduced' items purchased by the customer
#     and the additional of purchase of 'cooked, breakfast, reduced' with the associated quantity
#     Please note that product_id under 'None' category will not be included in this calculation
#
#     Returning sub_total list
#
def subtotal_gen (history)-> "subtotal_dataset":

    historical_data = history
    num_records = len(historical_data)
    print(f"The generated no. of rows in subtotal.csv is {num_records}")
    # sort the historical data using customer_id and then by date
    sorted_history = sorted(historical_data, key=lambda x:((x["customer_id"], "%S"), (x["order_date"], "%Y-%m-%d")))
    
    df = pd.DataFrame.from_dict(sorted_history)
    df.to_csv("order_by_customer.csv")

 
    current_index = 0
    sub_total = []
    
    while current_index < num_records:
        product = sorted_history[current_index]["product_id"]
        quantity = sorted_history[current_index]["quantity"]
        cat_prefix = product[0]
        current_order_id = sorted_history[current_index]["order_id"]
        current_customer_id = sorted_history[current_index]["customer_id"]

        # depends on the current record only / independent of customer_id
        if cat_prefix == "c":
            this_order_cooked_count = quantity
            this_order_breakfast_count  = 0
            this_order_reduced_count = 0
        elif cat_prefix == "b":
            this_order_cooked_count = 0
            this_order_breakfast_count  = quantity
            this_order_reduced_count = 0
        elif cat_prefix == "r":            
            this_order_cooked_count = 0
            this_order_breakfast_count  = 0
            this_order_reduced_count = quantity
        else:
            this_order_cooked_count = 0
            this_order_breakfast_count  = 0
            this_order_reduced_count = 0
    
                        
        if current_index == 0:                
            prev_cooked_count = 0
            prev_breakfast_count = 0
            prev_reduced_count = 0
        # when not in the first record 
        # will depend on if a new start of customer_id and get the value from sub_total[]
        
        else:
            current_customer_id = sorted_history[current_index]["customer_id"]
            last_customer_id = sorted_history[current_index-1]["customer_id"]
            if current_customer_id != last_customer_id:
                prev_cooked_count = 0
                prev_breakfast_count = 0
                prev_reduced_count = 0
            else:
                prev_cooked_count = sub_total[current_index-1]["prev_cooked_count"] + sub_total[current_index-1]["this_order_cooked_count"]
                prev_breakfast_count = sub_total[current_index-1]["prev_breakfast_count"] + sub_total[current_index-1]["this_order_breakfast_count"]
                prev_reduced_count = sub_total[current_index-1]["prev_reduced_count"] + sub_total[current_index-1]["this_order_reduced_count"]
        
        record={"customer_id":current_customer_id, "order_id":current_order_id, "prev_cooked_count": prev_cooked_count, "prev_breakfast_count": prev_breakfast_count, "prev_reduced_count": prev_reduced_count, "this_order_cooked_count": this_order_cooked_count, "this_order_breakfast_count": this_order_breakfast_count, "this_order_reduced_count": this_order_reduced_count}

        sub_total.append(record)
        
        # print(sub_total)
                
        current_index +=1



    return sub_total

#
# this is the end of test3.py
#
        

    

    

    