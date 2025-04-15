from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Product
from api.serializers import ProductSerializer


# http://127.0.0.1:8000/api/products/
# 방식   url         기능
# GET   products/    list
# POST  products/   create


# dev_29
@api_view(["GET", "POST"])
def products_api(request):

    if request.method == "GET":
        products = Product.objects.all()
        # many=True ➜ 여러 개의 인스턴스 (QuerySet, 리스트 등)
        # many=False (기본값) ➜ 단일 인스턴스
        serializer = ProductSerializer(products, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    # dev_30
    # 디시리얼라이져
    if request.method == "POST":
        print(request.data)
        serializer = ProductSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)