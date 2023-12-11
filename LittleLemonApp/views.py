from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# Create your views here.
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer

# @api_view()
# def menu_items(request):
#     items = MenuItem.objects.select_related('category').all()
#     serilized_item = MenuItemSerializer(items, many = True)
#     return Response(serilized_item.data)

# @api_view()
# def single_item(request, id):
#     items = get_object_or_404(MenuItem, pk=id)
#     serilized_item = MenuItemSerializer(items)
#     return Response(serilized_item.data)

@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many= True)
    return Response(serialized_item.data)

@api_view()
def single_items(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)