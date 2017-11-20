"""
1. error_messages 보다 validate 에러 우선



필드에 사용가능한것 : https://marshmallow.readthedocs.io/en/latest/api_reference.html#module-marshmallow.exceptions


validate = Length(min, max, error), Email, Equal(comparable), OneOf, Range(min,max), URL
Field = default, attribute, load_from, dump_to, required, allow_none, load_only, dump_only, missing

Decorators 쓰면 세세한 에러같은거 추가가능(이메일 자리수가3자 미만이면 3자 이상이어야한다 등등)

키값 알파벳순으로 정
"""

import datetime
from marshmallow import Schema, fields, pprint
from collections import OrderedDict

class Album(object):
    def __init__(self, title, release_date, email, name, password, isSuperUser, age):
        self.title = title
        self.release_date = release_date
        self.email = email
        self.name = name
        self.created_at = datetime.datetime.now()
        self.password=password
        self.isSuperUser = isSuperUser
        self.age = age

class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()

    name = fields.String(required=True)
    # age = fields.Integer(
    #     required=True,
    #     validate=lambda n: 18 <= n <= 40,
    #     error_messages={'required': 'Age is required.'}
    # )
    age = fields.Number(
        required=True,
        validate=lambda n: 18 <= n <= 40,
        error_messages={'required': {'message': 'valueError', 'code': 300}}
    )

    city = fields.String(
        required=True,
        error_messages={'required': {'message': 'City required', 'code': 400}}
    )
    email = fields.Email()

    # 함수적용가능
    uppername = fields.Function(lambda obj: obj.name.upper())
    date_created = fields.DateTime(attribute="created_at", format="%Y-%m-%d %H:%M:%S")


    password = fields.Str(load_only=True) # 값이 있으면 건너뛰고 보여주지않음
    #created_at = fields.DateTime(dump_only=True) # 값이 True이면 건너뛰고 아닐경우 보여줌(읽기전용)
    isSuperUser = fields.Bool(truthy=True) # FIXME

    # 텍스트 포맷가능
    greeting = fields.FormattedString('Hello {name}') #값을 다른데서 받아오는건 필드에 선언하지않아도됨
    # 이안에 있는 필드값이 최우선

# Or, equivalently
class AlbumSchema2(Schema):
    class Meta:
        fields = ("title", "release_date", "email", "name", "password",  "uppername", "isSuperUser", "age")

album = Album("Beggars Banquet", datetime.date(1968, 12, 6), "test@test.com", "test", "1234", False, 0)
schema = AlbumSchema()
data, errors = schema.dump(album)

#assert isinstance(data, OrderedDict)

pprint(data)
print(errors)


user_data = [
    {'email': 'mick@stones.com', 'name': 'Mick'},
    {'email': 'invalid', 'name': 'Invalid', 'age': 50},  # invalid email
    {'email': 'keith@stones.com', 'name': 'Keith', 'age': 15},
    {'email': 'charlie@stones.com'},  # missing "name"
]

result = AlbumSchema(many=True).load(user_data)
# print(result)
# print(type(result))