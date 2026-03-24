from city_functions import city_country
def test_city_country():
    resultado = city_country('santiago', 'chile', population=5000000)
    assert resultado == 'Santiago, Chile - población 5000000'