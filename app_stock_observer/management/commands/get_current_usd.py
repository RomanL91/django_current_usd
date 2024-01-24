import requests, certifi

from time import sleep

from multiprocessing import Process

from django.conf import settings 

from django.core.management.base import BaseCommand

from app_stock_observer.models import CourseJournal

# from django.utils import timezone


class Command(BaseCommand):

    def add_SSL_certi(self):
        path_cert = certifi.where()
        file_cert_to_add = open(
            'Unified_State_Internet_Access_Gateway.cer', 'r'
        )
        cert_to_add = file_cert_to_add.read()
        file_cert_to_add.close()
        with open(path_cert, 'a') as file_cert:
            file_cert.write(cert_to_add)
        print('[==INFO==] Unified_State_Internet_Access_Gateway.cer добавлен')


    def get_current_usd(self):

        self.add_SSL_certi()

        print('[==INFO==] Запуск скрипта получения данных курса USD/RUB.')
        
        while True:
            response = requests.post(
                url=settings.URL_API_CURRENT_USD, 
                json=settings.INFORMATION_FOR_DOWNLOAD
            ).json()

            data = response['data']

            for el in data:
                if el['s'] == 'MOEX:SIH2024':
                    obj = CourseJournal.objects.create(
                        section=el['s'],
                        exchange_rate=el['d'][-2] / 1000,
                        # date_time=timezone.now() # как вариант добавлять время, при auto_now_add=False
                    )
                    obj.save()
                    break

            sleep(settings.REQUEST_DELAY_INTERVAL)


    def handle(self, *args, **options):
        proc = Process(target=self.get_current_usd)
        proc.start()
        proc.join()
