#homework medicstore
#library
!uv add openpyxl
import pandas as pd

# Load the dataset
df_sales1 = pd.read_csv("../data/Sales_MedicStore_part1.csv",sep=";")
df_sales1

# Load the dataset
df_sales2 = pd.read_csv("../data/Sales_MedicStore_part2.csv",sep=";")
df_sales2

# Load the dataset
df_mapping = pd.read_excel("../data/Mapping.xlsx")
df_mapping

# Assemle the file Sales_Part1 and Sales_Part2 together into Sales
df_sales = pd.concat([df_sales1, df_sales2])
df_sales


#Verification of concatenation
df_sales1.shape
df_sales2.shape
df_sales.shape

# Merge the Sales dataset with the Mapping dataset
# First I will check the columns of both the cocat sales and the mapping dataset
df_sales.columns
df_mapping.columns

#Merge the two datasets on the column "Sub-Category"
df_merged = pd.merge(df_sales, df_mapping, left_on="Sub-Category", right_on="Sub-Category")
df_merged

#Verification of the merge
df_merged.shape
df_sales.shape
df_mapping.shape

#compute total sales
df_merged["Total Sales"] = df_merged["Quantity"] * df_merged["Unit Price"]
df_merged["Total Sales"]

totalsales=sum(df_merged["Total Sales"])

#column names in final dataset
df_merged.columns

#first 5 rows of the final dataset
df_merged.head(5)

#last 5 rows of the final dataset
df_merged.tail(5)

#statistical description of the final dataset
df_merged.describe()

#how many orders are in the final dataset
df_merged["Order ID"].describe()

#top 3 customers by number of orders
df_merged["Customer Name"].value_counts().head(3)

#sales of france
sales_france = sum(df_merged[df_merged["Country"] == "France"]["Total Sales"])

#comparison of sales of france with total sales
part_of_sales_france = (sales_france / totalsales) * 100
print(f"Sales of France: {sales_france} which is {part_of_sales_france:.2f}% of total sales.")
