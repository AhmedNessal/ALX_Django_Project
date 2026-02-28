from rest_framework import serializers
from .models import BorrowRecord

class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = '__all__'
        read_only_fields = ('borrowed_at', 'returned_at')