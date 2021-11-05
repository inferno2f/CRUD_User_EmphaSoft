from rest_framework import mixins, viewsets, permissions

from .models import User
from .permissions import IsAuthUserOrReadOnly
from .serializers import UserSerializer


class ListOrPostAPIView(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    ''' API that returns a list of all users or allows to create a new one '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetOrEditAPIView(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    '''
    API available only through Token auth
    Allows to retrieve, update or delete information about a user
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthUserOrReadOnly)
