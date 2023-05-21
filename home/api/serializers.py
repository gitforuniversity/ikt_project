from django.contrib.auth import get_user_model
from home.models import *
from rest_framework import serializers

User = get_user_model()


class SerialCategory(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    slug = serializers.SlugField(read_only = True)

    def create(self, validated_data):
        data = Categorie.objects.create(**validated_data)
        return data

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
class SerialActivity(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()

    def create(self, validated_data):
        data = Activitie.objects.create(**validated_data)
        return data

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class SerialUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SerialBlog(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date',]
    
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

class SerialTeacher(serializers.ModelSerializer):
    category = SerialCategory()
    teacher_activity = SerialActivity(many = True)

    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']
    
    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)
    
class SerialEvent(serializers.ModelSerializer):
    # teachers = SerialTeacher(many = True)
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']
    
    def create(self, validated_data):
        return Event.objects.create(**validated_data)

class SerialCourse(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']
    
    def create(self, validated_data):
        return Event.objects.create(**validated_data)

class SerialNotice(serializers.ModelSerializer):
    
    class Meta:
        model = Notice
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']
    
    def create(self, validated_data):
        return Event.objects.create(**validated_data)

class SerialResearch(serializers.ModelSerializer):

    class Meta:
        model = Research
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']
    
    def create(self, validated_data):
        return Event.objects.create(**validated_data)

class SerialScholarship(serializers.ModelSerializer):

    class Meta:
        model = Scholarship
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

