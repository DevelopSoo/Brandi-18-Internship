from .product_view import (
                            ProductView, 
                            ProductDetailView, 
                            ProductCategoryView,
                            ProductSellerView,
                            ProductSellerSearchView,
                            ProductColorView,
                            ProductSizeView
)

from .order_view import (
                            DashboardSellerView,
                            OrderListView,
                            OrderView
)

from .account_view import (
                            AccountSignUpView,
                            AccountLogInView
)

from utils.error_handler import error_handle

def create_endpoints(app, services):
    product_service = services.product_service
    order_service = services.order_service
    account_service = services.account_service

    # product
    app.add_url_rule("/products",
                    view_func=ProductView.as_view('product_view', product_service), 
                    methods=['GET','POST', 'PATCH'])

    app.add_url_rule("/products/<product_code>", 
                    view_func=ProductDetailView.as_view('product_detail_view', product_service), 
                    methods=['GET'])

    app.add_url_rule("/products/seller/<int:category_id>", 
                    view_func=ProductCategoryView.as_view('product_category_view', product_service), 
                    methods=['GET'])

    app.add_url_rule("/products/seller/<int:seller_id>",
                    view_func=ProductSellerView.as_view('product_seller_view', product_service),
                    methods=['GET'])

    app.add_url_rule("/products/seller", 
                    view_func=ProductSellerSearchView.as_view('product_seller_search_view', product_service), 
                    methods=['GET'])

    app.add_url_rule("/products/color",
                    view_func=ProductColorView.as_view('product_color_view', product_service),
                    methods=['GET'])
    
    app.add_url_rule("/products/size",
                    view_func=ProductSizeView.as_view('product_size_view', product_service),
                    methods=['GET'])

    # order
<<<<<<< HEAD
    app.add_url_rule("/order",
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> Order 주문관리 진행중
=======
    app.add_url_rule("/orders",
>>>>>>> [Admin > order_dao, order_service, order_view]
                    view_func=OrderListView.as_view('order_list_view', order_service),
                    methods=['GET'])
    
    app.add_url_rule("/order/delivery",
<<<<<<< HEAD
=======
                    view_func=OrderListView.as_view('order_view', order_service),
                    methods=['GET'])
    
    app.add_url_rule("/orders",
>>>>>>> [상품관리 > 상품리스트]
=======
>>>>>>> Order 주문관리 진행중
                    view_func=OrderListView.as_view('order_delivery_view', order_service),
                    methods=['PATCH'])

    app.add_url_rule("/dashboard/seller",
                    view_func=DashboardSellerView.as_view('dashboard_seller', order_service),
                    methods=['GET'])
    
    app.add_url_rule("/order",
                    view_func=OrderView.as_view('order_view', order_service),
                    methods=['GET'])
                    
    # account
    app.add_url_rule("/account/signup",
                    view_func=AccountSignUpView.as_view('account_signup_view', account_service),
                    methods=['POST'])
    
    app.add_url_rule("/account/login",
                    view_func=AccountLogInView.as_view('account_login_view', account_service),
<<<<<<< HEAD
<<<<<<< HEAD
                    methods=['POST'])
<<<<<<< HEAD
<<<<<<< HEAD
    
    app.add_url_rule("/seller/signin",
                    view_func=AccountLogInView.as_view('seller_login_view', account_service),
<<<<<<< HEAD
                    methods=['POST'])
    
    
    error_handle(app)
=======
>>>>>>> Add : 회원가입 API 작성중
    
=======
                    methods=['POST'])
>>>>>>> Modify : 디렉토리 수정, gitignore에 .vscode 추가
=======
                    methods=['POST'])
    
>>>>>>> Modify : import 경로 문제 수정
=======
    
    error_handle(app)
    
>>>>>>> [error_handle 작성]
=======
                    methods=['POST'])
>>>>>>> MOD: minor changes
