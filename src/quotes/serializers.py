from rest_framework import serializers
from .models import Quote, Author

class QuoteSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Quote
        fields = ("created", "author", "quotation",)

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("name",)