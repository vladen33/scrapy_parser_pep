# Scrapy PEP - Асинхронный парсер документации PEP на базе фреймворка Scrapy

## Описание проекта:
В проекте представлен **Парсер**, который собирает информацию с сайта https://www.python.org/
- перечень всех PEP, с указанием номера, названия и статуса;
- сводную информацию о статусах PEP (статус - количество);
- вся информация сохраняется в файлы **csv**

## Инструкция по установке:
1. Загрузите проект:
```bash
git clone https://github.com/vladen33/scrapy_parser_pep.git
```
2. Установите и активируйте виртуальное окружение, обновите pip:
```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -U pip
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Запусnbnt парсер pep:
```
scrapy crawl pep
```

### Автор проекта:
[Васильев Владислав](https://github.com/vladen33)
