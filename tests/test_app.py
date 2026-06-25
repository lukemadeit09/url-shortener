from app import generate_code


def test_code_length():
    assert len(generate_code()) == 6


def test_code_is_alphanumeric():
    assert generate_code().isalnum()


def test_codes_are_unique():
    codes = {generate_code() for _ in range(100)}
    assert len(codes) > 90  # extremely unlikely to collide much