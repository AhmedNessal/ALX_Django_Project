from pytz import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from books.models import Book
from .models import BorrowRecord
from .serializers import BorrowRecordSerializer

class CheckoutBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        book_id = request.data.get('book_id')
        try:
            book = Book.objects.get(id=book_id, available=True)
        except Book.DoesNotExist:
            return Response({"error": "Book not available"}, status=status.HTTP_400_BAD_REQUEST)

        borrow = BorrowRecord.objects.create(book=book, user=request.user)
        book.available = False
        book.save()

        serializer = BorrowRecordSerializer(borrow)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ReturnBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        borrow_id = request.data.get('borrow_id')
        try:
            borrow = BorrowRecord.objects.get(id=borrow_id, user=request.user, returned_at__isnull=True)
        except BorrowRecord.DoesNotExist:
            return Response({"error": "No active borrow record found"}, status=status.HTTP_400_BAD_REQUEST)

        borrow.returned_at = timezone.now() # type: ignore
        borrow.save()

        borrow.book.available = True
        borrow.book.save()

        serializer = BorrowRecordSerializer(borrow)
        return Response(serializer.data, status=status.HTTP_200_OK)