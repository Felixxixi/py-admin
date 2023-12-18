import pecan

from example.controllers.api import order
from example.controllers.api import pinyin


class ApiController(object):
    orders = order.OrdersController()
    testorder = order.OrdersController()
    pinyins = pinyin.PinyinController()

    @pecan.expose("json")
    def index(self):
        return {"version": "1.0.0", "info": "test api"}
