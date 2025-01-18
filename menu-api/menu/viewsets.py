# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from menu.models import Menu

from menu.serializers import MenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.published_all
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]