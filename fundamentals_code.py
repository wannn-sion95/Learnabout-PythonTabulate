# Import the tabulate module
from tabulate import tabulate

# Sample data: list of lists
data = [
   ["Wannn Sion", 18, "Programmer, Computer Science"],
    ["Ridwan", 19, "Telecommunication Engineering"],
    ["Rayna", 18, "Informatics Engineering"]
]

# Creating a table with headers and a grid format
table = tabulate(
    data, 
    headers=["Name", "Age", "Profession"], 
    tablefmt="orgtbl"
)

print(table)# Import the tabulate module
