
import random

MAXIMUM_SILK = 1000
LOW_SILK_THRESHOLD = 200


def main():
    """Menu-driven game to create cities, generate tax, and lose cities depending on trade."""
    print("Welcome to the Medieval Silk Game.\n"
          "You can create new cities with the tax your empire generates.\n"
          "Cities cost and generate tax according to their name length.\n"
          "For example, Venice would cost 6 ducats.\n"
          "Trade brings in up to 10000 bolts of silk per year.\n"
          "If trade is less than 200 bolts, a city loses its independence.\n"
          "You start with these cities: Lucca, Treviso, Turin, Vercelli. \n\n")
    print("You start with these cities: \n"
          "Lucca, Treviso, Turin, Vercelli,\n"
          "After 0 years, you have 4 cities and your treasury has 0 ducats.")
    print(f"(W)ait\n"
          f"(D)isplay cities\n"
          f"(A)dd new city\n"
          f"(Q)uit")
    cities = ["Lucca", "Treviso", "Turin", "Vercelli"]
    number_of_years = 0
    number_of_ducats = 0
    choice = input("Choose:").upper()
    while choice != "Q":
        if choice == "W":
            number_of_years += 1  # increase the year by 1
            if len(cities) == 1:
                collapsed_city = delete_list_item(cities)
                print(f"Sadly, your city of {collapsed_city} has collapsed")
            else:
                # Display rainfall
                for i in range(4):
                    print("----")

                silk_traded = random.randint(0, MAXIMUM_SILK)
                if silk_traded > LOW_SILK_THRESHOLD:
                    print("This year the amount of silk traded was", silk_traded)
                    for city in cities:
                        tax_generated = calculate_tax(silk_traded, city)   # Calculate ducats you earn from each city
                        number_of_ducats = number_of_ducats + tax_generated  # Update the number of ducats
                        print(city, "earned", tax_generated, ",", end="")
                else:
                    print("This year the amount of silk traded was", silk_traded)

                    # Remove random item from the list.
                    conquered_city = delete_list_item(cities)
                    print("Sadly, your city of", conquered_city, "has collapsed")
        elif choice == "D":
            display_cities(cities)
        elif choice == "A":
            city_name = get_valid_name()
            while city_name in cities:
                print("City already in the list. Choose another name")
                city_name = get_valid_name()
            if number_of_ducats > len(city_name):
                cities.append(city_name)
                number_of_ducats = number_of_ducats - len(city_name)
            else:
                print("You can't afford", city_name)

        else:
            print("Invalid Choice")

        print("\nAfter", number_of_years, " years, you have", len(cities), "cities and your treasury has",
              number_of_ducats, "ducats")
        print(f"(W)ait\n"
              f"(D)isplay cities\n"
              f"(A)dd new city\n"
              f"(Q)uit")
        choice = input("Choose:").upper()
    if len(cities) > 0:

        print(f"You finished with these cities:\n {','.join(cities)},\n After {number_of_years} years, you have {len(cities)}"
              f" cities and your treasury has {number_of_ducats} ducats.\n Thank you for playing the Medieval Silk "
              f"Game :)")
    else:
        print(f"You finished with no cities:\n After {number_of_years} years, you have 0 cities,"
              f" and your treasury has {number_of_ducats} ducats.\n Thank you for playing the Medieval Silk Game :)")


def display_cities(cities):
    """Display cities"""
    print(','.join(cities))


def get_valid_name():
    """Get a valid name"""
    name = input("City Name:").title()
    while name == "":
        print("Invalid input")
        name = input("City Name:").title
    return name


def calculate_tax(silk_traded, city):
    """Calculate tax and return tax as an integer"""
    value = (silk_traded / 1000) / 2
    value_2 = (silk_traded / 1000)
    original_tax = random.uniform(value, value_2) * len(city)
    good_tax = int(original_tax)
    return good_tax


def delete_list_item(cities):
    """Delete first item in a list and return deleted item"""
    deleted_city = cities.pop(0)
    return deleted_city


main()
