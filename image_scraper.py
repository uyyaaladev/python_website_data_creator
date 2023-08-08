import wget
import subprocess
import pandas as pd
import requests
import json
import urllib3
import os
import glob


# Path to the directory containing the .xlsx files
directory = os.getcwd()

# Get a list of all .xlsx files in the directory
xlsx_files = glob.glob(os.path.join(directory, '*.xlsx'))

excel_data = []


def append_data(a):
    return excel_data.append(a)


def create_data(a: str) -> list:
    b = a
    urls = pd.read_excel(b)
    for x in urls['urls']:
        append_data(x)


for x in xlsx_files:
    create_data(x)


# files_cont = pd.read_excel(xlsx_files[0])

image_data_holder = []

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


def get_data(a):
    val = url_alterator(a)
    response = requests.get(val)
    result = response.json()
    return result


file_names_container = []


def image_data(x: str) -> None:
    key_count = 0
    abcde = x[33:]
    a: dict = get_data(x)
    for value in a["product"]["images"]:
        for key, value in value.items():
            if "src" in key:
                file_names_container.append(abcde+"-"+str(key_count))
                key_count += 1
                image_data_holder.append(value)
                # print(key_count)
    key_count = 0


for x in excel_data:
    value = x
    abcd = image_data(value)


def downloader(x, y):
    base_url = x
    image_name = y + ".webp"
    wget.download(base_url, out=directory + "/" + image_name)


for x in range(len(image_data_holder)):
    abcd = image_data_holder[x]
    file_nms = file_names_container[x]
    downloader(abcd, file_nms)


# def runcmd(cmd, verbose=False, *args, **kwargs):

#     process = subprocess.Popen(
#         cmd,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         text=True,
#         shell=True
#     )
#     std_out, std_err = process.communicate()
#     if verbose:
#         print(std_out.strip(), std_err)
#     pass


# for y in image_data_holder:
#     runcmd(f"wget {y}", verbose=True)


# def downloader(url, file_path, file_name):
#     full_path = file_path + file_name + '.jpg'
#     # urllib3.urlretrieve(url, full_path)
#     urllib3.

# for items in a.values():
#     for key, value in items.items():
#         if "images" in key:
#             for v in value:
#                 for k, vl in v.items():
#                     if "src" in k:
#                         print(vl)

#     for val in v.values():
#         for key, value in val['images']:
#             image_data_holder.append({key: value})


# print(len(image_data_holder))
