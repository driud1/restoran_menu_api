# def foo(a):
#     print(locals())
#     print(globals())
#     return a ** 5
#
#
# def bar(a, b):
#     print(locals())
#     print(globals())
#     return a - b
#
#
#
#
# def cycle():
#     print(locals())
#     print(globals())
#     for i in reversed(range(10)):
#         print(i)
#
#
# if __name__ == '__main__':
#     cycle()
#     foo(4)
#     spam = foo(2)
#     eggs = bar(4, 8)
#
#     print(spam, eggs)

import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q": "56.01,37.47518846248848"}

headers = {
    "X-RapidAPI-Key": "43037ce7a5msh82cc2fd7be32072p1e21d6jsn7c575fd5d00c",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
print(response.json()['location'])

# response.json() - из ответа создаем словарь, dict.items() - из словаря делаем список кортежей
d = response.json()
# for key, value in d.items():
for key, value in response.json().items():
    print(f"key = {key} : value = {value}")
    # пройдис ь по вложеным словарям