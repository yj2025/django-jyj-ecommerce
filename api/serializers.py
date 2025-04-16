from rest_framework import serializers
from store.models import Category, Product

# 2. Serilaizer 객체의 주요 기능
# 1) serialization
# 2) deserialiaztion
# 3) validation
# 4) request / response 데이터 핸들링 ( to_internal_value() / to_representation() )
# 5) nested serialization


# dev_29
# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     price = serializers.ImageField()
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#     description = serializers.CharField(
#         max_length=250, required=False, allow_blank=True, allow_null=True
#     )
#     image = serializers.ImageField()
#     is_sale = serializers.BooleanField()
#     sale_price = serializers.IntegerField()


# dev_32


# 객체를 => 딕셔너리로 만드는게 목적
#
class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["id", "name", "category"]
        # dev_32 ForeignKey 필드 자동 직렬화
        # ForeignKey에 해당 되는 모델을 시리얼라이즈로 만들필요 없이 자동으로 직렬화(json) 해줌
        # 단점: depth 가 깊어 지면 속도에 문제가 생김
        # 기본적으로 read_only 임
        # depth = 1


class CategorySerializer(serializers.ModelSerializer):
    # dev_32 역방향 참조
    products = ProductSerializer(many=True, read_only=True)  # related_name=products

    class Meta:
        model = Category
        fields = "__all__"