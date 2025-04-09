from django.conf import settings
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from decimal import Decimal

# dev_18
from store.models import Product

# dev_23
from accounts.models import User


# dev_15
class Cart:  # 카트 클래스 생성

    # Cart 객체와 세션에 있는 Cart 객체를 연결 시킴
    def __init__(self, request):  # 객체 생성시 request 객체를 받도록 함

        self.session = request.session  # session 객체를 Cart 객체에 변수로 저장

        # dev_23
        # 로그인이 되어 있다면, 로그인 유저에 대한 정보를 빼내기 위하여...
        self.request = request

        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # session에 cart 객체가 없으면 session 객체에 cart 를 만듦
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    # dev_16
    # 리스트 컴프리 헨션
    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    # dev_21
    def get_product_total(self):
        return sum(
            item["quantity"] * Decimal(item["price"]) for item in self.cart.values()
        )

    # dev_18
    def __iter__(self):
        product_ids = self.cart.keys()  # ("1","2")

        # select * from product where id in ("1","2")
        products = Product.objects.filter(id__in=product_ids)

        # self.cart = {
        #          "1":{"quantity":7,"price":3000.00,"product": <Product: 상품1>, "total_price":21000 }
        #          "2":{"quantity":1,"price":5000.00,"product": <Product: 상품2> , "total_price":50000 }
        #        }
        for product in products:
            self.cart[str(product.id)]["product"] = product

        for item in self.cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]

            yield item  # 제너레이터 문법 return

    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)

        # self.cart = {
        #          "1":{"quantity":7,"price":"3000.00"}
        #          "2":{"quantity":1,"price":"5000.00"}
        #        }

        if product_id not in self.cart:
            # dev_21
            if product.is_sale:
                self.cart[product_id] = {
                    "quantity": 0,
                    "price": str(product.sale_price),
                }
            else:
                self.cart[product_id] = {"quantity": 0, "price": str(product.price)}

        if is_update:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        self.save()

    # dev_23
    def cart_to_db(self):

        if self.request.user.is_authenticated:  # 로그인이 되어 있는 유저라면
            current_user = User.objects.filter(id=self.request.user.id)
            # Convert {'3':1} to {"3":1}
            carty = str(self.cart)
            carty = carty.replace("'", '"')
            current_user.update(
                old_cart=str(carty)
            )  # ord_cart 에 장바구니 str 형태로 저장

    #     self.sesstion =request.sesssion = { 'cart':' {}(self.cart)  }
    #     self.cart = {
    #                       "1",{"quantity": 1, "price": "10000.00"}
    #                      "2":{"quantity":1,"price":"5000.00"}
    #                  }
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True  # 해당 세션을 DB에 저장
        # dev_23
        self.cart_to_db()

    # dev_19
    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # dev_24
    def get_cart(self):
        return self.cart

    def decrypt_all_sessions(self):
        """현재 DB에 저장된 모든 세션을 복호화하여 출력"""
        sessions = Session.objects.all()  # DB에서 모든 세션 조회

        if not sessions.exists():
            print("❌ 현재 저장된 세션이 없습니다.")
            return

        print(f"🔹 총 {sessions.count()}개의 세션을 찾았습니다.")

        for session in sessions:
            try:
                session_data = SessionStore(
                    session_key=session.session_key
                ).load()  # 세션 복호화
                print(f"✅ 세션 키: {session.session_key}\n   데이터: {session_data}\n")

            except Exception as e:
                print(f"❌ 복호화 실패 - 세션 키: {session.session_key}, 오류: {e}")