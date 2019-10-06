import re
import pyperclip

# phoneAndemail.py - Finds phone numbers and email addresses on the clipboard.

a_string = str(pyperclip.paste())


# regex1 finds phone numbers in a string

def get_phonenums():
    # Create phone number regex
    phoneregex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              #area code
        (\s|-|\.)?                      # separator
        (\d{3})                         # first three digits
        (\s|-|\.)                       # separator
        (\d{4})                         # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
        )''', re.VERBOSE)
    matches = []
    for group in phoneregex.findall(a_string):
        phone = '-'.join([group[1], group[3], group[5]])
        if group[8] != '':
            phone += ' ext' + group[8]
        matches.append(phone)

    if len(matches) > 0:
        phonenumbers = '\n'.join(matches)
        pyperclip.copy(phonenumbers)
        tmp_list = ['Phone numbers copied to clipboard: ',
                      str(len(matches)), '\n', phonenumbers, '\n']
        print(''.join(tmp_list))
    else:
        print("No phone numbers found.")


def get_emailaddresses():
    emailregex = re.compile(r'''(
        ([a-zA-Z0-9._%+-]+          # username
        @                           # @ symbol
        [a-zA-Z0-9.-]+              # email provider
        \.[a-zA_Z]{2,4})            # website extension (like .com etc)
        )''', re.VERBOSE)
    matches = []
    for group in emailregex.findall(a_string):
        email = group[0]
        matches.append(email)
    # TODO: Find matches in clipboard text.
    # TODO: Copy results to the clipboard.

    if len(matches) > 0:
        emailaddresses = '\n'.join(matches)
        pyperclip.copy(emailaddresses)
        tmp_list = ['Emails copied to clipboard: ',
                    str(len(matches)), '\n', emailaddresses, '\n']
        print(''.join(tmp_list))
    else:
        print("No email addresses found.")


get_phonenums()
get_emailaddresses()
