from src.user.user_middlewares import *
from src.user.user_services import *


def user_registration_controller(first_name, last_name, phone_number, password):
    result = ""
    if not if_username_exist(first_name, last_name):
        result = "Username is already taken"
    elif not check_good_password_format(password):
        result = "Password require 8 characters minimum, 1 lowercase, 1 uppercase, 1 digit and 1 special character"
    elif not check_good_phone_number_format(phone_number):
        result = "Phone has to be only digits"
    else:
        try:
            user_add_service(first_name, last_name, phone_number, password)
        except Exception as err:
            print(err)
        else:
            result = ""
    return result


def user_login_controller(phone_number, password):
    result = ""
    if not check_good_phone_number_format(phone_number):
        result = "Phone has to be only digits"
    else:
        try:
            if_good_password(phone_number, password)
        except Exception as err:
            print(err)
        else:
            result = ""
    return result
