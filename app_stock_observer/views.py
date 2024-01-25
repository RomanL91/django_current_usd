from django.views import View

from django.http import HttpResponse, JsonResponse

from app_stock_observer.models import CourseJournal


class GetCurrentUsd(View):
    def get(self, request, *args, **kwargs):
        data = [
            el.to_dict for el in CourseJournal.objects.all().order_by('-date_time')[:10]
        ]
        return JsonResponse(data=data, safe=False)


class RootView(View):
    def get(self, request, *args, **kwargs):
        try:
            log_name = request.META['LOGNAME']
        except Exception:
            log_name = 'пользователь' 
        info = f'''
        Привет {log_name}! <br>
        Это информационный вывод.<br>
        Задание:<br>
        Предлагаем вам создать "голый" джанго проект,<br>
        который по переходу на страницу /get-current-usd/ (<a href="/get-current-usd/">GO</a>)<br> 
        бужет отображать в json формате актуальный курс доллара к рублю<br>
        (запрос по апи, найти самостоятельно) и показывать 10 последних запросов<br>
        (паузу между запросами курсов должна быть не менее 10 секунд).<br>
        <hr>
        Мои мысли:<br>
        "голый" джанго проект? - для него в голову лезет Celery, Redis + DRF,<br>
        но "голый" так "голый".<br>
        <br>
        Зависимости который я поставил (django, requests, uvicorn и все.)<br>
        --> asgiref==3.7.2 ; python_version >= "3.10" and python_version < "4.0"<br>
        --> certifi==2023.11.17 ; python_version >= "3.10" and python_version < "4.0"<br>
        --> charset-normalizer==3.3.2 ; python_version >= "3.10" and python_version < "4.0"<br>
        --> click==8.1.7 ; python_version >= "3.10" and python_version < "4.0"<br>
        --> colorama==0.4.6 ; python_version >= "3.10" and python_version < "4.0" and platform_system == "Windows"<br>
        --> django==5.0.1 ; python_version >= "3.10" and python_version < "4.0"<br>
        --> h11==0.14.0 ; python_version >= "3.10" and python_version < "4.0"<br>
        --> idna==3.6 ; python_version >= "3.10" and python_version < "4.0"<br>
        --> requests==2.31.0 ; python_version >= "3.10" and python_version < "4.0"<br>
        --> sqlparse==0.4.4 ; python_version >= "3.10" and python_version < "4.0"<br>
        --> typing-extensions==4.9.0 ; python_version >= "3.10" and python_version < "3.11"<br>
        --> tzdata==2023.4 ; python_version >= "3.10" and python_version < "4.0" and sys_platform == "win32"<br>
        --> urllib3==2.1.0 ; python_version >= "3.10" and python_version < "4.0"<br>
        --> uvicorn==0.27.0 ; python_version >= "3.10" and python_version < "4.0"<br>
        <br>
        (запрос по апи, найти самостоятельно) ?? - это было наверное самым трудным<br>
        ввиду отсутствия времени. Честно, что я нашел, устраивает меня на 5 из 10.<br>
        Зашел на сайт tradingview и через инструменты разработчика во вкладке сеть<br>
        нашел это: 'https://scanner.tradingview.com/futures/scan', однако, чтобы от <br>
        этого что-то получить нужно дать ему "полезную нагрузку".<br>
        <br>
        (паузу между запросами курсов должна быть не менее 10 секунд) ??<br>
        не менее..то есть 11 сек и больше, правильно же понял? - если так,<br>
        тогда у меня все верно.<br>
        не меньше же 10 сек?! (7, 8, 9).. - а так, значит я запутался =).<br>
        <br>
        для админки:<br>
        логин: admin<br>
        пароль: Eto@$SamuySlojnuy123Parol!<br>
        <br>
        <hr>
        Спасибо за предоставленную возможноть.<br>
        С уважением Лебедев Роман Александрович.<br>
        +7(771)464-87-17, @RomanL91<br>
        <a href="https://hh.kz/resume/cb6d9481ff0b03b7b90039ed1f52637a584e66">Мое резюме</a>
        '''
        return HttpResponse(info)
