from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):

    def get(self, request, format='XML'):
        an_api = [
            'sadasd'
        ]
        return Response({'message': 'hello', 'an_api': an_api})