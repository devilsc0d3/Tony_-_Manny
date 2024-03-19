from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from src.user.user_controllers import *


class SettingScreen(Screen):
    data = {}

    def __init__(self, **kwargs):
        super(SettingScreen, self).__init__(**kwargs)
        self.get_json_datas()
        self.refresh()

    def on_back_press(self):
        self.manager.current = 'home'

    def refresh(self):
        # self.clear_widgets()
        self.clear_user_info_widgets()
        self.get_json_datas()

    def clear_user_info_widgets(self):
        # Clear all existing user info widgets
        for widget in self.children[:]:
            if isinstance(widget, Label):
                self.remove_widget(widget)

    def phone_number_update(self, user_id):
        hashed_phone_number = hashlib.sha256(self.phone_number_input.text.encode('utf-8')).hexdigest()
        raw_phone_number = self.phone_number_input.text
        try:
            result = (user_update_phone_number_controller
                      (hashed_phone_number, raw_phone_number, user_id))
        except Exception as err:
            print("exception user update phone number controller: ", err)
        else:
            if result != "":
                print("result: ", result)
            else:
                # load datas from the session
                session = JsonStore('session.json')
                data = session.get('user')

                # update only phone number in the json
                data['phone_number'] = self.phone_number_input.text

                # save
                session.put('user', **data)

                # delete previous widget
                self.remove_widget(self.phone_number_label)

                # create and add the new one
                self.phone_number_label = Label(text=f'Phone Number: {self.phone_number_input.text}',
                                                color=(0, 0, 0, 1),
                                                font_size='20sp',
                                                size_hint=(None, None), size=(300, 50),
                                                pos_hint={'center_x': 0.5, 'center_y': 0.3})
                self.add_widget(self.phone_number_label)

                print("User phone number updated successfully")

    def password_update(self, user_id):
        hashed_password = hashlib.sha256(self.password_input.text.encode('utf-8')).hexdigest()
        raw_password = self.password_input.text
        try:
            result = (user_update_password_controller
                      (hashed_password, raw_password, user_id))
        except Exception as err:
            print("exception user update password controller: ", err)
        else:
            if result != "":
                print("result: ", result)
            else:
                print("User password updated successfully")

    def get_json_datas(self):
        session = JsonStore('session.json')
        if session.exists('user'):
            # Si des données utilisateur existent, les récupérer
            data = session.get('user')
        else:
            data = {
                'id': "",
                'first_name': "",
                'last_name': "",
                'phone_number': "",
                # ajouter d'autres champs au besoin
            }
        first_name_label = Label(text=f'First Name: {data["first_name"]}', color=(0, 0, 0, 1), font_size='20sp',
                                 size_hint=(None, None), size=(300, 50),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.1})
        self.add_widget(first_name_label)

        # last name
        last_name = data['last_name']
        last_name_label = Label(text=f'Last Name: {last_name}', color=(0, 0, 0, 1), font_size='20sp',
                                size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        self.add_widget(last_name_label)

        # phone number
        phone_number = data['phone_number']
        self.phone_number_label = Label(text=f'Phone Number: {phone_number}', color=(0, 0, 0, 1), font_size='20sp',
                                        size_hint=(None, None), size=(300, 50),
                                        pos_hint={'center_x': 0.2, 'center_y': 0.5})
        self.add_widget(self.phone_number_label)
        self.phone_number_input = TextInput(hint_text='New Phone Number', multiline=False,
                                            size_hint=(None, None), size=(300, 40),
                                            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(self.phone_number_input)
        phone_number_button = Button(text='Update', size_hint=(None, None), size=(100, 40),
                                     pos_hint={'center_x': 0.8, 'center_y': 0.5})
        phone_number_button.bind(on_press=lambda instance: self.phone_number_update(data['id']))
        self.add_widget(phone_number_button)

        # password
        password_label = Label(text='New Password : ' + "x" * len(data['phone_number']),
                               color=(0, 0, 0, 1),
                               font_size='20sp',
                               size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.2, 'center_y': 0.6})
        self.add_widget(password_label)
        self.password_input = TextInput(hint_text='New Password', multiline=False, password=True,
                                        size_hint=(None, None), size=(300, 40),
                                        pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.add_widget(self.password_input)
        password_button = Button(text='Update', size_hint=(None, None), size=(100, 40),
                                 pos_hint={'center_x': 0.8, 'center_y': 0.6})
        password_button.bind(on_press=lambda instance: self.password_update(data['id']))
        self.add_widget(password_button)
