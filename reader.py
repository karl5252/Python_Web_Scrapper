import requests
from bs4 import BeautifulSoup

# identify elements that can be used -> anchor, button, image, input, select, textarea
# get attributes id,name,placeholder,value,title,type,class, hidden
# print only attributes of selected elements

if __name__ == "__main__":
    URL = ""
    _interactive_els = ('a', 'button', 'img', 'input', 'select', 'textarea')
    _attribute_els = ('class', 'hidden', 'id', 'name', 'placeholder', 'title', 'type', 'value')

    URL = "https://realpython.github.io/fake-jobs/"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    for interactive_el in _interactive_els:
        #element = soup._interactive_els.find_all(interactive_el)
        element = soup.find_all(interactive_el)
        for attribute in _attribute_els:
            if element.has_attr(attribute)
        #print(f"{interactive_el}: {element}")
