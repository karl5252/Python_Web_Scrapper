from bs4 import BeautifulSoup

contents = '<q tag1 tag2>Quote1</q>dome other text<q tag1 tag3>quote2</q>'

soup = BeautifulSoup(contents)

for tag in soup.findAll('q'):
    print(f"{tag.name} : {tag.attrs}")
    #print(tag.contents)
print('Finished')
