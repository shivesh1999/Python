from turtle import title
from rest_framework import serializers
from book_api.models import book

# serializer does the conversion of the data 
# this is defining it in our json response
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    published_date = serializers.DateField()
    quantity = serializers.IntegerField()

    # for handling the post request for create
    def create(self, data):
        return book.objects.create(**data)

    # for handing the update request 
    def update(self, instance, data):
        instance.title=data.get('title', instance.title)
        instance.number_of_pages=data.get('number_of_pages', instance.number_of_pages)
        instance.published_date=data.get('published_date', instance.published_date)
        instance.quantity=data.get('quantity', instance.quantity)
        instance.save()
        return instance


    
