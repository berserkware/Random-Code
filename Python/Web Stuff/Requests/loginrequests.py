import requests

payload = {
    "login" : "berserkware",
    "password" : "nothing"
}

with requests.Session() as s:
    p = s.post('https://github.com/login', data=payload)

    r = s.get('https://github.com')
    print(r.text)