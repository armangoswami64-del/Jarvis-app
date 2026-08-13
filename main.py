from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.camera import Camera
from kivy.uix.label import Label

class JarvisUI(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cam = Camera(play=True, resolution=(640, 480))
        self.add_widget(self.cam)
        self.log = Label(
            text="[SYSTEM ACTIVE]\nVOICE-CONTROL: ONLINE",
            size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            color=(0, 0.8, 1, 1)
        )
        self.add_widget(self.log)

class JARVISApp(App):
    def build(self):
        return JarvisUI()

if __name__ == '__main__':
    JARVISApp().run()
  
