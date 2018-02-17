from PyQt5 import QtWidgets, QtCore
from ui import contactadder
from models import contactModel, tagModel, TagContactModel
import random
import contactlist_controller

# Controller for contactadder view
class ContactAdderController(QtWidgets.QMainWindow):
    def __init__(self):
        super(ContactAdderController, self).__init__()
        self.view = contactadder.Ui_textListView()
        self.view.setupUi(self)
        self.showTags()
        self.addBehavior()

    # tags are added dinamically to the view as checkboxes (new tags can be added to the system in tagadder view)
    # tagmodel is used to retrieve all the tags from the specific table of the database
    def showTags(self):
        tag_model = tagModel()
        tags = tag_model.getDBTags()
        for tag in tags:
            checkbox = QtWidgets.QCheckBox()
            checkbox.setText(tag[0])
            self.view.buttonListLayout.addWidget(checkbox)

    #gives a behavior to the buttons. The function enableSaving is called every 0.5 secs
    def addBehavior(self):
        self.view.back_button.clicked.connect(self.goToContactList)
        self.view.submit.clicked.connect(self.saveContact)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.enableSaving)
        self.timer.start(500)

    # enable the saving button only when first name and last name fields aren't empty
    def enableSaving(self):
        if self.view.first_name.text() != "" and self.view.last_name.text() != "":
            self.view.submit.setEnabled(True)
        else:
            self.view.submit.setEnabled(False)

    # save the contact. Each contact is associated to a contactmodel which is caracterized
    # by id, firstname, lastname, phone number, e-mail, url and some notes about him
    # these data are then stored in an apposite table of the database
    # moreover, some tags can be associated to the contact
    # TagContactModel is a model characterized by a contact id and a tagname
    # the contact id and the tag are then saved in an apposite table of the database
    # the id field is generated randomically
    def saveContact(self):
        first_name = self.view.first_name.text()
        last_name = self.view.last_name.text()
        telephone = self.view.telephone.text()
        email = self.view.email.text()
        url = self.view.url.text()
        notes = self.view.notes.toPlainText()

        if (first_name != None and first_name != "" and last_name != None and last_name != ""):
            newContact = contactModel()
            id = ''.join(random.choice("abcdefghilmnopqrtstuvz0123456789") for _ in range(10))
            newContact.setfield(id, first_name, last_name, telephone, email, url, notes)
            newContact.saveContact()
            items = (self.view.buttonListLayout.itemAt(i).widget() for i in range(self.view.buttonListLayout.count()))
            for i in items:
                if i.isChecked() == True:
                    tag_contact_model = TagContactModel()
                    tag_contact_model.setId(id)
                    tag_contact_model.setTag(i.text())
                    tag_contact_model.saveContactTag()
        self.goToContactList()

    # change view and go to the contactlistview
    def goToContactList(self):
        self.view.homWindow = QtWidgets.QMainWindow()
        self.view.ui = contactlist_controller.ContactListController()
        self.view.tlv.close()
        self.view.ui.show()


