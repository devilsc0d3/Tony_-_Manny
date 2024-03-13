from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from src.front.click_and_collect.menu import MenuScreen
from src.front.home.home import TestScreen
from src.front.login.login import LoginScreen
from src.front.reservation_table.reservation import ReservationScreen


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(TestScreen(name='test'))
        sm.add_widget(ReservationScreen(name='place'))
        sm.add_widget(MenuScreen(name='c_c'))
        return sm


def pages():
    MyApp().run()
