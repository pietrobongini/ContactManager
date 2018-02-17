from PyQt5 import QtWidgets
from ui import tagadder
from models import tagModel
import contactlist_controller

# controller for the tagadder view
class TagAdderController(QtWidgets.QMainWindow):
    def __init__(self):
        super(TagAdderController, self).__init__()
        self.view = tagadder.Ui_MainWindow()
        self.view.setupUi(self)
        self.addBehavior()

    # add behavior to the buttons
    def addBehavior(self):
        self.view.submit.clicked.connect(self.saveTag)
        self.view.back.clicked.connect(self.goToContactListView)

    # save a tag in a specific table of the database
    # it uses tag model to store the tag in the specific table of the database
    def saveTag(self):
        tag = self.view.tagInput.text()
        if (tag != "" and tag != None):
            tag_model = tagModel()
            tag_model.setTag(tag)
            tag_model.saveTag()
            self.goToContactListView()

    # go to contact list view
    def goToContactListView(self):
        self.view.homWindow = QtWidgets.QMainWindow()
        self.view.ui = contactlist_controller.ContactListController()
        self.view.mw.close()
        self.view.ui.show()