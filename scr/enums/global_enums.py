from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected status code"
    WRONG_USER_LIST_LENGTH = "Invalid user list length"