import requests
from bs4 import BeautifulSoup


# identify elements that can be used -> anchor, button, image, input, select, textarea
# get attributes id,name,placeholder,value,title,type,class, hidden
# print only attributes that match the set and are part of selected elements
def regular_parse(search_tag, search_attrib, search_val):  # //tagname[@attribute-name=’value1’]
    if type(search_val[search_attrib]) is list:
        search_val[search_attrib] = [i.encode('utf-8').decode('latin-1') for i in search_val[search_attrib]]
        search_val[search_attrib] = ' '.join(search_val[search_attrib])
    return f"//{search_tag}[@{search_attrib}='{search_val[search_attrib]}']"


if __name__ == "__main__":
    URL = ""
    interactive_elements = ('a', 'button', 'img', 'input', 'select', 'textarea')
    attribute_els = ('class', 'hidden', 'id', 'name', 'placeholder', 'title', 'type', 'value')

    URL = "https://www.msn.com/pl-pl/wiadomosci/polska/samoch%C3%B3d-przelecia%C5%82-nad-ogrodzeniem-i-kozio%C5%82kowa%C5%82-na-prywatnej-posesji/ar-AAQpRlv?ocid=BingHPC"  # "https://realpython.github.io/fake-jobs/"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    for interactive_element in interactive_elements:
        searched_elements = soup.find_all(interactive_element)
        for searched_element in searched_elements:
            for attribute in attribute_els:
                attr_filter = searched_element.has_attr(attribute)
                value = ''
                if attr_filter:
                    # print(f"{interactive_element}: {attribute} {searched_element[attribute]}")
                    print(regular_parse(interactive_element, attribute, searched_element))
