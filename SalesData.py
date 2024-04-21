import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
class SalesData:
    def __init__(self, data=None):

        self.data = data

        """------------------------------Task-2--------------------------"""
    def read_csv(self, file_path: str):
        try:
            # Use Pandas to read CSV file
            self.data = pd.read_csv(file_path)
            return self.data
        except Exception as e:
            print("Error, sorry...")
            return None

    def eliminate_duplicates(self):

        try:
            self.data = self.data.drop_duplicates().reset_index(drop=True)

        except Exception as e:
            print("Error, sorry...")

    def calculate_total_sales(self):

        try:
            total_sales = self.data.groupby('Product')['Total'].sum().reset_index()
            return total_sales
        except Exception as e:
            print(f"Error calculating total sales: {e}")
            return None

    def _calculate_total_sales_per_month(self):

        try:
            self.data['Date'] = pd.to_datetime(self.data['Date'], format='%d.%m.%Y', errors='coerce')
            # Convert 'Date' column to datetime for grouping by month
            self.data['Date'] = pd.to_datetime(self.data['Date'])
            total_sales_per_month = self.data.groupby(self.data['Date'].dt.month)['Total'].sum().reset_index()
            print("----------------------------------------------------------------")

            plt.plot(total_sales_per_month['Date'], total_sales_per_month['Total'])
            plt.title('Total Sales per Month')
            plt.xlabel('Month')
            plt.ylabel('Total Sales')
            plt.show()
            return total_sales_per_month
        except Exception as e:
            print(f"Error calculating total sales per month: {e}")
            return None

    def _identify_best_selling_product(self):

        try:
            best_selling_product = self.data.groupby('Product')['Total'].sum().idxmax()
            return best_selling_product
        except Exception as e:
            print(f" {e}")
            return None

    def _identify_month_with_highest_sales(self):
        try:
            self.data['Date'] = pd.to_datetime(self.data['Date'])
            month_with_highest_sales = self.data.groupby(self.data['Date'].dt.month)['Total'].sum().idxmax()
            return month_with_highest_sales
        except Exception as e:
            print( f"{e}")

            return None

    def analyze_sales_data(self):
        try:
            best_selling_product = self._identify_best_selling_product()
            month_with_highest_sales = self._identify_month_with_highest_sales()
            analysis_results = {
                'best_selling_product': best_selling_product,
                'month_with_highest_sales': month_with_highest_sales
            }

            return analysis_results
        except Exception as e:
            print(f"Error analyzing sales data: {e}")
            return None

    def add_to_dictionary(self):

        try:
            minimest_selling_product = self.data.groupby('Product')['Total'].sum().idxmin()
            average_sales_for_all_months = self.data['Total'].mean()

            extended_results = self.analyze_sales_data()
            extended_results.update({
                'minimest_selling_product': minimest_selling_product,
                'average_sales_for_all_months': average_sales_for_all_months
            })

            return extended_results
        except Exception as e:
            print(f"Error performing additional analysis: {e}")
            return None
        """------------------------------Task-3--------------------------"""

    def calculate_cumulative_sales(self):

            try:
                #הפונקציה הזאת מוסיפה עמודה חדשה לטבלה!!!

                self.data['CumulativeSales'] = self.data.groupby('Product')['Total'].cumsum()
                print("Was done successfully.")
            except Exception as e:
                print(f" {e}")

    def add_90_percent_values_column(self):

            try:
                self.data['90PercentValues'] = self.data['Quantity'].quantile(0.9)
                print("90% values column added successfully.")
            except Exception as e:
                print(f"Error adding 90% values column: {e}")

    def bar_chart_category_sum(self):

            try:
                plt.figure(figsize=(10, 6))
                sns.barplot(x='Product', y='Quantity', data=self.data, estimator=np.sum)
                plt.title("Sum of Quantities Sold for Each Product")
                plt.xticks(rotation=45, ha='right')
                # plt.show()
            except Exception as e:
                print(f"Error plotting bar chart: {e}")

    def calculate_mean_quantity(self):

            try:
                total_values = self.data['Total'].values
                mean_value = np.mean(total_values)
                median_value = np.median(total_values)
                second_max_value = np.partition(total_values, -2)[-2]

                print(f"Mean: {mean_value}, Median: {median_value}, Second Max: {second_max_value}")
            except Exception as e:
                print(f"Error calculating mean, median, and second max: {e}")

    def filter_by_sellings_or_and(self):

            try:
                condition1 = (self.data['Quantity'] > 5) | (self.data['Quantity'] == 0)
                condition2 = (self.data['Price'] > 300) & (self.data['Quantity'] < 2)

                filtered_data = self.data[condition1 | condition2]
                print("Filtered data based on sellings conditions:")
                print(filtered_data)
            except Exception as e:
                print(f"Error filtering data by sellings conditions: {e}")

    def divide_by_2(self):

        try:
            # Identify numeric columns
            numeric_columns = self.data.select_dtypes(include=[np.number]).columns

            # Divide only numeric columns by 2 for "BLACK FRIDAY"
            self.data.loc[:, numeric_columns] /= 2
            self.data.rename(columns=lambda col: f"BlackFriday{col}", inplace=True)

            print("Values divided by 2 for 'BLACK FRIDAY' successfully.")
        except Exception as e:
            print(f"Error dividing values for 'BLACK FRIDAY': {e}")

    def calculate_stats(self, columns=None):


            try:
                if columns is None:
                    columns = self.data.columns

                for col in columns:
                    max_value = self.data[col].max()
                    sum_value = self.data[col].sum()
                    abs_values = np.abs(self.data[col])
                    cum_max_value = np.maximum.accumulate(self.data[col])

                    print(f"Column: {col}")
                    print(f"Maximum: {max_value}")
                    print(f"Sum: {sum_value}")
                    print(f"Absolute Values: {abs_values}")
                    print(f"Cumulative Maximum: {cum_max_value}")
                    print("------------------------")
            except Exception as e:
                print(f"Error calculating stats: {e}")


    #משימות 4-5 הן רשות!!!!!!!!!!!!!!!!!!!!!!!!!! כי אפשר לבחור 12 רשויות-------------------------
   # משימה 7 שאלה 3


    def number_game_promotions(self, product_name: str):
        try:

            sales_numbers = self.data[self.data['Product'] == product_name]['Quantity'].tolist()
            highest_paid_number = max(sales_numbers)


            promotion_range = range(highest_paid_number - 5, highest_paid_number + 6)

            print(f"Promotion Range for {product_name}: {promotion_range}")
        except Exception as e:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            error_message = f"{current_time}> Error type: {str(e)} >"
            print(error_message)

        #משימה 7 שאלות 6-7
        def print_(self):
            print("First 3 rows:")
            print(self.data.head(3))

            print("\nLast 2 rows:")
            print(sales_data.tail(2))

            print("\nRandom row:")
            print(sales_data.iloc[0])
            print("\nLoop through numeric values:")
            for col in self.data.select_dtypes(include=[float, int]):
                for value in self.data[col]:
                    print(value)

