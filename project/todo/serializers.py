from rest_framework import serializers
from todo.models import Todo, LANGUAGE_CHOICES, STYLE_CHOICES, Customer
from passlib.hash import sha256_crypt

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
    

class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Customer` instance, given the validated data.
        """
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        password = validated_data.get('password', instance.password)
        instance.password = hashed = sha256_crypt.using(rounds=5000).hash(password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

