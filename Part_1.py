# Variables
total_months = 0
total_rainfall = 0

# User enters number of years
years = int(input("Enter the number of years: "))

# Loop through each year
for year in range(1, years + 1):
    # Loop through each month
    for month in range(1, 13):
        # User enters rainfall in inches for that month
        rainfall = float(input(f"Enter the rainfall in inches for year {year}, month {month}: "))
        # Add the rainfall to the total
        total_rainfall += rainfall
        # Increment the number of months
        total_months += 1

# Calculate the average rainfall per month
average_rainfall = total_rainfall / total_months

# Display the results
print(f"The number of months is {total_months}")
print(f"The total inches of rainfall is {total_rainfall}")
print(f"The average rainfall per month is {average_rainfall}")

input("Press enter to exit")
