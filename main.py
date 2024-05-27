from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivymd.uix.screenmanager import MDScreenManager

class PrimeiraTela(MDScreen):
    pass

class HomeScreen(MDScreen, App):
    pass

class Cookies(MDScreen):
    pass

class Brownie(MDScreen):
    pass

class Macarrons(MDScreen):
    pass

class Bolo(MDScreen):
    pass

class App(MDApp):
    def build(self):
        Window.size = (dp(300), dp(600))
        Builder.load_file(("main.kv"))
        sm = MDScreenManager()
        sm.add_widget(PrimeiraTela())
        sm.add_widget(HomeScreen())
        sm.add_widget(Bolo())
        sm.add_widget(Cookies())
        sm.add_widget(Macarrons())
        sm.add_widget(Brownie())
        return sm
        
App().run()