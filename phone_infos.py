import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number = input("Enter your number with +__: ")

# PARSING STRING TO PHONE NUMBER
phone = phonenumbers.parse(number)

# GETTING TIMEZONE
time = timezone.time_zones_for_number(phone)

# GETTING CARRIER
car = carrier.name_for_number(phone,"en")

# GETTING REGION
reg = geocoder.description_for_number(phone,"en")

print(phone)
print(time)
print(car)
print(reg)