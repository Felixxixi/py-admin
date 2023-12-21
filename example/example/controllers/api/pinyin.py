from pecan import rest
from wsmeext.pecan import wsexpose

from example.model.database import Session
from example.model.models import Pinyin


class PinyinController(rest.RestController):

    @wsexpose(str)
    def get(self):
        session = Session()
        pinyins = session.query(Pinyin).all()
        pinyin_list = [{
            'id': pinyin.id,
            'pinyin': pinyin.pinyin
        } for pinyin in pinyins]
        return pinyin_list
