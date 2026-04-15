from jsonschema import validate

from scr.enums.global_enums import GlobalErrorMessages

class GetUserResponse:
    def __init__(self, response):
        self.response = response
        self.body = response.json()
        self.status_code = response.status_code

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.status_code in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def assert_json(self, schema):
        if isinstance(self.body, list):
            for item in self.body:
                validate(item, schema)
        else:
            validate(self.body, schema)
        return self
