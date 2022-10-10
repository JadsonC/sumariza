from .resumir import resumir, stopwords
from sumari.models import Sumari
from sumari.serializers import SumariSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class SumariViewSet(viewsets.ModelViewSet):
    queryset = Sumari.objects.all()
    serializer_class = SumariSerializer
    
    def create(self, request):
        request.data['resumo'] = resumir(request.data['link'], stopwords)
        serializer= SumariSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    