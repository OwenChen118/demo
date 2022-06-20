import xml.etree.ElementTree as et

tree=et.ElementTree(file='menu.xml')
root=tree.getroot()
print(root.tag)

for meal in root:
    print('tag:',meal.tag,'attr:',meal.attrib)
    for price in meal:
        print('\ttag:',price.tag,'attr:',price.attrib)

