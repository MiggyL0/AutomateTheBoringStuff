#! python3

import re, pyperclip

#Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 413-333-1231, 444-1231, (123) 333-1231, 123-123-1231 ext 12312, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?        # area code optional
(\s|-)              # first Separator
\d\d\d              # first 3 digits
-                   # second separator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s)|x)   # extension word-part(optional)
(\d{2,5}))?         # extension numberpart(optional)
)

''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thine@something.com

[a-zA-Z0-9_.+]+            # name
@            # @ symbol
[a-zA-Z0-9_.+]            # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

#TODO: extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhonenumbers = []
for phoneNumber in extractedPhone:
    allPhonenumbers.append(phoneNumber[0])

print(allPhonenumbers)

#TODO: copy the extracted email/phone to the clipboard
results = '\n'.join(allPhonenumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)