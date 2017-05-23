import wpf

from System.Windows import Window

class AddNewPosition(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'AddNewPosition.xaml')
