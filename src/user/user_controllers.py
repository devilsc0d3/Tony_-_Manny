from src.user.user_middlewares import *
from src.user.user_services import user_add_service


def user_add_controller(first_name, last_name, phone_number, password):
    result = ""
    if not if_username_exist(first_name, last_name):
        result = "Username is already taken"
    elif not check_good_password(password):
        result = "Password require 8 characters minimum, 1 lowercase, 1 uppercase, 1 digit and 1 special character"
    else:
        try:
            user_add_service(first_name, last_name, phone_number, password)
        except Exception as err:
            print(err)
        else:
            result = ""
    return result
