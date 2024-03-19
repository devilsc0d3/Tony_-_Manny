from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.app import MDApp
from src.front.click_and_collect.menu import MenuScreen
from src.front.home.Test import TestScreen
from src.front.login.login import LoginScreen
from src.front.order.order import OrderScreen
from src.front.reservation_table.reservation import ReservationScreen
from src.front.registration.registration import RegistrationScreen
from src.front.setting.setting import SettingScreen

Builder.load_file('./front/home/test.kv')
Builder.load_file('./front/click_and_collect/menu.kv')
Builder.load_file('./front/reservation_table/reservation.kv')
Builder.load_file('./front/order/order.kv')
Builder.load_file('./front/setting/setting.kv')


class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SettingScreen(name='setting'))
        sm.add_widget(TestScreen(name='test'))
        sm.add_widget(OrderScreen(name='order'))
        sm.add_widget(ReservationScreen(name='place'))
        sm.add_widget(MenuScreen(name='c_c'))
        sm.add_widget(RegistrationScreen(name='registration'))

        return sm


def pages():
    MyApp().run()
