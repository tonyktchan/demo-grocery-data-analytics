# demo-grocery-data-analytics
This is a demo repo to generate grocery (food) orders and sales using Python and Pandas with Unit Testing

### Python and Pandas DataFrames

Pandas and python built-in functions are being used as they are the most appropriate libraries for these order generation. Together with Faker, we can easily generate detailed customer database and sales transactions/database for any Data Analytics/Engineering Purposes.

No SQL or PySpark are being used (Their functions will be demonstrated in other upcoming repo).

### Source Files
To run:
python -m main

main.py will import test1.py, test2.py and test3.py to generate around 1,000 orders from 20 customers 
for the previous year (365 days).

Output csv files are:
- products.csv - a dimension table for the unique product_id into 3 categories (cooked-food, breakfast-food, reduced-food) and undefined category
- historical_orders.csv - contains all the 1,000 orders (around 2,000 itemised orders) from customer since previous year
- order_by_customer.csv - the customer orders are sorted for individual customer in chronological order
- subtotal.csv - is the final subtotal for each category for each customer for the last year


### Unit Testing
To run :
python -m test4

test4.py consists of several basic unit testings to ensure the csv files exist and have the expected number of records within limits (+/- 2 percent variations)

Enjoy!