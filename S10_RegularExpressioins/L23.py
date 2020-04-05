import re
message = 'Call me at 111-222-3333 tomorrow, or at 415-234-2342'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.search(message))