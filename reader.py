import requests
from bs4 import BeautifulSoup


# identify elements that can be used -> anchor, button, image, input, select, textarea
# get attributes id,name,placeholder,value,title,type,class, hidden
# print only attributes that match the set and are part of selected elements
def attribute_filter(element):
    for attribute in attribute_els:
        return element.has_attr(attribute)


# def regular_parse(tag_name, attrib, tag_value):  # //tagName[@attrib='attrib value'][@attrib2='attrib2 value']...
#     if type(tag_value[attrib]) is list:
#         tag_value[attrib] = [i.encode('utf-8').decode('latin-1') for i in tag_value[attrib]]
#         tag_value[attrib] = ' '.join(tag_value[attrib])
#     return f"//{tag_name}[@{attrib}='{tag_value[attrib]}']"


def dict_parse(tag_name, attr_dict):  # //tagName[@attrib='attrib value'][@attrib2='attrib2 value']...
    xpath = f"//{tag_name}"
    for key in attr_dict:
        xpath += f"[@{key}='{attr_dict.get(key)}']"
    return xpath


def contains_parser(search_tag, attr_dict):
    # //xpath[contains( @ attribute, 'attribute value')]
    # //xpath[contains( @ text(), 'attribute value')]
    pass


def text_parser(search_tag, text):
    # //button[text()]
    # //button/text()
    pass


if __name__ == "__main__":
    URL = ""
    interactive_elements = ('a', 'button', 'img', 'input', 'select', 'textarea')
    attribute_els = ('class', 'hidden', 'id', 'name', 'placeholder', 'title', 'type', 'value')

    # URL = "https://www.msn.com/pl-pl/wiadomosci/polska/samoch%C3%B3d-przelecia%C5%82-nad-ogrodzeniem-i-kozio%C5%82kowa%C5%82-na-prywatnej-posesji/ar-AAQpRlv?ocid=BingHPC"  # "https://realpython.github.io/fake-jobs/"
    URL = "http://localhost:63342/Python_Web_Scrapper/test_1.html?_ijt=t2e6llvg3jm08scj5bsg7leba1"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    for interactive_element in interactive_elements:  # button
        searched_elements = soup.find_all(interactive_element)
        for searched_element in searched_elements:  # <button name="banana" type="button">Banana</button>
            #print(f"{searched_element.name}: {(searched_element.attrs)}")
            print(dict_parse(searched_element.name, searched_element.attrs))

            # if dictonary size iz larger than 1(pair) put key-pair into a list
            # print(searched_element.get_attribute_list(attribute_els))
            # for attribute in attribute_els:

            # attr_filter = searched_element.has_attr(attribute)
            # if attr_filter:
            # print(f"{searched_element}{searched_element.get_attribute_list(attribute)})
            #    attr_list = searched_element.get_attribute_list(attribute)
            #    print(f"{interactive_element}: {attribute} {attr_list}")
            # print(searched_element)
            # print(regular_parse(interactive_element, attribute, searched_element))
