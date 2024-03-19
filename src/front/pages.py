from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.app import MDApp
from src.front.click_and_collect.menu import MenuScreen
from src.front.home.Test import TestScreen
from src.front.login.login import LoginScreen
from src.front.order.order import OrderScreen
from src.front.reservation_table.reservation import ReservationScreen
from src.front.registration.registration import RegistrationScreen

Builder.load_file('C:\\Users\\faure_jadlbzp\Desktop\sql project\src\\front\home\\test.kv')
Builder.load_file('C:\\Users\\faure_jadlbzp\Desktop\sql project\src\\front\click_and_collect\menu.kv')
Builder.load_file('C:\\Users\\faure_jadlbzp\Desktop\sql project\src\\front\\reservation_table\\reservation.kv')
Builder.load_file('C:\\Users\\faure_jadlbzp\Desktop\sql project\src\\front\\order\\order.kv')

Builder.load_file('./front/home/test.kv')
Builder.load_file('./front/click_and_collect/menu.kv')
Builder.load_file('./front/reservation_table/reservation.kv')

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(TestScreen(name='test'))
        sm.add_widget(OrderScreen(name='order'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(ReservationScreen(name='place'))
        sm.add_widget(MenuScreen(name='c_c'))
        sm.add_widget(RegistrationScreen(name='registration'))

        return sm


def pages():
    MyApp().run()
