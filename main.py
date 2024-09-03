
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (800, 600)

class MyApp(App):
    def go_to_game_selection(self, *args):
        self.manager.current = "game_selection"
    def __init__(self,**kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")
        self.add_widget(layout)

        self.title = Label(text = 'play',font_size='48sp', size_hint(1, 0.8))
        layout.add_widget(self.title)

        play_button = Button(text='play',size_hint=(1, 0.2))

        play_button.bind(on_press=self.go_to)

class ClickerApp(App):
   def build(self):
    sm = ScreenManager()
    sm.add_widget(MainScreen(name='main'))
    return sm


class ScrButton(Button):
    def __init__(self, screen ,direction = 'right', goal = 'main',**kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manger.transition.direction = self.direction
        self.screen.manger.current = self.goal


app = MyApp()
app.run()

