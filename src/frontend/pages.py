from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.app import MDApp

from src.frontend.page.click_and_collect.menu import MenuScreen
from src.frontend.page.home.home import HomeScreen
from src.frontend.page.login.login import LoginScreen
from src.frontend.page.order.order import OrderScreen
from src.frontend.page.registration.registration import RegistrationScreen
from src.frontend.page.reservation_table.reservation import ReservationScreen
from src.frontend.page.setting.setting import SettingScreen

Builder.load_file('./frontend/page/home/home.kv')
Builder.load_file('./frontend/page/click_and_collect/menu.kv')
Builder.load_file('./frontend/page/reservation_table/reservation.kv')
Builder.load_file('./frontend/page/order/order.kv')
Builder.load_file('./frontend/page/setting/setting.kv')


class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))

        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SettingScreen(name='setting'))
        sm.add_widget(OrderScreen(name='order'))
        sm.add_widget(ReservationScreen(name='place'))
        sm.add_widget(MenuScreen(name='c_c'))
        sm.add_widget(RegistrationScreen(name='registration'))

        return sm


def pages():
    MyApp().run()
