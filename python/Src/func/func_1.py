#!/use/bin/python
# -*- coding:utf-8 -*-
import yaml
with open(r'C:\Users\zhujh\PycharmProjects\untitled1\Src\element\b.yaml','r',encoding='utf-8')as fb:
    # a =yaml.load(fb) 使用yaml模块的load方法将yaml文件中的数据转换为python字典的形式
    item_data = yaml.load(fb,Loader=yaml.FullLoader)
# print(item_data['three']['wx_id'])
def foo(driver):
    tex=driver.find_element_by_id(item_data['three']['wx_id']).find_element_by_class_name('android.widget.TextView').text
    print(tex)
    return tex
def qq(driver):
    text=driver.find_element_by_id(item_data['three']['qq_id']).find_element_by_class_name('android.widget.TextView').text
    print(text)
    return text
def wb(driver):
    txt=driver.find_element_by_id(item_data['three']['wb_id']).find_element_by_class_name('android.widget.TextView').text
    print(txt)
    return txt
def mlma(driver):
    tet=driver.find_element_by_id(item_data['three']['pd_id']).find_element_by_class_name('android.widget.TextView').text
    print(tet)
    return tet