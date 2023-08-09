import os
import glob
import pandas as pd
import requests
import re


class DataProcessor:
    def __init__(self):
        self.addon = ".json"
        self.file_names_container = []
        self.str1 = 'c:/Users/Yeshwanth/Desktop/uyyaala to kidsfud products/milk_formulas/'
        self.json_container = []
        self.data_list = []
        self.pattern1 = r'data-mce-fragment="1"'
        self.pattern2 = r'data-mce-style="color: #([a-zA-z0-9]{6});"'
        self.keys_to_check = {'title', 'body_html',
                              'vendor', 'product_type', 'handle'}
        self.excel_data = []
        self.brand_names = []
        self.value_holder = []
        self.str_len = len('_milk_formulas.xlsx')

    def append_data(self, a):
        self.excel_data.append(a)

    def create_data(self, a):
        urls = pd.read_excel(a)
        for x in urls['urls']:
            self.append_data(x)

    def create_brand_names(self, a):
        if "cow&gate" in a:
            strs = a.replace("cow&gate", "cow_gate")
            b = strs[len(self.str1):-(self.str_len)]
        else:
            b = a[len(self.str1):-(self.str_len)]

        self.brand_names.append(b)

    def url_alterator(self, x):
        container = x + self.addon
        return container

    def alter_data(self, a, b):
        abcd = self.url_alterator(b)
        self.excel_data[a] = abcd

    def run_alterator(self):
        for x, y in enumerate(self.excel_data):
            self.alter_data(x, y)

    def get_data(self, a):
        if a != "":
            response = requests.get(a)
            result = response.json()
            self.json_container.append(result)

    def run_get_data(self):
        for x in self.excel_data:
            self.get_data(x)
        self.excel_data.clear()

    def format_data(self, val, pattern1, pattern2):
        container = re.sub(pattern1, "", val)
        container = re.sub(pattern2, "", container)
        return container

    def filter_data(self, x):
        data_container = {}
        for key, value in x["product"].items():
            if key in self.keys_to_check:
                data_container[key] = self.format_data(
                    value, self.pattern1, self.pattern2)
        self.data_list.append(data_container)

    def run_filter_data(self):
        for x in self.json_container:
            self.filter_data(x)

    def bundle_data(self, x, y):
        output_path = os.getcwd() + "/output/" + y
        df = pd.DataFrame(x)
        df.to_excel(f"{output_path}.xlsx")

    def process_data(self, xlsx_files):
        for x in range(len(xlsx_files)):
            data = xlsx_files[x]
            self.create_data(data)
            self.run_alterator()
            self.create_brand_names(data)
            self.run_get_data()
            self.run_filter_data()
            brand_data = self.brand_names[x]
            self.bundle_data(self.data_list, brand_data)
            self.excel_data.clear()
            self.json_container.clear()
            self.value_holder.clear()
            self.data_list.clear()


if __name__ == "__main__":
    directory = os.getcwd()
    xlsx_files = glob.glob(os.path.join(directory, '*.xlsx'))

    data_processor = DataProcessor()
    data_processor.process_data(xlsx_files)
