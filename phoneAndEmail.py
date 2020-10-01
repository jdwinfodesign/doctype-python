#! python3

import re, pyperclip

#print('Hello, world!')

# Create a regex for phone numbers

#((/d/d/d)|(\(\d\d\d\)))?    #area code (optional)
phoneRegex = re.compile(r'''

(
((\d\d\d)|(\(\d\d\d\)))    #area code (optional)
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    #last 4 digits
(((ext(\.)?\s)|x)           # extension characters (optional)
(\d{2,5}))?                 # extension number (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-Z0-9_.+]+    # name
@                  # @ symbol
[a-zA-Z0-9_.+]+    #domain name

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email and phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email and phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
print(results)
