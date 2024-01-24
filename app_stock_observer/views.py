from django.http import JsonResponse
from django.views import View
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from app_stock_observer.models import CourseJournal


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        print('TYT')
        print(type(obj))
        if isinstance(obj, CourseJournal):
            print(obj)
            return str(obj)
        return super().default(obj)


class MyView(View):
    def get(self, request, *args, **kwargs):
        data = serializers.serialize('json', CourseJournal.objects.all()[:10], cls=LazyEncoder)
        print(type(data))
        return JsonResponse(data=data, safe=False)
