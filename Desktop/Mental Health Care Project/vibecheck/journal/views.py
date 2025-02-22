from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import JournalEntry
from .serializers import JournalENtrySerializer
from .utils import analyze_sentiment

# Create your views here.
class JournalEntryView(APIViews):
    journals = JournalEntry.objects.filter(user=request.user).order_by()

