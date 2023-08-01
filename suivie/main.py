from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
import helper
#Window.size = (300, 650)

class suivie(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        kv1 = Builder.load_string(helper.toolbar1)
        return kv1

if __name__=="__main__":
    suivie().run()