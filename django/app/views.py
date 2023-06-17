from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def helloWorld(request: Request):
    return Response("Hello World!")
