# dev_15
from django.conf import settings


class Cart(): # 카트 클래스 생성

    # Cart 객체와 세션에 있는 Cart 객체를 연결 시킴
    
    def __init__(self, request): # 객체 생성 시 request 객체를 받도록 함
        
        self.session = request.session # session 객체를 Cart 객체에 변수로 저장

        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # session에 cart 객체가 없으면 session 객체에 cart를 만듦
            cart = self.session[settings.CART_SESSION_ID]

        self.cart = cart

    def __len__(self):
        pass

    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {"quantity":0,"price":str(product.price)}

        if is_update:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        self.save()