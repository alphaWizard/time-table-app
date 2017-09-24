from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import subject
from .serializers import subjectSerializer



class routinedata(generics.ListAPIView):


    def get_queryset(self):

         dayvalue= self.kwargs['dayvalue']
         periodvalue= self.kwargs['periodvalue']
         return subject.objects.filter(day__dayname__exact=dayvalue,period__periodname__exact=periodvalue)


    serializer_class = subjectSerializer
