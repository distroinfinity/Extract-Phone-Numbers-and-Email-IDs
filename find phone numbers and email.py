#! python3

import re, pyperclip 

#TODO: CREATE A REGEX FOR PHONE NUMBERS
phoneregex = re.compile(r''' 
# 415-555-0000 ,555-0000 ,(415) 555-0000, 555-0000,, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?       #area code (optional)
(\s|-)                          # fisrt separator
\d\d\d                          # first three digits
-                               #separatpr
\d\d\d\d                        #last 4 digits
(((ext(\.)?\s)|x)               #extension part (optional)
(\d{2,5}))?                     #extension numberpart (optional)
)
''',re.VERBOSE)
#TODO: CREATE A REGEX FOR EMAIL ADDRESSES
emailregex = re.compile(r'''
#some.+_ thing@something.com

[a-zA-Z0-9_.+]+     #name part
@[a-zA-Z0-9_.+]+    # @symbol
        #domain name part
''',re.VERBOSE)
#TODO: GET THE TEXT OFF THE CLIPBOARD
text = pyperclip.paste()
#TODO: EXTRACT THE EMAIL/PHONE
extractedphone = phoneregex.findall(text)
extractedemail = emailregex.findall(text)
allphonenum = []
for i in extractedphone:
    allphonenum.append(i[0])

# print(allphonenum)
# print(extractedemail)
#TODO: copy the extracted email/phone to the clipboard.
result =  '\n'.join(allphonenum) + '\n''\n'.join(extractedemail)
pyperclip.copy(result)
