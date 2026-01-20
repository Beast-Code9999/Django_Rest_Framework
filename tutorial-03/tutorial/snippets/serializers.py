from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# class SnippetSerializer(serializers.Serializer):
#     # Define how each field should be validated when converting JSON ↔ Python objects
    
#     id = serializers.IntegerField(read_only=True)  # Auto-generated, users can't set this
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)  # Optional field
#     code = serializers.CharField(style={"base_template": "textarea.html"})  # Display as textarea in browser
#     linenos = serializers.BooleanField(required=False)  # Show line numbers? Optional, defaults to False
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="python")  # Must pick from list
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")  # Must pick from list

#     def create(self, validated_data):
#         """
#         Called when POST request creates a new snippet.
#         validated_data = dict of clean data that passed validation
#         """
#         return Snippet.objects.create(**validated_data)  # Save to database

#     def update(self, instance, validated_data):
#         """
#         Called when PUT/PATCH request updates existing snippet.
#         instance = existing Snippet object from database
#         validated_data = dict of new data
#         """
#         # Update each field: use new value if provided, otherwise keep old value
#         instance.title = validated_data.get("title", instance.title)
#         instance.code = validated_data.get("code", instance.code)
#         instance.linenos = validated_data.get("linenos", instance.linenos)
#         instance.language = validated_data.get("language", instance.language)
#         instance.style = validated_data.get("style", instance.style)
#         instance.save()  # Save changes to database
#         return instance

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style"]
