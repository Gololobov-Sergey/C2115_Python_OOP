import requests

# response = requests.get("https://coinmarketcap.com/")
# #print(response.text)
#
# coin_list = []
#
# response_parse = response.text.split("<span>")
# for parse_elem in response_parse:
#     if parse_elem.startswith("$"):
#         for elem in parse_elem.split("</span>"):
#             if elem.startswith("$"):
#                 coin_list.append(float(elem.split("$")[1].replace(",", "")))
#
# btc = coin_list[0]
# print(btc)


from bs4 import BeautifulSoup

response = requests.get("https://coinmarketcap.com/currencies/hamster-kombat/")
soup = BeautifulSoup(response.text, features="html.parser")
soup_list = soup.find_all("span", {"class", "sc-65e7f566-0 WXGwg base-text"})
res = str(soup_list[0]).split(">")
print("Hamster Kombat -", res[1].split("<")[0])


