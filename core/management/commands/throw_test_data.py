"""
core/test_data.py

Populates DB with example data for development, testing and demonstration purposes
"""

import json
import pathlib
import random
from datetime import datetime

import requests
import tqdm

from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from django.conf import settings
from core.models import (
    Order,
    Master,
    Service,
    Review,
    DecorImage,
)


class Command(BaseCommand):
    """
    Populates DB with example data for development, testing and demonstration purposes
    """

    BASE_DIR = settings.BASE_DIR
    MEDIA_ROOT = settings.MEDIA_ROOT

    help = "Populates DB with example data for development, testing and demonstration purposes"

    def load_data(self):
        """
        data taken off to json for readability, now read them
        """
        with open(
            pathlib.Path(__file__).resolve().parent / "data.json", "r", encoding="utf-8"
        ) as f:
            return json.loads(f.read())

    def download_pics(self, google_drive_url, pics_ids):
        """
        Downloads images from googledrive to media/ dir
        """
        print("download pics...")
        total = sum([len(dir_) for dir_ in pics_ids.values()])
        pbar = tqdm.tqdm(total=total)
        for dir_name, content_dict in pics_ids.items():

            for file_name, file_id in content_dict.items():
                filepath = pathlib.Path(self.MEDIA_ROOT / dir_name / f"{file_name}.webp")
                filepath.parent.mkdir(parents=True, exist_ok=True)
                if not filepath.is_file():
                    response = requests.get(google_drive_url.format(file_id), timeout=5)
                    if response.status_code == 200:
                        with open(filepath, "wb") as f:
                            f.write(response.content)
                pbar.update(1)
        pbar.close()
        print("done!\n")

    def populate_db(self, masters, services, orders, reviews, decor_pics):
        """
        manually adds data to db
        """

        service_insts = {}
        for i, service in enumerate(services, start=1):
            inst = Service(
                name=service["name"],
                description=service["description"],
                price=service["price"],
                duration=random.randint(10, 300),
                image=ImageFile(open(self.MEDIA_ROOT / "service" / f"{i}.webp", "rb")),
            )
            service_insts[i] = inst
            inst.save()

        master_insts = {}
        for i, master in enumerate(masters, start=1):
            inst = Master(
                name=master["name"],
                bio=master["description"],
                photo=ImageFile(open(self.MEDIA_ROOT / "master" / f"{i}.webp", "rb")),
                experience=master["work_experience"],
                services_provided=[service_insts[id_] for id_ in master["services"]],
            )
            master_insts[i] = inst
            inst.save()

        order_insts = {}
        for i, order in enumerate(orders, start=1):
            inst = Order(
                client_name=order["client_name"],
                phone="".join(random.choices(range(10), k=11)),
                master=master_insts[order["master_id"]],
                services=[service_insts[id_] for id_ in order["services"]],
                appointment_date=datetime.combine(
                    datetime.strptime(order["date"], "%Y-%m-%d").date(),
                    datetime.time(random.randint(10, 20), 0),
                ),
            )
            order_insts[i] = inst
            inst.save()

        review_insts = {}
        for i, review in enumerate(reviews, start=1):
            inst = Review(
                text=review["text"],
                client_name=review["client_name"],
                master=master_insts[review["master_id"]],
                services_were_provided=[service_insts[id_] for id_ in review["services"]],
                rating=review["rating"],
            )
            review_insts[i] = inst
            inst.save()

        decor_image_insts = {}
        for name in decor_pics.keys():
            inst = DecorImage(
                image=ImageFile(open(self.MEDIA_ROOT / "decor" / f"{name}.webp", "rb"))
            )
            decor_image_insts[name] = inst
            inst.save()

    def clear_db(self):
        """
        erase everything before population
        """
        for model in [
            Order,
            Master,
            Service,
            Review,
            DecorImage,
        ]:
            model.objects.all().delete()

    def handle(self, *args, **options):
        (
            google_drive_url_,
            pics_ids_,
            masters_,
            services_,
            orders_,
            reviews_,
        ) = self.load_data().values()

        self.download_pics(google_drive_url_, pics_ids_)
        self.populate_db(masters_, services_, orders_, reviews_, pics_ids_["decor"])
