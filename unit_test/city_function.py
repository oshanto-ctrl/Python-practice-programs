from itertools import count


def location(city_name, country_name, population = ''):
    """City name of a Country."""
    if population:
        user_loc = f"{city_name}, {country_name} - {population}"
    else:
        user_loc = f"{city_name}, {country_name}"
    return user_loc.title()