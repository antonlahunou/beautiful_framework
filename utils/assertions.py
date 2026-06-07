def assert_validation_error(response, expected_status: int, expected_field: str = None, expected_msg: str = None):
    assert response.status_code == expected_status
    error_data = response.json()

    if expected_field or expected_msg:
        for error in error_data.get("detail", []):
            if expected_field and expected_field in str(error.get("loc", [])):
                if expected_msg:
                    assert expected_msg in error.get("msg", "")
                return
        raise AssertionError(f"Expected error for field '{expected_field}' not found")