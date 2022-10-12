import requests as req
from bs4 import BeautifulSoup
import json
import tqdm
import time

data = {
    "data":[]
}


for page in range(0,41):
    url = f"https://barnaul.hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&salary=&clusters=true&ored_clusters=true&enable_snippets=true&page={page}&hhtmFrom=vacancy_search_list"
    resp = req.get(url,  headers={'user-agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(class_ = "vacancy-serp-item-body__main-info")

    for iter in tqdm.tqdm(tags):
        time.sleep(2)
        tag_title = iter.find(class_ = "serp-item__title")

        tag_region = iter.find(attrs={"data-qa":"vacancy-serp__vacancy-address"}).text
        
        url_object = tag_title.attrs["href"]
        resp_object = req.get(url_object,  headers={'user-agent': 'Mozilla/5.0'})
        
        soup_object= BeautifulSoup(resp_object.text, "lxml")
        tag_experience = soup_object.find(class_ = "vacancy-description-list-item").find_all(attrs={"data-qa":"vacancy-experience"})[0].text 

        tag_salary = soup_object.find(attrs={"data-qa":"vacancy-salary"}).text

        data["data"].append({"title":tag_title.text , "work expirience":tag_experience, "salary":tag_salary, "region":tag_region})

        with open("data.json", "w") as file:
            json.dump(data,file, ensure_ascii=False, indent=4)