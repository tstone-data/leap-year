
# Number of days per month. First value placeholder for indexing purposes
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# List of month names
month_names = ['', 'January', 'February', 'March', 'April', 'May',
'June', 'July', 'August', 'September', 'October', 'November', 'December']

def is_leap(year):
    """Return True if a leap year, False in non-leap year"""
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

def month_converter(month):
    """Converts user input from number to month name"""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    else:
        return month_names[month]

def days_in_month(year, month):
    """Return number of days in that month in that year"""
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29
    else:
        return days[month]


# Welcome user to the platform
print("Welcome to the Leap Year Determiner!")

# Ask for year input from the user
year = input("Input the year you're interested in: ")
year = int(year)

# Return leap year determination
if is_leap(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

# Introduce user to next section of platform
print("Now let's determine how many days are in a particular month that year!")

# Prompt user for how many days in month that year
month = input("Input the month you're interested in: ")
month = int(month)

# Get the number of days in the specified month
num_days = days_in_month(year, month)
month_name = month_converter(month)

# Return number of days in month for that particular year
if num_days == 'Invalid Month':
    print(num_days)
else:
    print(f"In the year {year}, {month_name} has {num_days} days")
