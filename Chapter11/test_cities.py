from pratice_11_1 import cityAndCountry
from pratice_11_2 import city_country_population
def test_city_country():
    city_country = cityAndCountry('santiago','chile')
    assert city_country == 'Santiago Chile'

def test_city_country_population():
    city_country_population_result = city_country_population('santiago','chile','5000000')
    assert city_country_population_result == "Santiago Chile - Population 5000000"