import datetime
import unittest

from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from firebase_admin import auth
import firebase_admin
from firebase_admin import credentials


class TestUserManagement(APITestCase):

    cred = credentials.Certificate("C:\\Users\\rnlgksclsrn\\.ssh\\moodie_firebase_auth_private_key.json")
    default_app = firebase_admin.initialize_app(cred)
    fake = Faker()

    def setUp(self):
        self.factory = APIRequestFactory()
        self.name = self.fake.name()
        self.email = self.fake.email()
        self.password = self.fake.password()

    def tearDown(self):
        fake = Faker()

    def test_create_user(self):
        # 회원 가입 테스트 코드

        # Given - 이메일, 이메일 인증 정보, 비밀번호, 활동여부

        # When - 회원가입을 요청하면 이메일 중복 여부를 판단한 후, 회원가입 성공 및 실패 여부를 반환한다.
        user = auth.create_user(
            display_name=self.name,
            email=self.email,
            email_verified=False,
            password=self.password,
            disabled=False)

        # Then - 성공해야 한다.
        self.assertEqual(user.email, self.email)

    def test_update_user(self):
        # 회원 정보 전체 수정.

        # Given 유저의 uid

        # When 유저 정보 새로 수정할 때.
        for user in auth.list_users().iterate_all():
            user = auth.update_user(
                user.uid,
                display_name=self.name,
                email=self.email,
                email_verified=False,
                password=self.password,
                disabled=False)

            # Then - 성공해야 한다.
            self.assertEqual(user.email, self.email)

    def test_search_user(self):
        # 유저 uid로 유저 정보 조회 Test

        # Given - 유저 정보.

        # When 회원 가입 후, 마이 페이지에서 계정 정보 조회 시.
        user = auth.create_user(
            display_name=self.name,
            email=self.email,
            email_verified=False,
            password=self.password,
            disabled=False)

        # Then - 가입에 사용했던 이메일을 반환한다.
        self.assertEqual(user.email, auth.get_user(user.uid).email)

    @unittest.skip
    def test_delete_user_all(self):
        # 회원 전체 삭제 테스트
        for user in auth.list_users().iterate_all():
            auth.delete_user(user.uid)

    def test_verify_id_token(self):
        # firebase ID token verify 테스트
        id_token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImIwNmExMTkxNThlOGIyODIxNzE0MThhNjdkZWE4Mzc0MGI1ZWU3N2UiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbW9vZGllLWRhMzY4IiwiYXVkIjoibW9vZGllLWRhMzY4IiwiYXV0aF90aW1lIjoxNjQ4MTkxODQ3LCJ1c2VyX2lkIjoiaDNqRDZ3ZVFqdFdpYzAwTXVkemMySlNWV0cwMyIsInN1YiI6ImgzakQ2d2VRanRXaWMwME11ZHpjMkpTVldHMDMiLCJpYXQiOjE2NDgyMDA5MDQsImV4cCI6MTY0ODIwNDUwNCwiZW1haWwiOiJkb25nZG9uZ0BuYXZlci5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiZG9uZ2RvbmdAbmF2ZXIuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.NNSnUgofaSIWXOJokJa1RtYEK5f7hImScJtsfe80oMbpJGVxxhiZcD-bo5WJOVDyB53NBCPt7naNIrczRA68y73RsSdAUhvGM2qMVNEEgpqlVgvaJNmcT4T4DoAu8YJem63KPJj1hjbNylyfZ_s7ABTF9XRwdyrEt4DpF3-zxChk1QtUL49DN71O2TXXCBx_ej-2k2hGAVKRicKVi3YYsKvhlXP8-5opiAaadk5xR8FXTQd1ECTL73leAfNB04zWcsraNUwv1urz8uxEVLKLlQConTSy9ZdMgiou50lBM4c74eATz0veR6HFRH8XuznBuAxrhjJV8R3cQbS2MfNBXA'
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        self.assertEqual(
            auth.get_user(uid).email, "dongdong@naver.com")

    def test_set_admin_clam(self):
        id_token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImIwNmExMTkxNThlOGIyODIxNzE0MThhNjdkZWE4Mzc0MGI1ZWU3N2UiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbW9vZGllLWRhMzY4IiwiYXVkIjoibW9vZGllLWRhMzY4IiwiYXV0aF90aW1lIjoxNjQ4MTkxODQ3LCJ1c2VyX2lkIjoiaDNqRDZ3ZVFqdFdpYzAwTXVkemMySlNWV0cwMyIsInN1YiI6ImgzakQ2d2VRanRXaWMwME11ZHpjMkpTVldHMDMiLCJpYXQiOjE2NDgyMDA5MDQsImV4cCI6MTY0ODIwNDUwNCwiZW1haWwiOiJkb25nZG9uZ0BuYXZlci5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiZG9uZ2RvbmdAbmF2ZXIuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.NNSnUgofaSIWXOJokJa1RtYEK5f7hImScJtsfe80oMbpJGVxxhiZcD-bo5WJOVDyB53NBCPt7naNIrczRA68y73RsSdAUhvGM2qMVNEEgpqlVgvaJNmcT4T4DoAu8YJem63KPJj1hjbNylyfZ_s7ABTF9XRwdyrEt4DpF3-zxChk1QtUL49DN71O2TXXCBx_ej-2k2hGAVKRicKVi3YYsKvhlXP8-5opiAaadk5xR8FXTQd1ECTL73leAfNB04zWcsraNUwv1urz8uxEVLKLlQConTSy9ZdMgiou50lBM4c74eATz0veR6HFRH8XuznBuAxrhjJV8R3cQbS2MfNBXA'
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        auth.set_custom_user_claims(uid, {'admin': True})
        self.assertEqual(auth.get_user(uid).email, "dongdong@naver.com")

