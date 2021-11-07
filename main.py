import requests
from bs4 import BeautifulSoup

# get page as html
# idenftify elements that can be used -> anchor, button, image, input, select, textarea
# list them grouped by type
# print into JSON file

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="ResultsContainer")
# print(results.prettify())
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
      print(job_element.prettify(), end="\n" * 2)

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    links = job_element.find_all("a")
    for link in links:
        print(link.text.strip())




