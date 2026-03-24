def city_country(city, country, population=None):
    if population is None:
        return f"{city.title()}, {country.title()}"
    else:
        return f"{city.title()}, {country.title()} - población {population}"
