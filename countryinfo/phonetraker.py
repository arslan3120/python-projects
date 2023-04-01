import phonenumbers
from phonenumbers import carrier, geocoder, timezone


mobileNo = input("mobile no: ")
mobileNo = phonenumbers.parse(mobileNo)
print(timezone.time_zones_for_number(mobileNo))
print(carrier.name_for_number(mobileNo, "en"))
print(geocoder.description_for_number(mobileNo, "en"))
print("Valid Mobile Numer:", phonenumbers.is_valid_number(mobileNo))
print("checking possibility of number:", phonenumbers.is_possible_number(mobileNo))

