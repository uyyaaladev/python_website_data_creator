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

value_holder = []

addon = '.json'

str_len = len('_milk_formulas.xlsx')


def append_data(a):
    return excel_data.append(a)


def create_data(a: str) -> list:
    urls = pd.read_excel(a)
    for x in urls['urls']:
        append_data(x)


def create_brand_names(a):
    if "cow&gate" in a:
        strs = a.replace("cow&gate", "cow_gate")
        b = strs[len(str1):-(str_len)]
    else:
        b = a[len(str1):-(str_len)]

    brand_names.append(b)


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


def alter_data(a, b):
    abcd = url_alterator(b)
    excel_data[a] = abcd


def run_alterator():
    for x, y in enumerate(excel_data):
        alter_data(x, y)


def get_data(a):
    if (a != ""):
        response = requests.get(a)
        result = response.json()
        json_container.append(result)


def run_get_data():
    for x in excel_data:
        get_data(x)
    excel_data.clear()


def format_data(val: str, pattern1: str, pattern2: str) -> str:
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


def filter_data(x: list) -> list:
    data_container = {}
    for key, value in x["product"].items():
        if key in keys_to_check:
            data_container[key] = format_data(value, pattern1, pattern2)
            # data_list.append(
            #     {key: format_data(value, pattern1, pattern2)})
    data_list.append(data_container)


def run_filter_data():
    for x in range(len(json_container)):
        filter_data(json_container[x])


def bundle_data(x, y):
    output_path = directory + "/output/" + y
    df = pd.DataFrame(x)
    df.to_excel(f"{output_path}.xlsx")


def print_json_data():
    if len(json_container) > 0:
        for x in json_container:
            print(x)
    print("printed 1 time")


for x in range(len(xlsx_files)):
    data = xlsx_files[x]
    create_data(data)
    run_alterator()
    create_brand_names(data)
    run_get_data()
    # excel_data.clear()
    run_filter_data()
    brand_data = brand_names[x]
    bundle_data(data_list, brand_data)
    del excel_data[:]
    del json_container[:]
    del value_holder[:]
    del data_list[:]
