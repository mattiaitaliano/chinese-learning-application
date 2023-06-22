from kivy.uix.screenmanager import ScreenManager

class NavigationScreenManager(ScreenManager):
    screen_stack = []

    def push(self, screen_name):
        self.screen_stack.append(self.current)
        self.current = screen_name

    def pop(self):
        if len(self.screen_stack) > 0:
            screen_name = self.screen_stack[-1]
            del self.screen_stack[-1]
            self.current = screen_name

        