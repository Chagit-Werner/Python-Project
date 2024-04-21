from SalesData import SalesData

if __name__ == "__main__":
    sales_data = SalesData()

    # Read data from the CSV file (replace with your file path)
    sales_data.read_csv(r"C:\Users\user1\OneDrive\Desktop\YafeNof.csv")

    print("------------------------------Task-3--------------------------")

    # Example to test the SalesData class
    sales_data.calculate_cumulative_sales()
    print(sales_data.data.head())

    # Check the 'CumulativeSales' column
    print(sales_data.data['CumulativeSales'])

    # Add 90% values column
    sales_data.add_90_percent_values_column()
    print("PLT_-------------------------------------------")
    # Plot bar chart for category sum
    # sales_data.bar_chart_category_sum()

    # Calculate mean, median, and second max for Total column
    sales_data.calculate_mean_quantity()

    # Filter by sellings conditions
    sales_data.filter_by_sellings_or_and()

    # Divide values by 2 for "BLACK FRIDAY"
    sales_data.divide_by_2()

    # Calculate stats for all columns
    sales_data.calculate_stats()
