from rest_framework import viewsets, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']