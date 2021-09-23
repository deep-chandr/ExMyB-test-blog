# create user

from django.contrib.auth.models import User
import random
import string


for i in range(10):
    name = random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
    obj = {
        'username': name,
        'email' : '{}@gmail.com'.format(name),
        'password': name
    } 
    User.objects.create(**obj)


