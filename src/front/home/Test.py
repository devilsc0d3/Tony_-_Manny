from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button


class TestScreen(Screen):
    place_button = ObjectProperty(None)
    c_and_c_button = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TestScreen, self).__init__(**kwargs)

    def move_place(self):
        self.manager.current = 'place'

    def move_c_c(self):
        self.manager.current = 'c_c'

    def initialize_user(self, user_info):
        if user_info:
            phone_number = user_info.get('phone_number')
            if phone_number:
                phone_label = Label(text=f'Phone Number: {phone_number}', color=(1, 1, 1, 1), font_size='20sp',
                                    size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5})
                self.add_widget(phone_label)
        else:
            print("User information not available.")


