from rest_framework import generics, permissions
from .models import JournalEntry
from .serializers import JournalEntrySerializer
from .utils import analyze_sentiment
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
import random

# ✅ Home Page View
def index(request):
    return render(request, "index.html")  # Ensure the path is correct

# ✅ Generates Personalized Advice Based on Mood
def generate_advice(mood):
    positive_responses = [
        "You're doing great! Keep up the positive mindset! 💪",
        "Your energy is inspiring! Keep spreading the good vibes. 🌟",
        "Stay consistent and watch yourself achieve even greater things! 🚀",
    ]
    
    neutral_responses = [
        "Try doing something new today! Maybe a new hobby or a challenge?",
        "Growth happens when you step outside your comfort zone. What’s one thing you can improve?",
        "Feeling neutral is okay, but how about adding some excitement to your day?"
    ]
    
    negative_responses = [
        "Don't let someone's words define you. You're stronger than you think! ❤️",
        "It's okay to have bad days. What matters is that you don't let them stop you. Keep going!",
        "You're not alone. Talk to someone you trust, and remember, this moment will pass. 🌈"
    ]

    if mood == "Positive":
        return random.choice(positive_responses)
    elif mood == "Neutral":
        return random.choice(neutral_responses)
    elif mood == "Negative":
        return random.choice(negative_responses)
    
    return "Stay strong and keep moving forward!"

# ✅ Journal API: Create and Retrieve Journal Entries
class JournalEntryListCreate(generics.ListCreateAPIView):
    serializer_class = JournalEntrySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return JournalEntry.objects.filter(user=self.request.user).order_by('-time_stamp')
        return JournalEntry.objects.none()

    def perform_create(self, serializer):
        text = self.request.data.get("text", "").strip()

        if not text:
            raise serializers.ValidationError({"text": "Journal entry cannot be empty."})

        mood = analyze_sentiment(text)
        advice = generate_advice(mood)

        serializer.save(user=self.request.user if self.request.user.is_authenticated else None, mood=mood)

        # Return response with mood and advice
        return Response({
            "message": "Journal entry created successfully.",
            "mood": mood,
            "advice": advice
        })
