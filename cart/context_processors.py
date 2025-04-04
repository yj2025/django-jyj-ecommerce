from .cart import Cart

def cart(request):

    # 세션 확인 테스트
    cart.decrypt_all_sessions()

    return {"cart": Cart(request)}