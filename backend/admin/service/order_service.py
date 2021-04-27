from admin.model import OrderDao

from utils.response import error_response
from utils.custom_exception import DataNotExists, DatabaseConnectFail, StartDateFail

import traceback
from datetime import timedelta, date

class OrderService:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance                      

    def __init__(self):
        self.order_dao = OrderDao()
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> Order 주문관리 진행중
    
<<<<<<< HEAD
>>>>>>> Modify: Directory 구조 변경 및 경로 수정정
    # 주문 조회
=======
>>>>>>> [Admin > order]
    def get_order_list(self, conn, params):
        """주문 조회 리스트 서비스

        주문 리스트 정보를 위해 model로 정보를 넘김
        
        Args:
            conn (Connection): DB 커넥션 객체
            params (dict): query parameter로 받은 정보 (셀러명, 조회 기간 등)
            
        Returns:
            order_list_info (dict) : 
                    order_list_info: 
                            order_list_info = {
                                    "order_list" : [
                                        {
                                            "color_id": 색상 아이디,
                                            "order_created_at": 주문 생성 날짜,
                                            "order_detail_number": 주문 상세 번호,
                                            "brand_name": 브랜드명,
                                            "order_number": 주문 번호,
                                            "order_status_type_id": 주문 상태 아이디,
                                            "order_username": 주문자명,
                                            "orderer_phone": 주문자 전화번호,
                                            "price": 상품 가격,
                                            "quantity": 구매 수량,
                                            "size_id": 사이즈 아이디,
                                            "product_name": 상품명
                                        } for result in order_detail
                                    ],
                                    "total_count": 주문 전체 수
                            }     
            500 : Exceptions  
                StartDateFail : 조회 날짜가 알맞지 않을 때 발생하는 에러
                KeyError : 데이터베이스의 key값이 맞지 않을 때 발생하는 에러
        """
        
        if 'end_date' in params:
            params['end_date'] +=  timedelta(days=1)
            params['end_date_str'] = params['end_date'].strftime('%Y-%m-%d')

        if 'start_date' in params:
            params['start_date_str'] = params['start_date'].strftime('%Y-%m-%d')

        if 'start_date' in params and 'end_date' in params and params['start_date'] > params['end_date']:
            raise StartDateFail('조회 시작 날짜가 끝 날짜보다 큽니다.')

        orders_info, order_count = self.order_dao.get_order_list(conn, params)
        
        order_list_info = {
                "order_list" : [
                    {
                        "color": result["color_name"],
                        "order_created_at": result["created_at"],
                        "order_detail_number": result["detail_order_number"],
                        "brand_name": result["korean_brand_name"],
                        "order_number": result["order_number"],
                        "order_status_type": result["order_status_type"],
                        "order_username": result["order_username"],
                        "orderer_phone": result["orderer_phone"],
                        "quantity": result["quantity"],
                        "size": result["size_name"],
                        "product_name": result["title"],
                        "total_price": int(result["price"] * result["quantity"]) if result["discount_rate"] == 0 else int(result["price"] * (1-result["discount_rate"]) * result["quantity"])
                    } for result in orders_info # 이름
                ],
                "total_count": order_count["count"]
        }
    
        return order_list_info


    def patch_order_status_type(self, conn, body):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        return order_dao.patch_order_status_type(conn, body)
    
    #배송완료, 상품준비, 전체상품, 노출상품
    def get_dashboard_seller(self, conn, account_id):
        return self.order_dao.get_dashboard_seller(conn, account_id)
        
=======
        return self.order_dao.patch_order_status_type(conn, body)
>>>>>>> Modify: Directory 구조 변경 및 경로 수정정
=======
        return self.order_dao.patch_order_status_type(conn, dbody)
>>>>>>> Order 주문관리 진행중
=======
        # DB에 없는 주문 상태를 전달할 때 -> dao에서 처리하기 or view 혹은 service에서 처리하기
=======
=======
        """주문 및 배송처리 함수

        json으로 받은 값을 바탕으로 주문 및 배송 처리하기 위한 함수

        Args:
            conn (Connection): DB 커넥션 객체
            body (json): 
                [
                    {"orders_detail_id" : 주문 상세 아이디, "order_status_type_id": 변경할 주문 상태 아이디},
                    {"orders_detail_id" : 주문 상세 아이디, "order_status_type_id": 변경할 주문 상태 아이디},
                    {"orders_detail_id" : 주문 상세 아이디, "order_status_type_id": 변경할 주문 상태 아이디}
                    ...
                ]

        Raises:
            DataNotExists: DB에 해당 id가 존재하지 않을 때 발생하는 에러

        Returns:
            impossible_to_patch (list) : 주문 상태를 변경하는데 실패한 값 반환
        """
        status_type_exist, status_type_not_exist = self.order_dao.check_if_status_type_exists(conn, body)

