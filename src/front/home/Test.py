from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label


class TestScreen(Screen):
    place_button = ObjectProperty(None)
    c_and_c_button = ObjectProperty(None)

    def __init__(self, setting_instance, **kwargs):
        super(TestScreen, self).__init__(**kwargs)
        #self.get_json_datas()
        self.setting_instance = setting_instance

    def update_user_info_from_settings(self):
        self.setting_instance.update_user_info()
    def move_place(self):
        self.manager.current = 'place'

    def move_c_c(self):
        self.manager.current = 'c_c'

    def move_order(self):
        self.manager.current = 'order'

    def move_setting(self):
        self.manager.current = 'setting'

    def on_back_press(self):
        session = JsonStore('session.json')
        session.clear() # delete everything in the json
        self.update_user_info_from_settings()
        self.manager.current = 'login'

    def get_json_datas(self):
        session = JsonStore('session.json')





