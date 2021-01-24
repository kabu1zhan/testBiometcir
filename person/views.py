from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Person
from .serializers import PersonSerializer
from .service import ageCalculate


class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def create(self, request, *args, **kwargs):
        '''Пост запрос для занесения иина в базу и счета возраста'''

        try:
            serialzer = self.get_serializer(data=request.data, many=False)
            serialzer.is_valid(raise_exception=True)
            age = ageCalculate.Age(iin=request.data['iin'])
            serialzer.save(age=age.getAge())
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        except:
            return Response('Вы ввели некорректный иин', status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        '''Get запрос в бд по иину и вывод иина и возраста'''

        person = Person.objects.get(iin=kwargs['pk'])
        serialzer = self.get_serializer(person, many=False)
        if serialzer.data:
            return Response(serialzer.data, status=status.HTTP_200_OK)
        else:
            return Response('Данный иин не найден', status=status.HTTP_404_NOT_FOUND)

