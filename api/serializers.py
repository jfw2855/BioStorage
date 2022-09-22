from django.contrib.auth import get_user_model
from rest_framework import serializers

#model imports
from .models.experiment import Experiment
from .models.storage import Storage
from .models.storage_type import StorageType
from .models.manufacturer import Manufacturer
from .models.category import Category
from .models.container import Container
from .models.item_type import ItemType
from .models.item import Item

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = '__all__'

class StorageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageType
        fields = '__all__'


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

class ReadStorageSerializer(serializers.ModelSerializer):
    storage_type = StorageTypeSerializer()    #populates foreign key fields of storage_type
    class Meta:
        model = Storage
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'

class ReadContainerSerializer(serializers.ModelSerializer):
    storage_id = ReadStorageSerializer()    #populates foreign key fields of storage
    class Meta:
        model = Container
        fields = '__all__'

class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # This model serializer will be used for User creation
    # The login serializer also inherits from this serializer
    # in order to require certain data for login
    class Meta:
        # get_user_model will get the user model (this is required)
        # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5 } }

    # This create method will be used for model creation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserRegisterSerializer(serializers.Serializer):
    # Require email, password, and password_confirmation for sign up
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=40)

    def validate(self, data):
        # Ensure password & password_confirmation exist
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Please include a password and password confirmation.')

        # Ensure password & password_confirmation match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Please make sure your passwords match.')
        # if all is well, return the data
        return data

class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)


class ReadItemSerializer(serializers.ModelSerializer):
    item_type = ItemTypeSerializer()
    category_id = CategorySerializer()
    container_id = ReadContainerSerializer()
    manufacturer_id = ManufacturerSerializer()
    storage_id = StorageSerializer()
    exp_id = ExperimentSerializer()
    owner = UserSerializer()
    class Meta:
        model = Item
        fields = '__all__'