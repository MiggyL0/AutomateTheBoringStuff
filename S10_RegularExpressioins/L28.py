import re

re.compile(r'''
\d\d\d    # Area Code
-         # First Dash
\d\d\d    # First 3 Digits
-         # Second Dash
\d\d\d\d''', re.VERBOSE)
