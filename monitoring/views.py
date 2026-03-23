from rest_framework.generics import CreateAPIView,UpdateAPIView,ListAPIView
from .models import Keyword, Flag
from .serializers import KeywordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .services.scanner import load_mock_data, run_scan
from .serializers import FlagSerializer
from django.utils.timezone import now

class KeywordCreateView(CreateAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class ScanView(APIView):
    def post(self, request):
        content_items = load_mock_data()
        run_scan(content_items)
        return Response({"message": "Scan completed"})
    
class FlagListView(ListAPIView):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer

class FlagUpdateView(UpdateAPIView):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Set reviewed_at when status changes
        instance.reviewed_at = now()
        instance.save()
 
