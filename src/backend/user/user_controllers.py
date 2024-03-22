from src.backend.user.user_middlewares import *
from src.backend.user.user_services import *


def user_registration_controller(first_name, last_name, phone_number, raw_phone_number,
                                 password, confirm_password, raw_password):
    result = "FALSE"
    if not if_username_exist(first_name, last_name):
        result = "Username is already taken"
    elif not if_phone_number_exist(phone_number):
        result = "Phone number is already taken"
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


def user_get_by_phone_number_controller(phone_number, raw_phone_number):
    result = ["FALSE"]
    if not check_good_phone_number_format(raw_phone_number):
        result = ["Phone has to be only digits"]
    else:
        try:
            result = user_get_by_phone_number_service(phone_number)
        except Exception as err:
            print("exception user add service: ", err)
    return result


def user_update_phone_number_controller(new_phone_number, raw_phone_number, user_id):
    result = "FALSE"
    if not check_good_phone_number_format(raw_phone_number):
        result = "Phone has to be only digits"
    elif not if_phone_number_exist(new_phone_number):
        result = "Phone number is already taken"
    else:
        try:
            user_update_phone_number_service(new_phone_number, user_id)
        except Exception as err:
            print("exception update phone number service", err)
        else:
            result = ""
    return result


def user_update_password_controller(new_password, raw_password, user_id):
    result = "FALSE"
    if not check_good_password_format(raw_password):
        result = "Password require 8 characters minimum, 1 lowercase, 1 uppercase, 1 digit and 1 special character"
    else:
        try:
            user_update_password_service(new_password, user_id)
        except Exception as err:
            print("exception update phone number service", err)
        else:
            result = ""
    return result
