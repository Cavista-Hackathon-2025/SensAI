from django.urls import path
from .import views
from journal.views import JournalEntryListCreate

urlpatterns = [
    path('journals/', JournalEntryListCreate.as_view(), name='journal-entries'),
]
