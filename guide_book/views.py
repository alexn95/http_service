from rest_framework.response import Response
from rest_framework.views import APIView


class NextTaskView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        # тут будет логика из service
        return Response(data)
