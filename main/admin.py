from django.contrib import admin
from .models import Entry
from .forms import EntryCreateForm

# Register your models here.
class EntryCreateAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'matric_no', 'lecture_1', 'lecture_2', 'lecture_3', 'lecture_4', 'lecture_5', 'lecture_6']
    form = EntryCreateForm
    search_fields = ['first_name', 'second_name']


    
admin.site.register(Entry, EntryCreateAdmin)