from rest_framework import serializers
from .models import JournalEntry

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = ['id', 'user', 'text', 'mood', 'timestamp']
        read_only_fields = ['user', 'mood', 'timestamp']
