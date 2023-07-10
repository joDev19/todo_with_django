from rest_framework import serializers
from todo.models import Todo, LANGUAGE_CHOICES, STYLE_CHOICES

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    done = serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new `Todo` instance, given the validated data.
        """
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Todo` instance, given the validated data.
        """ 
        instance.name = validated_data.get('name', instance.name)
        instance.done = validated_data.get('done', instance.done)
        instance.save()
        return instance
    
