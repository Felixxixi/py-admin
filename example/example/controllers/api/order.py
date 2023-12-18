import pecan
from pecan import rest, response
from example.common.decorators import api_response
from example.common.error import ServiceError


class OrdersController(rest.RestController):

    @pecan.expose("json")
    @api_response
    def get(self):
        raise ServiceError("1", "测试异常")

        # return {
        #     "100A": "1 bag of corn",
        #     "293F": "2 bags of potatoes",
        #     "207B": "1 bag of carrots"
        # }

    @pecan.expose()
    def post(self):
        # TODO: Create a new order, (optional) return some status data
        response.status = 201
        return "POST SUCCESS!\n"

    @pecan.expose()
    def put(self):
        # TODO: Idempotent PUT (return 200 or 204)
        # response.status = 204
        response.status = 205
        return "PUT SUCCESS!\n"

    @pecan.expose()
    def delete(self):
        # TODO: Idempotent DELETE
        response.status = 200
        return "DELETE SUCCESS\n"
