from rest_framework.exceptions import APIException


class QuestionNotFound(APIException):
    status_code = 409
    default_detail = '해당 id를 가진 질문이 Database 내 존재하지 않습니다. 요청 question id를 다시 한 번 확인해주세요.'