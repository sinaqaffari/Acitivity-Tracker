from rest_framework.views import APIView
from rest_framework.response import Response
from tracker.models import Activity
from django.db.models import Sum
from datetime import timedelta, datetime


class WeeklySummaryView(APIView):
    def get(self, request):
        user = request.user
        week_ago = datetime.now() - timedelta(days=7)
        data = Activity.objects.filter(user=user, timestamp__gte=week_ago)\
            .values('category')\
            .annotate(total=Sum('duration_minutes'))
        return Response(data)
    


    