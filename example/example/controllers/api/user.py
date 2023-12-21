from dataclasses import dataclass, asdict

from pecan import rest
from wsme import types as wtypes
from wsmeext.pecan import wsexpose


class UserCreate(wtypes.Base):
    name = wtypes.wsattr(wtypes.text, mandatory=True)
    email = wtypes.wsattr(wtypes.text, mandatory=True)

    def as_user(self, user_id):
        return User(id=user_id, name=self.name, email=self.email)


@dataclass
class User:
    id: int
    name: str
    email: str


class UserController(rest.RestController):
    @wsexpose(str, int)
    def get(self, user_id):
        """
        query 参数错误
        """
        user = User(id=user_id, name='John Doe', email='john@example.com')
        return asdict(user)

    @wsexpose(str, body=UserCreate)
    def post(self, user_create):
        """
        body 参数错误
        """
        user = user_create.as_user(1234)
        return asdict(user)
