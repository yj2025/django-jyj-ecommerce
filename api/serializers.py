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


# 객체를 => 딕셔너리로 만드는게 목적
#
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["id", "name", "category"]

    # dev_31
    # 가격은 0 이상 10,000 이하
    def validate_price(self, value):

        if value < 0:
            raise serializers.ValidationError("가격은 0 이상이어야 합니다.")

        if value > 100000:
            raise serializers.ValidationError("가격은 10만원 이하여야 합니다.")

        return value

    # 이름은 3자 이상 100자 이하
    def validate_name(self, value):
        if len(value.strip()) < 3:  # 문자열 양끝 공백 제거
            raise serializers.ValidationError("상품 이름은 최소 3자 이상이어야 합니다.")

        if len(value.strip()) > 100:
            raise serializers.ValidationError("상품 이름은 100자를 초과 할수 없습니다.")

        return value
    
    