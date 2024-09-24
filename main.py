from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition  # new
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Line, Color
from random import randint

# Встановлюємо розміри вікна для зручності тестування
Window.size = (800, 600)


# Головне вікно
class MainScreen(Screen):
    def go_to_game_selection(self, *args):
        self.manager.current = 'game_selection'

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)
        # BoxLayout: Створює розміщення віджетів у вертикальному напрямку.
        # BoxLayout використовується для організації віджетів у рядок або стовпець.
        #  У цьому випадку, елементи розташовуються вертикально.

        # Назва гри
        self.title = Label(text='Гра', font_size='48sp', size_hint=(1, 0.8))
        layout.add_widget(self.title)

        # Кнопка для переходу до вибору гри
        play_button = Button(text='Грати', size_hint=(1, 0.2))
        play_button.bind(on_press=self.go_to_game_selection)
        layout.add_widget(play_button)
        # bind(on_press=self.go_to_game_selection): Зв'язує подію натискання кнопки з методом go_to_game_selection.
        # Коли кнопка натиснута, буде викликана функція go_to_game_selection, яка змінює активний екран на 'game_selection'.


# Вікно вибору гри
class GameSelectionScreen(Screen):
    def go_to_basketball(self, *args):
        self.manager.current = 'basketball'

    def go_to_football(self, *args):
        self.manager.current = 'football'

    def go_to_hockey(self, *args):
        self.manager.current = 'hockey'

    def go_to_tennis(self, *args):
        self.manager.current = 'tennis'

    def go_to_paint(self, *args):
        self.manager.current = 'paint'

    def __init__(self, **kwargs):
        super(GameSelectionScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        # Кнопка баскетбол
        basketball_button = Button(text='Баскетбол', size_hint=(1, 0.5))
        basketball_button.bind(on_press=self.go_to_basketball)
        layout.add_widget(basketball_button)

        # Кнопка футбол
        football_button = Button(text='Футбол', size_hint=(1, 0.5))
        football_button.bind(on_press=self.go_to_football)
        layout.add_widget(football_button)

        # Кнопка хокей
        hockey_button = Button(text='Хокей', size_hint=(1, 0.5))
        hockey_button.bind(on_press=self.go_to_hockey)
        layout.add_widget(hockey_button)

        # Кнопка теніс
        tennis_button = Button(text='Теніс', size_hint=(1, 0.5))
        tennis_button.bind(on_press=self.go_to_tennis)
        layout.add_widget(tennis_button)

        paint_button = Button(text='Малювалка', size_hint=(1, 0.5))
        paint_button.bind(on_press=self.go_to_paint)
        layout.add_widget(paint_button)


# Вікно баскетболу
class BasketballScreen(Screen):
    score = NumericProperty(0)

    def __init__(self, **kwargs):
        super(BasketballScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)

        # Фон дозволяє зображенню розтягуватися для покриття всього екрану, а keep_ratio=False дозволяє ігнорувати пропорції зображення.
        self.background = Image(source='basketball_background.jpg', allow_stretch=True, keep_ratio=False,
                                size_hint=(1, 1))
        layout.add_widget(self.background)

        # М'яч
        self.ball = Image(source='basketball.png', allow_stretch=True, size_hint=(None, None), size=(100, 100))
        self.ball.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.ball.center = self.center  # Розташування м'яча в центрі екрану
        self.ball.bind(on_touch_down=self.ball_clicked)
        layout.add_widget(self.ball)

        # Лічильник
        self.score_label = Label(text='Score: 0', font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(self.score_label)

        # Кнопка "Назад"
        back_button = Button(text='Назад', size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0})
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

    def ball_clicked(self, instance, touch):
        # Перевіряє, чи натискання сталося на м'ячі.
        if instance.collide_point(*touch.pos):
            self.score += 1
            self.score_label.text = f'Score: {self.score}'
            self.ball_click_animation()

    def ball_click_animation(self):  # new
        # Анімація зміни розміру, прозорості і обертання
        anim = Animation(size=(150, 150), opacity=0.5, duration=0.2) + Animation(size=(100, 100), opacity=1,
                                                                                 duration=0.2)
        anim.start(self.ball)

    def go_back(self, instance):
        self.manager.current = 'game_selection'


# Вікно футболу
class FootballScreen(Screen):
    score = NumericProperty(0)

    def __init__(self, **kwargs):
        super(FootballScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)

        # Фон
        self.background = Image(source='football_background.png', allow_stretch=True, keep_ratio=False,
                                size_hint=(1, 1))
        layout.add_widget(self.background)

        # М'яч
        self.ball = Image(source='football.png', allow_stretch=True, size_hint=(None, None), size=(100, 100))
        self.ball.size_hint = (None, None)
        self.ball.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.ball.center = self.center  # Розташування м'яча в центрі екрану
        self.ball.bind(on_touch_down=self.ball_clicked)
        layout.add_widget(self.ball)

        # Лічильник
        self.score_label = Label(text='Score: 0', font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(self.score_label)

        # Кнопка "Назад"
        back_button = Button(text='Назад', size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0})
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

    def ball_clicked(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.score += 1
            self.score_label.text = f'Score: {self.score}'
            self.ball_click_animation()

    def ball_click_animation(self):
        # паралельна
        anim = Animation(pos=(80, 10))
        anim &= Animation(size=(300, 300), duration=1) + Animation(size=(150, 150), duration=1)
        anim.start(self.ball)

    def go_back(self, instance):
        self.manager.current = 'game_selection'


# Вікно хокею
class HockeyScreen(Screen):
    score = NumericProperty(0)

    def __init__(self, **kwargs):
        super(HockeyScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)

        # Фон дозволяє зображенню розтягуватися для покриття всього екрану, а keep_ratio=False дозволяє ігнорувати пропорції зображення.
        self.background = Image(source='basketball_background.jpg', allow_stretch=True, keep_ratio=False,
                                size_hint=(1, 1))
        layout.add_widget(self.background)

        # М'яч
        self.ball = Image(source='basketball.png', allow_stretch=True, size_hint=(None, None), size=(100, 100))
        self.ball.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.ball.center = self.center  # Розташування м'яча в центрі екрану
        self.ball.bind(on_touch_down=self.ball_clicked)
        layout.add_widget(self.ball)

        # Лічильник
        self.score_label = Label(text='Score: 0', font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(self.score_label)

        # Кнопка "Назад"
        back_button = Button(text='Назад', size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0})
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

    def ball_clicked(self, instance, touch):
        # Перевіряє, чи натискання сталося на м'ячі.
        if instance.collide_point(*touch.pos):
            self.score += 1
            self.score_label.text = f'Score: {self.score}'
            self.ball_click_animation()

    def ball_click_animation(self):
        anim = Animation(size=(150, 150), duration=0.2) + Animation(size=(100, 100), duration=0.2)
        # Запускає анімацію на віджеті м'яча
        anim.start(self.ball)

    def go_back(self, instance):
        self.manager.current = 'game_selection'


# Вікно Tennis
class TennisScreen(Screen):
    score = NumericProperty(0)

    def __init__(self, **kwargs):
        super(TennisScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)

        # Фон дозволяє зображенню розтягуватися для покриття всього екрану, а keep_ratio=False дозволяє ігнорувати пропорції зображення.
        self.background = Image(source='basketball_background.jpg', allow_stretch=True, keep_ratio=False,
                                size_hint=(1, 1))
        layout.add_widget(self.background)

        # М'яч
        self.ball = Image(source='basketball.png', allow_stretch=True, size_hint=(None, None), size=(100, 100))
        self.ball.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.ball.center = self.center  # Розташування м'яча в центрі екрану
        self.ball.bind(on_touch_down=self.ball_clicked)
        layout.add_widget(self.ball)

        # Лічильник
        self.score_label = Label(text='Score: 0', font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(self.score_label)

        # Кнопка "Назад"
        back_button = Button(text='Назад', size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0})
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

    def ball_clicked(self, instance, touch):
        # Перевіряє, чи натискання сталося на м'ячі.
        if instance.collide_point(*touch.pos):
            self.score += 1
            self.score_label.text = f'Score: {self.score}'
            self.ball_click_animation()

    def ball_click_animation(self):
        anim = Animation(size=(150, 150), duration=0.2) + Animation(size=(100, 100), duration=0.2)
        # Запускає анімацію на віджеті м'яча
        anim.start(self.ball)

    def go_back(self, instance):
        self.manager.current = 'game_selection'


class PaintWidget(Widget):
    def on_touch_down_ellipse(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))


class ClickerApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())  # new
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(GameSelectionScreen(name='game_selection'))
        sm.add_widget(BasketballScreen(name='basketball'))
        sm.add_widget(FootballScreen(name='football'))
        sm.add_widget(HockeyScreen(name='hockey'))
        sm.add_widget(TennisScreen(name='tennis'))
        return sm


if __name__ == '__main__':
    ClickerApp().run()