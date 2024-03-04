import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

password = ""

req_letters = int(input('How much letters do you want in your password: '))
req_digits =  int(input('How much digits do you want in your password: '))
req_special = int(input('How much special characters do you want in your password: '))


for i in range(1, req_letters+1):
    n_letters = random.choice(letters)
    password += n_letters

for i in range(1, req_digits+1):
    n_digits = random.choice(digits)
    password += n_digits

for i in range(1, req_special+1):
    n_symbols = random.choice(symbols)
    password += n_symbols

passw_list = list(password)
random.shuffle(passw_list)

shuffled_password = ''.join(passw_list)
print(shuffled_password)