import re

with open('\Users\Санжар\Desktop\PP2\TSIS4\Input.txt', 'r', encoding = 'utf-8') as f:
    txt = f.read()


compnamepat = re.findall(r'(?<=ТОО )[\w]+', txt)
compBINpat = re.findall(r'(?<=БИН )[\d]{12}', txt)

cntpat = re.findall(r'\d+\.\n', txt)
productsnamespat = re.findall(r'(.*)\n\d+,\d+ x \d+ ?\d+,\d+', txt)
amountofproduct = re.findall(r'(\d+),\d+ x \d+ ?\d+,\d+', txt)
priceofproduct = re.findall(r'\d+,\d+ x (\d+ ?\d+,\d+)', txt)
totalpriceofproducts = re.findall(r'Стоимость\n(\d+ ?\d+,\d+)', txt)

datepat = re.findall(r'Время: (\d{2}.\d{2}.\d{4} \d{2}:\d{2}:\d{2})', txt)
adresspat = re.findall(r'г\. (.*)', txt)

print('Name of the company:', *compnamepat)
print('BIN of the company:', *compBINpat)
print('List of bought items:')

for i in range(len(cntpat)):
    print('Title:', productsnamespat[i])
    print('Count:', amountofproduct[i])
    print('Unit price:', priceofproduct[i])
    print('Total price', totalpriceofproducts[i])

print('Time:', *datepat)
print('Adress:', *adresspat)