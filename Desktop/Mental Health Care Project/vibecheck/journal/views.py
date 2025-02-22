from rest_framework import generics, permissions
from .models import JournalEntry
from .serializers import JournalEntrySerializer
from .utils import analyze_sentiment
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the homepage!")


class JournalEntryListCreate(generics.ListCreateAPIView):
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user).order_by('-timestamp')

    def perform_create(self, serializer):
        text = self.request.data.get("text", "")
        mood = analyze_sentiment(text)
        serializer.save(user=self.request.user, mood=mood)
