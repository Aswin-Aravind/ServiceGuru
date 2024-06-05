from django.shortcuts import render

from django.contrib.auth.models import User

from api.models import Customer

from api.serializers import CustomerSerializer

from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from rest_framework import status

from rest_framework import authentication,permissions



class CustomerViewSetView(ModelViewSet):

    serializer_class = CustomerSerializer

    queryset = Customer.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]


    def perform_create(self, serializer):
        serializer.save(technician=self.request.user)







