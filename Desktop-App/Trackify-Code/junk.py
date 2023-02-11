import requests

data = requests.post(
    url='https://trackify.pangacomics.com/auth/jwt/create/',
    data={
        'email':'admin@gmail.com',
        'password':'admi'
    }
)
try:
    print(data.json()['access'])
except KeyError:
    print('Username or email incorrect')