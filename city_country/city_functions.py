def show_locations(city, country, population=0):
    """ Function that accepts two parameters: a city name and a country name. The function
    should return a single string of the form City, Country, such as Santiago, Chile.

    Modify your function so it requires a third parameter, population. It should now return
    a single string of the form City, Country – population xxx, such as Santiago, Chile – population 5000000.
    """
    if population:
        full_form = f"{city.title()}, {country.title()} - population {int(population)}"

    else:
        full_form = f"{city.title()}, {country.title()}"

    return full_form
