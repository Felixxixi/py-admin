import pecan

from example.controllers.api import pinyin
from example.controllers.api import user


class ApiController(object):
    pinyins = pinyin.PinyinController()
    users = user.UserController()

    @pecan.expose("json")
    def index(self):
        return {"version": "1.0.0", "info": "test api"}
