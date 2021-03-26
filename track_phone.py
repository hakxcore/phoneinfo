#Code by Mukesh Kumar
#!/bin/bash
##   Author: Mukesh Kumar
##   Email: anonymous_mails_box@protonmail.ch
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier
number = input("Enter a phone number along with country code: ")
ch_number = phonenumbers.parse(number, "CH")
print("-------------------------------------")
print("    Phone-number:", number)
print("         Country:", geocoder.description_for_number(ch_number, "en"))
service_number = phonenumbers.parse(number, "RO")
print("Service-Provider:", carrier.name_for_number(service_number, "en"))
gb_number = phonenumbers.parse(number, "GB")
print("        TimeZone:", timezone.time_zones_for_number(gb_number))
parse_phone = phonenumbers.parse(number, None)
print("  Parsing_phn_no:", parse_phone)
is_possible_no = phonenumbers.is_possible_number(parse_phone)
print("     Is-Possible:", is_possible_no)
is_valid_no = phonenumbers.is_valid_number(parse_phone)
print("        Is Valid:", is_valid_no)
print("-------------------------------------")
