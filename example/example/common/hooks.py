import json
import logging

import pecan
from webob import Response

from example.common.base import ApiResponse


class GlobalHandlerHooks(pecan.hooks.PecanHook):
    priority = 100

    def on_route(self, state):
        return

    def before(self, state):
        return

    def after(self, state):
        response = state.response
        status_code = response.status_code
        if status_code // 100 == 2:
            api_response = ApiResponse.success(response.json_body)
        else:
            json_body = response.json_body
            logging.error(f'{json_body}')
            if isinstance(json_body, dict) and 'faultstring' in json_body:
                api_response = ApiResponse.error(code=status_code, message=json_body['faultstring'])
            else:
                api_response = ApiResponse.error(code=status_code, message=response.explanation)

        state.response = Response(body=json.dumps(api_response.as_dict()), status=200,
                                  content_type='application/json; charset=utf-8')
        return

    def on_error(self, state, e):
        return
