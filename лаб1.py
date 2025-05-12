import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook #для создания Excel-файла

def parse_habr_career():
    url = 'https://career.habr.com/vacancies/skills/python'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Ошибка при получении данных с Хабр Карьера")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    vacancies = soup.find_all('div', class_='vacancy-card')

    wb = Workbook() #Создаём новый Excel-файл
    ws = wb.active #Создаём новый Excel-файл
    ws.append(["Название вакансии", "Ссылка", "Компания", "Город"])

    for vacancy in vacancies: #Цикл по всем найденным вакансиям на странице.
        title_tag = vacancy.find('div', class_='vacancy-card__title')
        title = title_tag.text.strip() if title_tag else "Не указано"
#Находим название вакансии. Сначала ищем блок с нужным классом, затем берём текст. Если блока нет записываем "Не указано".
        link_tag = title_tag.find('a') if title_tag else None
        link = 'https://career.habr.com' + link_tag['href'] if link_tag else "Нет ссылки"
#Извлекаем ссылку на вакансию. Она находится внутри тега a. Добавляем к ней базовый адрес сайта.
        company_tag = vacancy.find('div', class_='vacancy-card__company-title')
        company = company_tag.text.strip() if company_tag else "Не указано" #Извлекаем название компании.
        inlin = vacancy.find('span', class_= 'inline-list')


        city_tag = vacancy.find('div', class_='vacancy-card__meta')
        city = city_tag.find_all('a')

        sityparts = ''
        for c in city:
            sityparts += c.text + ' '

        sityparts = sityparts.strip() if sityparts else "Не указано"

        ws.append([title, link, company, sityparts]) #Добавляем данные в Excel таблицу.

    wb.save("vacancies.xlsx") #Сохраняем Excel файл

# Вызов функции
if __name__ == '__main__':
    parse_habr_career()
