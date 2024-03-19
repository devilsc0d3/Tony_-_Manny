from src.user.user_middlewares import *
from src.user.user_services import *


def user_registration_controller(first_name, last_name, phone_number, raw_phone_number,
                                 password, confirm_password, raw_password):
    result = "FALSE"
    if not if_username_exist(first_name, last_name):
        result = "Username is already taken"
    elif not check_good_password_format(raw_password):
        result = "Password require 8 characters minimum, 1 lowercase, 1 uppercase, 1 digit and 1 special character"
    elif not check_good_phone_number_format(raw_phone_number):
        result = "Phone has to be only digits"
    elif not check_if_passwords_are_same(password, confirm_password):
        result = "Passwords are not same"
    else:
        try:
            user_add_service(first_name, last_name, phone_number, password)
        except Exception as err:
            print("exception user add service: ", err)
        else:
            result = ""
    return result


def user_login_controller(phone_number, raw_password, raw_phone_number):
    result = "FALSE"
    if not check_good_phone_number_format(raw_phone_number):
        result = "Phone has to be only digits"
    else:
        try:
            if if_good_password(phone_number, raw_password):
                result = ""
        except Exception as err:
            print("exception if good password: ", err)
    return result
