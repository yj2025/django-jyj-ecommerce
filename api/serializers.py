from rest_framework import serializers
from store.models import Category, Product

# 2. Serilaizer 객체의 주요 기능
# 1) serialization
# 2) deserialiaztion
# 3) validation
# 4) create(), update()     request / response 데이터 핸들링 ( to_internal_value() / to_representation() )
# 5) nested serialization

# dev_33
# ✅ 주의할 점
# depth는 읽기 전용 출력.
# POST, PUT 요청에서 중첩된 객체를 직접 생성하거나 수정 불가
# 만약 쓰기도 원한다면 category_id 같은 별도 필드와 create() 오버라이드가 여전히 필요해요.


# 객체를 => 딕셔너리로 만드는게 목적


# 순환 참조 방지
class CategorySerializer(serializers.ModelSerializer):
    # dev_32 역방향 참조
    # products = ProductSerializer(many=True, read_only=True)  # related_name=products

    class Meta:
        model = Category
        fields = "__all__"


# dev_33


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # dev_33 write 을 할려면

    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["id", "name", "category"]
        # dev_32 ForeignKey 필드 자동 직렬화
        # ForeignKey에 해당 되는 모델을 시리얼라이즈로 만들필요 없이 자동으로 직렬화(json) 해줌
        # 단점: depth 가 깊어 지면 속도에 문제가 생김
        # 기본적으로 read_only 임
        # depth = 1

    #     {
    # "category": {
    # #         "name": "과일"
    # #     },
    #     "name": "오렌지",
    #     "price": "12000.00",
    #     "description": "파이썬 책입니다.",
    #     "image": null,
    #     "is_sale": false,
    #     "sale_price": 0
    # }
    #

    # def create(self, validated_data):
    #     category_data = validated_data.pop("category")

    #     # 카테고리 저장/조회
    #     category, _ = Category.objects.get_or_create(**category_data)
    #     product = Product.objects.create(**validated_data, category=category)

    #     return product