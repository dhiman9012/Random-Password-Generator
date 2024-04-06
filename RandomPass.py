import random
import string

pass_length=12
charVal=string.ascii_letters+ string.digits + string.punctuation

password=" "
for i in range(pass_length):
  password+=random.choice(charVal)

print("your random password is:",password)