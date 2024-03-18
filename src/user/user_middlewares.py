import re

from src.user.user_services import user_get_service


def if_username_exist(first_name, last_name):
    if len(user_get_service(first_name, last_name)) > 0:
        return False  # return false if user already exist
    else:
        return True  # return true if user don't exist


def check_good_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-=_+]).{8,}$'  # regex pattern to check the good format

    if re.match(pattern, password):
        return True  # return true if right format
    else:
        return False  # return false if wrong format
