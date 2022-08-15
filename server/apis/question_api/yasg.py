from drf_yasg import openapi


def response_schema_for_get_question_list():
    response_schema_dict = {
        "200": openapi.Response(
            description="질문 목록 조회 요청에 성공했을 경우",
            examples={
                "application/json": {

                    "result": [
                        {
                            "id": 2,
                            "title": "오늘 저녁은 뭐 먹었어?"
                        },
                        {
                            "id": 3,
                            "title": "오늘 아침은 뭐야?"
                        },
                        {
                            "id": 4,
                            "title": "오늘 간식은 뭐야?"
                        },
                        {
                            "id": 5,
                            "title": "string"
                        }
                    ]

                }
            }
        ),
    }
    return response_schema_dict


def response_schema_for_get_question_detail():
    response_schema_dict = {
        "200": openapi.Response(
            description="질문 상세 조회 요청에 성공했을 경우",
            examples={
                "application/json": {
                    "result":
                        {
                            "title": "오늘 저녁은 뭐 먹었어?"
                        }
                }
            }
        ),
        "409": openapi.Response(
            description="없는 질문에 대한 조회 요청을 했을 경우",
            examples={
                "application/json": {

                    "detail": "해당 id를 가진 질문이 Database 내 존재하지 않습니다. 요청 question id를 다시 한 번 확인해주세요.",
                    "status_code": 409

                }
            }
        )
    }
    return response_schema_dict
