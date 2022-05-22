
from rest_framework.views import APIView

from .serializers import CommentSerializer

from rest_framework.response import Response



class CommentsAPIView(APIView):
    def post(self,request):
        serializer=CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
   