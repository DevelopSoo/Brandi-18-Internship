from flask.views import MethodView
from flask import request, jsonify
from flask_request_validator import Param, Pattern, JSON, validate_params, ValidRequest
from flask_request_validator.error_formatter import demo_error_formatter
from flask_request_validator.exceptions import InvalidRequestError, InvalidHeadersError, RuleError

from connection import get_connection

class AccountSignUpView(MethodView):
    def __init__(self, service):
        self.service = service
    # account 회원가입
    # router => class => validate_params
    # rules 최상단에서 에러 처리
    # 최종적인 메시지 처리는 최상단에서
    @validate_params(
        Param('id', JSON, str, rules=[Pattern("^[a-z]+[a-z0-9]{4,19}$")], required=True),
        Param('password', JSON, str, rules=[Pattern('^[A-Za-z0-9@#!$]{6,12}$')], required=True),
        Param('phone', JSON, str, required=True),
        Param('sub_property_id', JSON, int, required=True),
        Param('korean_brand_name', JSON, str, required=True, rules=[Pattern('[가-힣0-9]+')]),
        Param('english_brand_name', JSON, str, required=True, rules=[Pattern('[a-zA-Z0-9]+')]),
        Param('customer_center_number', JSON, str, required=True)
    )
    def post(self, valid: ValidRequest):
        conn = None
        try:
            body = valid.get_json()
            conn = get_connection()
            if conn:
                self.service.post_account_signup(conn, body)
            conn.commit()    
            return jsonify('성고고고고고고공'), 200
        except Exception as e:
            if conn:
                conn.rollback()
            raise e
        
        finally:
            if conn:
                conn.close()

class AccountLogInView(MethodView):
    def __init__(self, service):
        self.service = service
    
    # seller or master 로그인
    def post(self):
        conn = None
        try:
            body = request.data
            conn = get_connection()
            if conn:
                result = self.service.post_account_login(conn, body)
                
            conn.commit()

            return jsonify('access_token'), 200

        finally:
            conn.close()