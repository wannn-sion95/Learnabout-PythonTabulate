from tabulate import tabulate

# Sample data: list of lists
data = [
    ["Anita", 18, "Rp.3.000.000"],
    ["Ridwan", 19, "Rp.4.350.075"],
    ["Rayna", 18, "Rp.5.250.000"]
]

# Customizing table appearance
table = tabulate(
    data,
    headers=["Name", "Age", "Salary"],
    tablefmt="fancy_grid",
    numalign="right",
    stralign="center",
    colalign=("center", "center", "right")
)

print(table)
