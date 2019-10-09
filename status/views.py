from rest_framework import generics,mixins,permissions
from rest_framework.authentication import SessionAuthentication

from .models import Status
from .serializers import StatusSerializer

# Create your views here.
class StatusAPIView(mixins.CreateModelMixin,
    generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #authentication_classes = [SessionAuthentication]
    serializer_class = StatusSerializer

    def get_queryset(self):
        print(self.request.user)
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class StatusCreateAPIView(generics.CreateAPIView):
    #permission_classes = []
    #authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = []
    #authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer