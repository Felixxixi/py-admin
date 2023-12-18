import json
import logging

import pecan

from example.common.error import ServiceError


class ApiResponse:
    def __init__(self, code, message, data=None):
        self.code = code
        self.message = message
        self.data = data


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        elif isinstance(obj, set):
            return list(obj)
        else:
            return super().default(obj)


def api_response(view_func):
    def wrapper(*args, **kwargs):
        try:
            result = view_func(*args, **kwargs)
            if isinstance(result, ApiResponse):
                response = result
            else:
                response = ApiResponse(code=200, message="Success", data=result)
        except Exception as e:
            logging.error(f"Exception caught: {e}", exc_info=True)

            if isinstance(e, ServiceError):
                response = ApiResponse(code=e.code, message=e.message, data=None)
            else:
                response = ApiResponse(code=500, message="Internal Server Error", data=None)

        response_json = json.dumps(response, cls=CustomEncoder)
        return pecan.Response(response_json, content_type='application/json; charset=utf-8')

    return wrapper
