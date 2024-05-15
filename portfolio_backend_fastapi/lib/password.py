import hashlib


def hash_password(plain_password) -> str:
    """
    Hashes a password for storing in the database.
    :param plain_password: The password to hash.
    :return: The hashed password.
    """
    return hashlib.sha256(plain_password.encode()).hexdigest()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a password against a hashed password.
    :param plain_password: The password to verify.
    :param hashed_password: The hashed password to verify against.
    :return: True if the passwords match, False otherwise.
    """
    return hash_password(plain_password) == hashed_password
