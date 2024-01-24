from django.contrib import admin

from app_stock_observer.models import CourseJournal


@admin.register(CourseJournal)
class CourseJournalAdmin(admin.ModelAdmin):
    list_display = [
        'section', 'exchange_rate', 'date_time',
    ]
    readonly_fields = [
        'section', 'exchange_rate', 'date_time',
    ]
