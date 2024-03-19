from kivy.app import App
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import ScreenManager

from src.front.click_and_collect.menu import MenuScreen
from src.front.home.home import Home
from src.front.login.login import LoginScreen
from src.front.reservation_table.reservation import ReservationScreen
from src.front.registration.registration import RegistrationScreen


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(Home(name='home'))
        sm.add_widget(ReservationScreen(name='place'))
        sm.add_widget(MenuScreen(name='c_c'))
        sm.add_widget(RegistrationScreen(name='registration'))
        return sm


def pages():
    MyApp().run()
