from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import HeatData
from ..serializers.heat_data import HeatDataSerializer


@api_view(["GET"])
def get(request: Request):
    limitParam = request.query_params.get("limit", "")
    limit = int(limitParam) if limitParam.isdecimal() else None
    datas = HeatData.objects.all()

    if (limit is not None):
        datas = reversed(HeatData.objects.all().order_by("-id")[:limit])

    serializer = HeatDataSerializer(datas, many=True)

    return Response(serializer.data)
