import wpf

from System.Windows import Application, Window

from AddNewPosition import *

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'UiDbManager.xaml')
    
    def onSearchClick(self, sender, e):
        pass
    
    def OnSaveChangesClick(self, sender, e):
        pass
    
    def onDeleteClick(self, sender, e):
        pass

    def onAddPositionClick(self, sender, e):
        addNewPositionWindow = AddNewPosition()
        addNewPositionWindow.ShowDialog()
        
if __name__ == '__main__':
    Application().Run(MyWindow())