sales_data = SalesData()

# Read data from the CSV file (replace with your file path)
sales_data.read_csv(r"C:\Users\user1\OneDrive\Desktop\YafeNof.csv")

print("------------------------------Task-3--------------------------")

# # Example to test the SalesData class
# sales_data.calculate_cumulative_sales()
# print(sales_data.data.head())
#
# # Check the 'CumulativeSales' column
# print(sales_data.data['CumulativeSales'])
#
# # Add 90% values column
# sales_data.add_90_percent_values_column()
# print("PLT_-------------------------------------------")
# # Plot bar chart for category sum
# # sales_data.bar_chart_category_sum()
#
# # Calculate mean, median, and second max for Total column
# sales_data.calculate_mean_quantity()
#
# # Filter by sellings conditions
# sales_data.filter_by_sellings_or_and()
#
# # Divide values by 2 for "BLACK FRIDAY"
# sales_data.divide_by_2()
#
# # Calculate stats for all columns
# sales_data.calculate_stats()
#בדיקה האם 2 עבד-----------------------------------------------------------
# # Display the original data
# print("Original Data:")
# print(sales_data.data)
#
# # Eliminate duplicates
# sales_data.eliminate_duplicates()
#
# # Display the cleaned data
# print("\nCleaned Data:")
# print(sales_data.data)
#
# # Calculate total sales for each product
# total_sales_per_product = sales_data.calculate_total_sales()
# print("\nTotal Sales per Product:")
# print(total_sales_per_product)
#
# Calculate total sales per month
total_sales_per_month = sales_data._calculate_total_sales_per_month()
print("\nTotal Sales per Month:")
print(total_sales_per_month)
#
# # Identify the best-selling product
# best_selling_product = sales_data._identify_best_selling_product()
# print("\nBest Selling Product:")
# print(best_selling_product)
#
# # Identify the month with the highest total sales
# month_with_highest_sales = sales_data._identify_month_with_highest_sales()
# print("\nMonth with Highest Sales:")
# print(month_with_highest_sales)
#
# # Perform overall analysis
# overall_analysis = sales_data.analyze_sales_data()
# print("\nOverall Analysis:")
# print(overall_analysis)
#
# # Perform additional analysis
# additional_analysis = sales_data.add_to_dictionary()
# print("\nAdditional Analysis:")
# print(additional_analysis)

