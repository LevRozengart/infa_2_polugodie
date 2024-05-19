import xml.etree.ElementTree as ETree
import pandas as pan
def xml_parse(data_file):
    tr = ETree.parse(data_file)
    rt = tr.getroot()
    items = []
    for it in rt.findall('.//item'):
        nm = it.find('name').text
        ct = it.find('category').text
        pr = float(it.find('price').text)
        items.append({'name': nm, 'category': ct, 'price': pr})
    return pan.DataFrame(items)
def filter_and_sort(df, cat):
    filtered = df[df['category'] == cat]
    sorted_df = filtered.sort_values(by='price')
    return sorted_df
def calc_total(df):
    return df['price'].sum()
data_file = './data.xml'
df = xml_parse(data_file)
cat = 'electronics'
sorted_filtered = filter_and_sort(df, cat)
tot = calc_total(sorted_filtered)
print(f"Отфильтрованные и отсортированные данные:\n{sorted_filtered}")
print(f"Общая стоимость товаров в категории '{cat}': {tot}")
