from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.graphics import Ellipse, Line, Color
from random import randint

class PaintWidget(Widget):
    def on_touch_down_ellipse(self, touch):
        color = (randint(), 1, 1)
        with self.canvas:
            Color(*color, mode = 'hsv')
            d = 30
            Ellipse(pos = (touch.x - d/2, touch.y - d/2), size=(d,d))
            touch.ud['line'] = Line (points = (touch.x, touch.y))
    def on_touch_move_ellipse(selfself, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        paint = Widget()
        self.painter = PaintWidget()
        clear_button = Button(text = 'Clear')
        clear_button.bind(on_relese = self.clear_canvas)
        paint.add_widget(self.painter)
        paint.add_widget(clear_button)
        return paint
    def clear_canvas(self, *args):
        self.paint. canvas.clear()

if __name__=='__main__':
    MyPaintApp().run()