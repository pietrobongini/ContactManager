from PyQt5 import QtWidgets
import contactdetails_controller

# button with model used in contactlist
# this is an Adapter used to adapt the contact model to the button class
# this button with model is used in contactlist
# this Adapter is useful to custom all the buttons of the list with a specific contact
# moreover, clicking on each of these buttons the view is changed to a detailed view of the specific contact
class ButtonListModel(QtWidgets.QPushButton):
    def __init__(self, contactmod,mainWindow):
        super(ButtonListModel,self).__init__()
        self.mw = mainWindow
        self.contact = contactmod
        self.defineButton()

    # add some properties and behaviour to the button
    def defineButton(self):
        self.setText(self.contact.getFirstName()+ " "+ self.contact.getLastName())
        self.setFixedHeight(50)
        self.clicked.connect(self.changeView)

    # go to contact details view
    def changeView(self):
        self.homWindow = QtWidgets.QMainWindow()
        self.ui = contactdetails_controller.ContactDetailsController(self.contact)
        self.mw.close()
        self.ui.show()
