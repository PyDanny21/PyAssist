import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input('Enter number with +__:')
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_numbers(phone)
car=carrier.name_for_number(phone,'en')
reg=geocoder.description_for_number(phone,'en')
print(car)
print(reg)
