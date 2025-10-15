from .serializers import ActivitySerializer
from rest_framework import viewsets
from .models import Activity


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    

    

