from rest_framework import serializers
from store.models import Category, Product

# **Serilaizer 객체의 주요 기능
# ✔️ 1) Serialization
# → Python 객체 (ex. 모델 인스턴스)를 JSON 같은 포맷으로 변환
# → 내부적으로 to_representation() 사용

# ✔️ 2) Deserialization
# → JSON 같은 입력 데이터를 Python 객체로 변환
# → 내부적으로 to_internal_value() 사용

# ✔️ 3) Validation
# → .is_valid() 호출 시 필드 검증 수행
# → validate_<field>(), validate() 메서드로 커스텀 검증 가능

# ✔️ 4) create(), update()     request / response 데이터 핸들링 ( to_internal_value() / to_representation() )

# ✔️ 5) Nested Serialization
# → 관계 모델을 중첩 구조로 표현
# → 예: ForeignKey, ManyToMany 필드를 다른 시리얼라이저로 감싸 표현



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

# 객체 => 딕셔너리로 만드는게 목적
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
    products = ProductSerializer(many=True, read_only=True)  # related_name=products # 여기서 중첩

    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        category_data = validated_data.pop("category")
        category, _ = Category.objects.get_or_create(**category_data)