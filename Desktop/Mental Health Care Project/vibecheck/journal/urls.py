from django.urls import path
from .import views
from journal.views import JournalEntryListCreate
from journal.views import index  # Ensure this matches the function name


urlpatterns = [
    path('journals/', JournalEntryListCreate.as_view(), name='journal-entries'),
    path("", index, name="Journal-Home")
]
