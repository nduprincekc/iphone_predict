number = '+2348120026592'

import phonenumbers

from phonenumbers import geodata, geocoder, carrier

ch = phonenumbers.parse(number, 'eH')
print(geocoder.description_for_number(ch, 'en'))


service_name = phonenumbers.parse(number,'we')

print(carrier.name_for_number(service_name, 'ru'))
