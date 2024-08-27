
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    txt = Label(text="виберіть екран")
    box_button = BoxLayout()
    box_button = BoxLayout(oreintation = "vertical",)



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

