from datetime import datetime, timedelta


def display_current_datetime():
    """
    This function gets and displays the current date and time 
    in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it
    print(f"Current date and time: {formatted_date}")


def calculate_future_date(days):
    """
    This function calculates and displays the future date 
    after adding 'days' to today's date.
    """
    current_date = datetime.now()  # Get today's date
    future_date = current_date + timedelta(days=days)  # Add the number of days
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format it
    print(f"Future date: {formatted_future_date}")


def main():
    display_current_datetime()  # Show the current date and time

    try:
        # Ask user for number of days and convert to integer
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(number_of_days)  # Calculate and display future date
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")


if __name__ == "__main__":
    main()
