from countryinfo import CountryInfo


count = input("enter your country name:  ")
country = CountryInfo(count)
print("Capital: ", country.capital())
print("Currencies is : ", country.currencies())