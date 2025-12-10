from rest_framework import serializers
from ..models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'body', 'publisher', 'author']
        read_only_fields = ['id']

