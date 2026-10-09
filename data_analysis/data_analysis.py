# Life Expectancy Analysis
# This program reads life expectancy data from a CSV file
# and finds the highest and lowest life expectancy values.
# For creativity, I added a feature that allows users to search for a
# country and view its minimum, maximum, and average life expectancy.

print("Welcome to the Life Expectancy Data Analysis Program!")

# Ask the user for a year
year_of_interest = input("\nEnter the year of interest: ")

# Variables for overall life expectancy
highest_expectancy = float("-inf")
lowest_expectancy = float("inf")

highest_country = ""
lowest_country = ""

highest_year = ""
lowest_year = ""

# Variables for the selected year
year_total = 0
year_count = 0

year_highest = float("-inf")
year_lowest = float("inf")

year_highest_country = ""
year_lowest_country = ""

# Dictionary to store country life expectancy values
country_data = {}

# Open and read the CSV file
with open("life-expectancy.csv") as file:

    next(file)

    for line in file:

        data = line.strip().split(",")

        entity = data[0]
        code = data[1]
        year = data[2]
        life_expectancy = float(data[3])

        # Find overall highest life expectancy
        if life_expectancy > highest_expectancy:

            highest_expectancy = life_expectancy
            highest_country = entity
            highest_year = year

        # Find overall lowest life expectancy
        if life_expectancy < lowest_expectancy:

            lowest_expectancy = life_expectancy
            lowest_country = entity
            lowest_year = year

        # Calculate statistics for the selected year
        if year == year_of_interest:

            year_total += life_expectancy
            year_count += 1

            # Highest life expectancy for selected year
            if life_expectancy > year_highest:

                year_highest = life_expectancy
                year_highest_country = entity

            # Lowest life expectancy for selected year
            if life_expectancy < year_lowest:

                year_lowest = life_expectancy
                year_lowest_country = entity

        # Store life expectancy values for each country
        if entity not in country_data:

            country_data[entity] = []

        country_data[entity].append(life_expectancy)


# Display overall results
print(f"\nThe overall max life expectancy is: {highest_expectancy} from {highest_country} in {highest_year}")

print(f"The overall min life expectancy is: {lowest_expectancy} from {lowest_country} in {lowest_year}")


# Display results for selected year
if year_count > 0:

    year_average = year_total / year_count

    print(f"\nFor the year {year_of_interest}:")

    print(f"The average life expectancy across all countries was {year_average:.2f}")

    print(f"The max life expectancy was in {year_highest_country} with {year_highest}")

    print(f"The min life expectancy was in {year_lowest_country} with {year_lowest}")

else:

    print(f"\nSorry, no data was found for the year {year_of_interest}.")


# EXTRA FEATURE: Country Life Expectancy Search

print("\n--- COUNTRY LIFE EXPECTANCY SEARCH ---")

country_search = input("Enter a country to explore: ").strip()

# Search without worrying about uppercase or lowercase
found_country = ""

for country in country_data:

    if country.lower() == country_search.lower():

        found_country = country
        break


if found_country != "":

    country_values = country_data[found_country]

    country_min = min(country_values)
    country_max = max(country_values)
    country_average = sum(country_values) / len(country_values)

    print(f"\nLife Expectancy Statistics for {found_country}:")

    print(f"Minimum life expectancy: {country_min:.2f}")
    print(f"Maximum life expectancy: {country_max:.2f}")
    print(f"Average life expectancy: {country_average:.2f}")

else:

    print(f"\nSorry, no data was found for '{country_search}'.")


print("\nThank you for using the Life Expectancy Data Analysis Program!")