import requests

# r = requests.get('https://skillbox.ru/media/code/chto-takoe-ipadres-i-maska-podseti-i-zachem-oni-nuzhny//')
# print(r)
# print(r.text)
# # print(r.content)
# # print(r.is_permanent_redirect)
# print(r.encoding)
# # for k, v in r.json():
# #     print(f"{k} : {v}")
#
#

req = requests.get("http://127.0.0.1:5467/api/v1/menus")
trq_text = req.text
req_text = requests.get("http://127.0.0.1:5467/api/v1/menus").text

print(requests.get("http://127.0.0.1:5467/api/v1/menus").text)

print(requests.get("http://127.0.0.1:5467/api/v1/menus").content)

print(requests.get("http://127.0.0.1:5467/api/v1/menus").status_code)

print(requests.get("http://127.0.0.1:5467/api/v1/menus").status_code == requests.codes.ok) #

print(requests.get("http://127.0.0.1:5467/api/v1/menus/1").status_code)

print(requests.get("http://127.0.0.1:5467/api/v1/menus/2").text)

print(requests.get("http://127.0.0.1:5467/api/v1/menus/3").text == requests.codes.ok)

print(requests.get("http://127.0.0.1:5467/api/v1/menus").json())

# dict = {i: ord(i) for i in map(chr, range(ord('a'), ord('z') + 1))}
# # print(dict)
# # dict["e"] = 90
# # print(dict)
# # for i in map(chr, range(ord('a'), ord('z') + 1)):
# #     dict[i] = ord(i)
# print(dict)

# import json
#
#
# print(json.dumps(dict))
# print(a_ind := ord("a"))
# print(chr(a_ind))

# print(chr, chr(98))


