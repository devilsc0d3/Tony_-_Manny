import hashlib
import re

from src.user.user_services import *


def if_username_exist(first_name, last_name):
    if len(user_get_by_username_service(first_name, last_name)) > 0:
        return False  # return false if user already exist
    else:
        return True  # return true if user don't exist


def check_good_password_format(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-=_+]).{8,}$'  # regex pattern to check the good format

    if re.match(pattern, password):
        return True  # return true if right format
    else:
        return False  # return false if wrong format


def if_good_password(phone_number, password):
    user = user_get_by_phone_number_service(phone_number)
    if user is not None:
        stored_password = user[0][4]  # password stocked in the 4th column of users table
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if hashed_password == stored_password:
            return True  # return true if the password match with the right user
    return False  # return false if not


def check_good_phone_number_format(phone_number):
    if re.match("^[0-9]+$", phone_number):
        return True  # return true if the phone number is only digits
    else:
        return False  # return false if not


def check_if_passwords_are_same(password, confirm_password):
    if re.match(password, confirm_password):
        return True  # return true if passwords are same
    else:
        return False  # return false not

def if_phone_number_exist(phone_number):
    if len(user_get_by_phone_number_service(phone_number)) > 0:
        return False  # return false if user already exist
    else:
        return True  # return true if user don't exist