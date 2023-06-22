from kivy.app import App
from kivy.core.window import Window

class LearnMandarin(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Learn Mandarin Chinese!"
        Window.maximize()
        Window.minimum_width = 800
        Window.minimum_height = 600
        
    def build(self):
        self.icon = "img/logo.jpg"

if __name__ == "__main__":
    LearnMandarin().run()