import factory.fuzzy
import uuid
from django.utils import timezone
from users.models import User, Device
from group.models import 필요한모델들

from django.contrib.auth.hashers import make_password


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ["nickname"]

    nickname = factory.Faker("name")
    password = make_password("test001!")
    email = factory.lazy_attribute(lambda a: f"{a.nickname.strip()}@test.com")
    username = factory.lazy_attribute(lambda a: f"{a.nickname.strip()}@test.com")
    createdAt = timezone.now()
    updatedAt = timezone.now()


class UserDeviceFactory(factory.django.DjangoModelFactory):
    class Meta:
        odel = Device
        django_get_or_create = ["id"]

    user = factory.SubFactory(UserFactory)
    id = factory.Faker("name")
    필요한 = "데이터"
    기타 = "등등"
    입니다 = factory.Faker("pystr")
