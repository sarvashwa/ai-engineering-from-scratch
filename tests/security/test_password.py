from src.security.password import hash_password, verify_password


def test_password():
    password = "hello123"

    hashed_password = hash_password(password)

    assert hashed_password != password
    assert verify_password(password, hashed_password) is True

    wrong_password = "wrong"

    assert verify_password(wrong_password, hashed_password) is False