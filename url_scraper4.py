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


def append_data(a):
    return excel_data.append(a)


def create_data(a: str) -> list:
    urls = pd.read_excel(a)
    for x in urls['urls']:
        append_data(x)


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


def create_file_names(a: list) -> str:
    if "cow&gate" in a:
        strs = a.replace("cow&gate", "cow_gate")
        b = strs[len(str1):-5]
    else:
        b = a[len(str1):-5]

    c = f"{b}_extracted_data"
    return c


def create_brand_names(x):
    abcd = x.split("_")[0]
    brand_names.append(abcd)


def get_data(a):
    response = requests.get(a)
    result = response.json()
    return result


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
    for dict_items in x:
        for value in dict_items.values():
            for key, value in value.items():
                if key in keys_to_check:
                    data_list.append(
                        {key: format_data(value, pattern1, pattern2)})
    return data_list


# def output_data(x, y):
#     output_path = directory + "/output/" + y
#     df = pd.DataFrame(x)
#     # df.to_excel(f"{output_path}.xlsx")
#     df.to_excel(f"{output_path}.xlsx")


def executioner(a):
    for x in range(len(excel_data)):
        bad = a
        if bad in excel_data:
            value_holder.append(get_data(excel_data[x]))

    abcd = filter_data(value_holder)
    # bund = output_data(abcd, b)
    print(data_list)
    return None


def task_runner(a):
    create_data(a)
    for x, y in enumerate(excel_data):
        alter_data(x, y)


def task_runner2():
    for x in range(len(file_names_container)):
        a = brand_names[x]
        # b = file_names_container[x]
        executioner(a)


for x in range(2):
    abcd = xlsx_files[x]
    task_runner(abcd)
    create_file_names(abcd)
    create_brand_names(abcd)
    task_runner2()


# for x in excel_data:
#     print(x)
