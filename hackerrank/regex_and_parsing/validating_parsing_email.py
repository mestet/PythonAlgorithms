import email.utils as eml
import re


def print_if_valid_email(text):
    pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'

    parsed_email = eml.parseaddr(text)
    if parsed_email != ('', ''):
        if bool(re.match(pattern, parsed_email[1])):
            print(f'{parsed_email[0]} <{parsed_email[1]}>')


# tests = [input() for _ in range(int(input()))]
tests = [
    'DEXTER <dexter@hotmail.com>',
    'VIRUS <virus!@variable.:p>',
    'vin <vineet@>',
    'vineet <vineet@gmail.com>',
    'vineet <vineet@gma.il.co.m>',
    'vineet <vineet@gma-il.co-m>',
    'vineet <vineet@gma,il.co@m>',
    'vineet <vineet@gmail,com>',
    'vineet <.vin@gmail.com>',
    'vineet <vin-nii@gmail.com>',
    'vineet <v__i_n-n_ii@gmail.com>',
    'shashank <shashank@9mail.com>',
    'shashank <shashank@gmail.9om>',
    'shashank <shashank@gma_il.com>',
    'shashank <shashank@mail.moc>',
    'shashank <shashank@company-mail.com>',
    'shashank <shashank@companymail.c_o>'
]
for t in tests:
    print_if_valid_email(t)
