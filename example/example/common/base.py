class ServiceError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    pass


class ApiResponse:
    def __init__(self, code, message, data=None):
        self.code = code
        self.message = message
        self.data = data

    @staticmethod
    def success(data=None):
        return ApiResponse('200', 'Success', data)

    @staticmethod
    def error(code=500, message='failed'):
        return ApiResponse(code, message, None)

    def as_dict(self):
        return {
            'code': self.code,
            'message': self.message,
            'data': self.data
        }
