
# import re
# from book_api.models import book
# from book_api.serializer import BookSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# # Create your views here.

# # for setting up the type of request we add this api_view 
# @api_view(['GET'])
# def book_list(request):
#     books = book.objects.all()
#     # books_python = list(books.values())
#     # return JsonResponse({
#     #     'books': books_python
#     # })
#     # many=True when you want to serialize many objects
#     serializer=BookSerializer(books,many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def book_create(request):
#     serializer= BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def Book(request,pk):
#     try:
#         selected_book=book.objects.get(pk=pk)
#     except:
#         return Response({
#             'error': 'Book does not exist'
#         },status=status.HTTP_404_NOT_FOUND)
#     if request.method =='GET':        
#         serializer=BookSerializer(selected_book)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer=BookSerializer(instance=selected_book,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return serializer.errors

#     if request.method=='DELETE':
#         selected_book.delete()
#         serializer=BookSerializer(selected_book)
#         return Response(status=status.HTTP_200_OK)
    
from rest_framework.views import APIView
from book_api.models import book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

class BookList(APIView):
    def get(self,request):
        books = book.objects.all()
        # books_python = list(books.values())
        # return JsonResponse({
        #     'books': books_python
        # })
        # many=True when you want to serialize many objects
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)