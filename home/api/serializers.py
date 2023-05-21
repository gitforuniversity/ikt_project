from django.contrib.auth import get_user_model
from home.models import *
from rest_framework import serializers

User = get_user_model()

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


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
    img = Base64ImageField(max_length = None, use_url = True)
    cover_img = Base64ImageField(max_length = None, use_url = True)

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