<<<<<<< HEAD
        appropriate_id = self.order_dao.check_appropriate_order_status_type(conn, body)
>>>>>>> [Admin > order]
=======
        possible_to_patch, impossible_to_patch = self.order_dao.check_if_possible_change(conn, status_type_exist)
>>>>>>> [Admin > order]

        impossible_to_patch += status_type_not_exist

<<<<<<< HEAD
        checked_current_order_status_list = self.order_dao.check_current_order_status(conn, body) 

<<<<<<< HEAD
>>>>>>> [Admin > order]
        # 주문 취소가 된 상품인 경우 -> 수정을 못하도록 에러발생
        # 이미 구매확정이 된 상품인 경우 -> 수정을 못하도록 에러발생
=======
>>>>>>> [Admin > order]
        possible_change_order_status = list()
        not_possible_change_order_status = list()
=======
        self.order_dao.patch_order_status_type(conn, possible_to_patch)
        # self.order_dao.insert_order_detail_history(conn, possible_to_patch)
        return impossible_to_patch
    
<<<<<<< HEAD
>>>>>>> [Admin > order]
        


        
=======
 
>>>>>>> [Admin > order]
    def get_order(self, conn, params):
        """주문 상세

        주문 상세 정보를 가져오는 함수

        Args:
            conn (Connection): DB 커넥션 객체
            params (dict): {"detail_order_number" : 주문 상세 번호}

        Returns:
            order_detail_info (dict) :         
                    order_detail_info = {
                        "order_detail": {
                            "order_number": 주문번호,
                            "order_detail_number": 주문상세번호,
                            "order_created_at": 주문발생 시간,
                            "order_status_type": 주문 상태,
                            "orderer_phone": 주문자 전화번호,
                            "orderer_name": 주문자명,
                            "product_id": 상품번호,
                            "price": 상품가격,
                            "discount_rate": 할인율,
                            "discounted_price": 할인된 가격,
                            "total_price": 총가격,
                            "product_name": 상품명,
                            "brand_name": 브랜드명,
                            "color": 색깔,
                            "size": 크기,
                            "quantity": 구매 수량,
                            "user_id": 사용자 id,
                            "recipient": 수령자명,
                            "zip_code": 우편번호,
                            "address": 주소 및 상세주소,
                            "recipient_phone": 수령자 전화번호,
                            "delivery_memo": 배송시 요청사항,
                        },
                        "order_history": [
                                    {
                                        "update_time": history["updated_at"],
                                        "order_status_type": history["order_status_type"]
                                    }
                                    for history in order_histories
                                ]
                }
        """
        order_detail, order_histories = self.order_dao.get_order(conn, params)

        order_detail_info = {
                "order_detail": {
                    "order_number": order_detail["order_number"],
                    "order_detail_number": order_detail["detail_order_number"],
                    "order_created_at": order_detail["created_at"],
                    "order_status_type": order_detail["order_status_type"],
                    "orderer_phone": order_detail["order_phone"],
                    "orderer_name": order_detail["orderer_name"],
                    "product_id": order_detail["product_id"],
                    "price": order_detail["price"],
                    "discount_rate": int(100 * order_detail["discount_rate"]),
                    "discounted_price": int(order_detail["price"] if order_detail["discount_rate"] == 0 else (order_detail["price"] * (1-order_detail["discount_rate"]))),
                    "total_price": int(order_detail["price"] * order_detail["quantity"] if order_detail["discount_rate"] == 0 else order_detail["price"] * (1-order_detail["discount_rate"]) * order_detail["quantity"]),
                    "product_name": order_detail["title"],
                    "brand_name": order_detail["korean_brand_name"],
                    "color": order_detail["color"],
                    "size": order_detail["size"],
                    "quantity": order_detail["quantity"],
                    "user_id": order_detail["user_id"],
                    "recipient": order_detail["recipient"],
                    "zip_code": order_detail["zip_code"],
                    "address": order_detail["address"]+" "+order_detail["detail_address"],
                    "recipient_phone": order_detail["recipient_phone"],
                    "delivery_memo": order_detail["delivery_memo_custom"] if order_detail["delivery_memo_custom"] else order_detail["delivery_memo"] if order_detail["delivery_memo"] else None,
                },
                "order_history": [
                            {
                                "update_time": history["updated_at"],
                                "order_status_type": history["order_status_type"]
                            }
                            for history in order_histories
                        ]
        }
        return order_detail_info
>>>>>>> [Admin > order_dao, order_service, order_view]
