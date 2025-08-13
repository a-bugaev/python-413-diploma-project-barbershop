"""
core/test_data.py

Populates DB with example data for development, testing and demonstration purposes
"""

import pathlib
import requests
import tqdm

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent

MASTERS = [
    {
        "id": 1,
        "name": "Эльдар 'Бритва' Рязанов",
        "description": "Мастер с опытом работы — владелец непревзойденной техники, чьи 'бритвы' (игр.) делают прически идеальными и гладкими.",
        "work_experience": 10,
    },
    {
        "id": 2,
        "name": "Зоя 'Ножницы' Космодемьянская",
        "description": "Мастер с 8-летним опытом — настоящий виртуоз 'ножниц', каждый клиент получает уникальный и точный до мелочей образ.",
        "work_experience": 8,
    },
    {
        "id": 3,
        "name": "Борис 'Фен' Пастернак",
        "description": "Мастер с 12-летним опытом — творец форм, его 'фен' превращает волосы в легкие, вьющиеся и элегантные произведения искусства.",
        "work_experience": 12,
    },
    {
        "id": 4,
        "name": "Иннокентий 'Лак' Смоктуновский",
        "description": "Мастер с 15-летним опытом — маг 'лака', создавая на прядях глянцевую или матовую чарму, словно на волшебной палитре.",
        "work_experience": 15,
    },
    {
        "id": 5,
        "name": "Раиса 'Бигуди' Горбачёва",
        "description": "Мастер с 9-летним опытом — молчаливая гувернантка стилей, ее 'бигуди' (игр.) всегда приводят в идеальную, неподдельную форму.",
        "work_experience": 9,
    },
]

SERVICES = [
    {
        "id": 1,
        "name": "Стрижка под 'Горшок'",
        "description": "Классическая стрижка",
        "price": 500,
    },
    {
        "id": 2,
        "name": "Укладка 'Взрыв на макаронной фабрике'",
        "description": "Стильная укладка",
        "price": 700,
    },
    {
        "id": 3,
        "name": "Королевское бритье опасной бритвой",
        "description": "Роскошное бритье",
        "price": 1000,
    },
    {
        "id": 4,
        "name": "Окрашивание 'Жизнь в розовом цвете'",
        "description": "Модное окрашивание",
        "price": 1200,
    },
    {
        "id": 5,
        "name": "Мытье головы 'Душ впечатлений'",
        "description": "Релаксирующее мытье",
        "price": 300,
    },
    {
        "id": 6,
        "name": "Стрижка бороды 'Боярин'",
        "description": "Стильная стрижка бороды",
        "price": 600,
    },
    {
        "id": 7,
        "name": "Массаж головы 'Озарение'",
        "description": "Релаксирующий массаж",
        "price": 800,
    },
    {
        "id": 8,
        "name": "Укладка 'Ветер в голове'",
        "description": "Легкая укладка",
        "price": 400,
    },
    {
        "id": 9,
        "name": "Плетение косичек 'Викинг'",
        "description": "Стильное плетение",
        "price": 900,
    },
    {
        "id": 10,
        "name": "Полировка лысины до блеска",
        "description": "Блестящая полировка",
        "price": 200,
    },
]

STATUS_CHOICES = {
    "new": "новая",
    "confirmed": "подтвержденная",
    "cancelled": "отмененная",
    "completed": "выполненная",
}

ORDERS = [
    {
        "id": 1,
        "client_name": "Пётр 'Безголовый' Головин",
        "services": [1, 10],
        "master_id": 1,
        "date": "2025-03-20",
        "status": STATUS_CHOICES["new"],
    },
    {
        "id": 2,
        "client_name": "Василий 'Кудрявый' Прямиков",
        "services": [2],
        "master_id": 2,
        "date": "2025-03-21",
        "status": STATUS_CHOICES["confirmed"],
    },
    {
        "id": 3,
        "client_name": "Афанасий 'Бородач' Бритвенников",
        "services": [3, 6, 7],
        "master_id": 3,
        "date": "2025-03-19",
        "status": STATUS_CHOICES["cancelled"],
    },
    {
        "id": 4,
        "client_name": "Себастьян 'Седой' Крашенов",
        "services": [4, 8],
        "master_id": 4,
        "date": "2025-03-22",
        "status": STATUS_CHOICES["completed"],
    },
]

GOOGLE_DRIVE_URL = "https://drive.usercontent.google.com/download?id={}&export=download&authuser=0"

PICS_IDS = {
    "service": {
        "1": "1_UAdn_9hxRZwhOFFRoRuEGONQzydt9mA",
        "2": "1VfQ386HcIVFdZYI9naQamYATBO6VSLRK",
        "3": "1LY067sa2MQ3zCwIfEYFEV4zngCIOyi-9",
        "4": "1hkj2Xrig9tFa33vgXKr3oBQGkEJ4B614",
        "5": "1khhiArfQkznQLkBvCaropMiWkOR29MxH",
        "6": "1x2GovZdrRXz_fM2HCIY20jq-lHQnRDX6",
        "7": "1se2Jgx51oZ_6wWBRTOvJScMZ3y7SLe2X",
        "8": "1C55sqVzWVuFiXGxTWgnSAwCvAWzWzT24",
        "9": "1pL4ko10WTsdImMLVDcIClcQb0BZ6HK8m",
        "10": "1YOw4BRreGuqrX5p2ROnZJyNCtMph-KNG",
    },
    "master": {
        "1": "14kuXccnYoBkQszGSx9-kPcXa_zF6Jj4b",
        "2": "1DZQ74pw6rQOlfXMWrda9_nduKnfbbWUi",
        "3": "1Tebt1j1QtDnn9z_lF06mTgw118oP06KK",
        "4": "1XJJoMPZmXpg7Ozk_o6ZGBv8q-vzN9qJv",
        "5": "1zr7juLCqjMsyVTQAI-a01LFEITz8-6DB",
    },
    "decor": {
        "interior": "1gv8U6yYymdg-BLTQiyJB8Mi-DVg9gegP",
    },
}


def download_pics():
    """
    Downloads images from googledrive to media/ dir
    """
    print("wait...")
    total = sum([len(dir_) for dir_ in PICS_IDS.values()])
    pbar = tqdm.tqdm(total=total)
    for dir_name, content_dict in PICS_IDS.items():

        for file_name, file_id in content_dict.items():
            response = requests.get(GOOGLE_DRIVE_URL.format(file_id), timeout=5)
            if response.status_code == 200:
                filepath = pathlib.Path(f"{PROJECT_ROOT}/media/{dir_name}/{file_name}.webp")
                filepath.parent.mkdir(parents=True, exist_ok=True)
                with open(filepath, "wb") as f:
                    f.write(response.content)
                    pbar.update(1)
    pbar.close()
    print("done!\n")

download_pics()
