'''
test4.py is used independently to perform unit tests on the output csv files
'''
import os 
import unittest
import pandas as pd


#
#
# This file contains some unit testing for 4 csv files as output of dataset generation
# - products.csv
# - order_by_customer.csv
# - historical_orders.csv
# - subtotal.csv (the final output)
#
class Compare2CSV(unittest.TestCase):

    def test_duplicate_rows(self):
        #
        # Check if the rows of products.csv are unique
        #
        df1 = pd.read_csv("products.csv")
        rows_duplicated = df1.duplicated()
        self.assertFalse(rows_duplicated.any(), "The products.csv contains duplicated rows.")
        
        return    
          
    def test_files_exist(self):
        #
        # Check if the 4 x csv files exist on local directory
        # and if either of them has 0 size
        #
        file1_exist = os.path.isfile("historical_orders.csv")
        file2_exist = os.path.isfile("subtotal.csv")
        file3_exist = os.path.isfile("products.csv")
        file4_exist = os.path.isfile("order_by_customer.csv")

        self.assertTrue(file1_exist and file2_exist and file3_exist and file4_exist, "At least 1 or more CSV files do not exist.")

        file1_size = os.path.getsize("historical_orders.csv")
        file2_size = os.path.getsize("subtotal.csv")
        file3_size = os.path.getsize("products.csv")
        file4_size = os.path.getsize("order_by_customer.csv")
        
        self.assertTrue(file1_size > 0 and file2_size > 0 and file3_size > 0 and file4_size >0, "At least 1 or more CSV files are empty.")

        return
    
    def test_compare_row_count(self):
        #
        # Compare the number of rows amongst order_by_customer, historical_orders and subtotal files
        # They should have the same number of rows
        #
        df1 = pd.read_csv("historical_orders.csv")
        df2 = pd.read_csv("subtotal.csv")
        df3 = pd.read_csv("order_by_customer.csv")

        self.assertEqual(df1.shape[0], df2.shape[0], "historical_orders and subtotal csv files do not have the same number of rows.")
        self.assertEqual(df1.shape[0], df3.shape[0], "historical_orders and order_by_customer cvs files do not have the same number of rows.")

        return
    
    def test_row_count_in_range(self):
        #
        # Check if the number of rows in the acceptable range
        # 1,000 orders * Avg(1,2,3) product_ids in each order by a customer 
        # average = 1,000 * 2 = 2,000 rows
        # assuming +-2% as acceptable range
        #
        min_no = 1960
        max_no = 2040

        df = pd.read_csv("order_by_customer.csv")

        row_no = df.shape[0]

        self.assertTrue(min_no <= row_no <= max_no, "order_by_customer.csv does not have acceptable number of rows")

        return
            
if __name__ == "__main__":
    unittest.main()
