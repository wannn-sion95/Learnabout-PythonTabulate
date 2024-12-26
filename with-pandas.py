# Import libraries
import pandas as pd
from tabulate import tabulate

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Anita", "Ridwan", "Rayna"],
    "Age": [18, 19, 18],
    "Profession": ["Engineer", "Data Scientist", "Programmer"]
})

# Displaying the DataFrame as a formatted table
table = tabulate(
    df, 
    headers='keys', 
    tablefmt='pipe'
)

print(table)
