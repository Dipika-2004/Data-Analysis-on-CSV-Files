import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
df = pd.read_csv('sales_data.csv')

# Group and aggregate sales per product
grouped = df.groupby('Product')['Sales'].sum()

# Plot the results
grouped.plot(kind='bar', 
             title='Total Sales per Product', 
             xlabel='Product', 
             ylabel='Total Sales', 
             colormap='plasma',
             rot=45)  # Rotate x-axis labels if product names are long

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()