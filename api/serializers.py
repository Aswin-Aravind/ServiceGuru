from django.contrib.auth.models import User

from api.models import Customer

from rest_framework import serializers






class CustomerSerializer(serializers.ModelSerializer):

    technician = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Customer

        fields = "__all__"

        read_only_fields = ["id","technician","status","created_date","updated_date","is_active"]