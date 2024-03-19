from kivy.uix.screenmanager import Screen


class SettingScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingScreen, self).__init__(**kwargs)

    def on_pre_enter(self):
        print("Setting screen")

    def on_back_press(self):
        self.manager.current = 'test'

