from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Category

from django.shortcuts import get_object_or_404
from rest_framework import status

# dev_32
from api.serializers.category_serializers import (
    CategorySerializer,
    CategorySimpleSerializer,
)

# dev_35
from rest_framework.views import APIView

# http://127.0.0.1:8000/api/categories/
# 방식   url         기능
# GET   categories/    list


# dev_32
@api_view(["GET"])
def categories_api(request):

    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


# dev_35


class CategoriesAPI(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySimpleSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def put(self, request):
        pass

    def delete(self, request):
        pass


class CategoryAPI(APIView):

    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySimpleSerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySimpleSerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        category.delete()
        return Response("삭제 성공", status=status.HTTP_204_NO_CONTENT)


# dev_36
# GenericAPIView: self.get_queryset()과 self.get_serializer()를 제공
# ListModelMixin: self.list() 내부에서 위의 메서드들을 호출
# 주의
# 기본적으로는 queryset, serializer_classs는 약속된 이름
# 대신 커스텀 마이징은 가능
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView


class CategoriesMixins(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryMixins(
    UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySimpleSerializer
    lookup_field = "name"

    def get(self, request, *args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
# dev_37
from rest_framework.generics import ListCreateAPIView

# generics.CreateAPIView : 생성
# generics.ListAPIView : 목록
# generics.RetrieveAPIView : 조회
# generics.DestroyAPIView : 삭제
# generics.UpdateAPIView : 수정
# generics.RetrieveUpdateAPIView : 조회/수정
# generics.RetrieveDestroyAPIView : 조회/삭제
# generics.ListCreateAPIView : 목록/생성
# generics.RetrieveUpdateDestroyAPIView : 조회/수정/삭제

class CategoriesGeneric(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated]

    # create 함수를 오버라이딩
    def create(self, request, args, **kwargs):
        name = request.data.get("name")

        # 같은 이름의 카테고리가 이미 존재할 경우 오류 메세지
        if Category.objects.filter(name=name).exists():
            raise ValidationError({"message": "같은 이름의 카테고리가 있습니다."})

        response = super().create(request,args, **kwargs)
        response.data = {
            "message": "카테고리가 성공적으로 생성 되었습니다.",
            "category": response.data,
        }

        return response
    
class CategoriesGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySimpleSerializer