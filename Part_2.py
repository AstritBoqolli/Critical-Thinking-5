# Variables
books = 0
points = 0

# Do while loop
while True:
    # User enters the number of books
    books = float(input("Enter the number of books that you have purchased this month: "))

    # Check if the input is positive
    if books > 0:
        # Check the number of books and assign the corresponding points
        if books // 2 == 0:
            points = 0
        elif books // 2 == 1:
            points = 5
        elif books // 2 == 2:
            points = 15
        elif books // 2 == 3:
            points = 30
        elif books // 2 >= 4:
            points = 60

        # Display the number of points awarded
        print(f"You have earned {points} points.")
    else:
        # If the input is not positive, display an error message and continue the loop
        print("Invalid number of books. Please enter a positive number.")
        continue

    # Break out of the loop when the number of books is valid
    break

input("Press enter to exit")
