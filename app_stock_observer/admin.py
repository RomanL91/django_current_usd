from django.contrib import admin

from app_stock_observer.models import CourseJournal


@admin.register(CourseJournal)
class CourseJournalAdmin(admin.ModelAdmin):
    fields_model = [
        'section', 'exchange_rate', 'date_time',
    ]
    list_display = fields_model
    readonly_fields = fields_model
