import os
import glob
import pandas as pd
import requests
import json
import re
from time import sleep

# All Variables
addon = ".json"
file_names_container = []
str1 = 'c:/Users/Yeshwanth/Desktop/uyyaala to kidsfud products/milk_formulas/'
json_container = []
data_list = []
pattern1 = r'data-mce-fragment="1"'
pattern2 = r'data-mce-style="color: #([a-zA-z0-9]{6});"'
keys_to_check = {'title', 'body_html', 'vendor',
                 'product_type', 'handle'}


# Path to the directory containing the .xlsx files
directory = os.getcwd()

# Get a list of all .xlsx files in the directory
xlsx_files = glob.glob(os.path.join(directory, '*.xlsx'))

excel_data = []

brand_names = []


def append_data(a):
    return excel_data.append(a)


def create_data(a: str) -> list:
    b = a
    urls = pd.read_excel(b)
    for x in urls['urls']:
        append_data(x)


for x in xlsx_files:
    create_data(x)

addon = '.json'


def url_alterator(x):
    """
    Adds the '.json' extension to the given URL.

    Args:
        x: URL string.

    Returns:
        str: URL with '.json' extension.
    """
    container = x + addon
    return container


# print(len(excel_data))

for x, y in enumerate(excel_data):
    abcd = url_alterator(y)
    excel_data[x] = abcd

# print(len(excel_data))

# for x in excel_data:
#     print(x)


def cleanser(val: str, pattern1: str, pattern2: str) -> str:
    """
    Cleanses the given string.

    Args:
        val (str): String to be cleaned.

    Returns:
        str: Cleaned string.
    """
    container = re.sub(pattern1, "", val)
    container = re.sub(pattern2, "", container)
    return container


def create_names(a: list) -> str:
    if "cow&gate" in a:
        strs = a.replace("cow&gate", "cow_gate")
        b = strs[len(str1):-5]
    else:
        b = a[len(str1):-5]

    c = f"{b}_extracted_data"
    return c


# get all .xlsx files and store there names in a list
for x in xlsx_files:
    file_names_container.append(create_names(x))

# for x in file_names_container:
#     print(x)

for x in file_names_container:
    abcd = x.split("_")[0]

    brand_names.append(abcd)

# for x in brand_names:
#     print(x)


def get_data(a):
    response = requests.get(a)
    result = response.json()
    return result


# for x in range(11):
#     a = brand_names[0]
#     b = excel_data[x]
#     if a in b:
#         print(a, b)

value_holder = []


def creator(x: list) -> list:
    for dict_items in x:
        for value in dict_items.values():
            for key, value in value.items():
                if key in keys_to_check:
                    data_list.append(
                        {key: cleanser(value, pattern1, pattern2)})
    return data_list


def bundler(x, y):
    output_path = directory + "/output/" + y
    df = pd.DataFrame(x)
    # df.to_excel(f"{output_path}.xlsx")
    df.to_excel(f"{output_path}.xlsx")


def runner(a, b):
    for x in range(len(excel_data)):
        bad = a
        if bad in excel_data[x]:
            value_holder.append(get_data(excel_data[x]))

    abcd = creator(value_holder)
    bund = bundler(abcd, b)

    return None


for x in range(len(brand_names)):  # runner('cow&gate')
    a = brand_names[x]
    b = file_names_container[x]
    runner(a, b)


# print(len(value_holder))

# print(len(value_holder))
