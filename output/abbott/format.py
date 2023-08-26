import pandas as pd
from bs4 import BeautifulSoup
import re


file_1 = pd.read_excel("abbott.xlsx")

body_html = []
exp_date = []
expiry_date = []
empty_cont = ""
a = 0
for x in file_1["body_html"]:
    body_html.append(BeautifulSoup(x, "html.parser"))


for x in body_html:
    abcd = x.findAll("span")
    for x in abcd:
        ab = x.find(style="color: #1e2e7d;")
        print(ab)


# print(a)
# def extractor(a, b):
#     # return (p for p in b if a in b.get_text())
#     return [p for p in b if a in b.get_text()]


# # print(body_html)


# for x in body_html:
#     abcd = x.find("p")
#     empty_cont = extractor("Expiry Date", abcd)
#     exp_date.append(empty_cont)
#     # print(empty_cont)


# # print(len(exp_date))

# for x in exp_date:
#     abcdef = re.findall('[0-9]+', str(x))
#     print(abcdef)

# for x in exp_date:
#     try:
#         expiry_date.append(next(x))
#     except:
#         StopIteration


# for x in expiry_date:
#     print(x.get_text())

# print(type(empty_cont))

# print(a)
# print(len(expiry_date))

# for x in expiry_date:
#     print(x)
