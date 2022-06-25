# import datetime
#
# from django.urls import reverse
# from faker import Faker
# from freezegun import freeze_time
# from django.utils import timezone
# from rest_framework import status
# from rest_framework.test import APITestCase, APIRequestFactory
#
#
# class UserManagement(APITestCase):
#     # Question :
#     # APIRequestFactory? - Test module이 url로 요청할 수 있게 만듦.
#     # Client? - 클라이언트 객체를 의미. test module에서 가볍게 만들어 쓸 수 있도록 지원
#     # Factory Boy? - 객체 생성 및 불러오기, 객체 상태 재 정의를 가능하게 해주는 lib
#
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.test_url = "테스트하고싶은url"
#         # HTTP_AUTHORIZATION을 위해 사용
#         self.register_url = "회원가입url"
#         self.login_url = "로그인url"
#         # url 속성 예시
#         self.url = reverse('sentiment')
#
#         # 회원가입 하기
#         self.user_data = {"email": "test@test.com", "password": "test001!", "nickname": "test_nickname",
#                           "회원가입에필요한데이터": "기타등등등", }
#         self.client.post(self.register_url, data=self.user_data)
#
#         # 로그인 하기
#         self.access_token = self.client.post(self.auth_url, {"email": self.user_data.get("email"),
#                                                              "password": self.user_data.get("password"), }, ).data.get(
#             "token")
#
#         # 인증 하기
#         self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token['access_token']}")
#
#     # 그룹을 생성하는 코드 테스트 -> 만약 테스트 코드가 많아지면 헷갈릴 수 있으니 이름으로 부족할 것 같으면 주석 작성
#     def test_create_group(self):
#         # 1. Given
#         data = {"그룹을": False, "생성할": ["TestTest"], "때": "TestTest", "필요한": "TestTest", "데이터": "😄",
#                 "들입니다": ["TestTest", "TestTest", ], "ㅎㅎ": "TestTest", }
#         # 2. When
#         response = self.client.post(self.create_url, data=data, format="json")
#
#         # 3. Then
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     # 권한을 바꾸는 메소드
#     def change_authorization(self, client_user):
#         access_token = self.client.post(self.auth_url,
#                                         {"email": client_user.email,
#                                          "password": "test001!", }, ).data.get("token")
#
#         self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token['access_token']}")
#
#     # 시간 설정 테스트 코드
#     # def test_check_5_combo(self):
#     #     fake = Faker()
#     #     user = User.objects.get(nickname="test_nickname")
#     #     datetimes = (datetime.datetime(2021, 11, day) for day in range(26, 31))
#     #     for now_date in datetimes:
#     #         with freeze_time(now_date):
#     #             # print(timezone.now())
#     #             id = fake.word()
#     #             data = {"data": [{"date": int(timezone.now()), "기타": "등등", "데이터가": "여러가지", "있습니다": "각자",
#     #                               "알맞은": "데이터넣어서진행", }], }
#     #             self.client.patch(self.url, data=data, format="json")
