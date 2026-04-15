
import requests
from jsonschema import validate

from configurations import SERVER_URL
from scr.baseclasses.get_user_response import GetUserResponse
from scr.enums.global_enums import GlobalErrorMessages
from scr.schemas.user_schemas import GET_USER_SCHEMA

def test_get_users():
    response = requests.get(f'{SERVER_URL}')
    get_user_response = GetUserResponse(response)

    get_user_response.assert_status_code(200).assert_json(GET_USER_SCHEMA)

# def test_equal():
#     assert 1 == 1, 'Numbers are not equal'
#
# def test_not_equal():
#     assert 1 != 1, 'Numbers are equal'