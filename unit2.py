import re
"""
Given a text file file.txt that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.
"""
# regular expression to find phone number in formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)
re_phone = re.compile('^((\([0-9]{3}\)) |([0-9]{3}\-))[0-9]{3}\-[0-9]{4}$')
# read file file.txt
with open("file.txt") as f:
    #read file line by line
    list_number = f.readlines()
    for phone_number in list_number:
        # if the phone_number is in the formats, then print it
        if re.match(re_phone, phone_number.strip()):
            print(phone_number.strip())
