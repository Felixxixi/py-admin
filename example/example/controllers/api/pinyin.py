import pecan
from pecan import rest

from example.common.decorators import api_response
from example.model.database import Session
from example.model.models import Pinyin


class PinyinController(rest.RestController):

    @pecan.expose()
    @api_response
    def get(self):
        session = Session()
        pinyins = session.query(Pinyin).all()
        pinyin_list = [{
            'id': pinyin.id,
            'pinyin': pinyin.pinyin
        } for pinyin in pinyins]
        return pinyin_list
