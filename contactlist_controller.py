from PyQt5 import QtWidgets
from ui import contactlist
from models import contactModel,tagModel, TagContactModel
import widgetwithmodel
import tagadder_controller, contactadder_controller

# controller for the contactlist view
class ContactListController(QtWidgets.QMainWindow):
    def __init__(self):
        super(ContactListController, self).__init__()
        self.view = contactlist.Ui_MainWindow()
        self.view.setupUi(self)
        self.addBehavior()
        self.showContacts()
        self.showTags()

    # add behavior to the buttons.
    def addBehavior(self):
        self.view.search_button.clicked.connect(self.searchContact)
        self.view.add_button.clicked.connect(self.goToContactAdderView)
        self.view.tag_button.clicked.connect(self.goToTagAdderView)

    # show all the contacts of the database represented by a customized button (widgetwithmodel)
    # through the contact model we retrieve from the table of the database all the contacts stored
    # then we customize the button with them
    def showContacts(self):
        contacts = contactModel().showContacts()
        if contacts != None:
            for contact in contacts:
                contactobject = contactModel()
                contactobject.setfield(contact[0], contact[1], contact[2], contact[3], contact[4], contact[5],contact[6])
                button = widgetwithmodel.ButtonListModel(contactobject, self.view.mw)
                self.view.buttonListLayout.addWidget(button)

    # show all the saved tags in an apposite box
    # we use the tagmodel to retrieve from the table of the database all the tags stored
    def showTags(self):
        tagmodel = tagModel()
        tags = tagmodel.getDBTags()
        noneItem = None
        self.view.tagBox.addItem(noneItem)
        for tag in tags:
            self.view.tagBox.addItem(tag[0])

    # search contacts inserting text in textedit or by tags or the two things together
    # contactmodel and tagcontactmodel are used to retrieve data from the respective tables of the database
    # the possibilities are:
    # no tags, no text --> find all contacts
    # no tags, text --> find all contacts having this text name/surname or having this text as initial part of name/surname
    # tag, no text --> find all contacts belonging to this tag
    # tag, text --> find all contacts belonging to this tag and having this
    # text as name/surname or having this text as initial part of name/surname
    def searchContact(self):
        search_tag = self.view.tagBox.currentText()
        search_name = self.view.search_text.text()
        contact_model = contactModel()
        for i in reversed(range(self.view.buttonListLayout.count())):
            self.view.buttonListLayout.itemAt(i).widget().setParent(None)

        if search_tag == "" and search_name == "":
            self.showContacts()

        if search_tag == "" and search_name != "":
            contacts_get_by_name = contact_model.getContactFromText(search_name)

            for contact in contacts_get_by_name:
                if (contact[0] != None or contact[0] != ""):
                    contact_object = contactModel()
                    contact_object.setfield(contact[0], contact[1], contact[2], contact[3], contact[4], contact[5],
                                           contact[6])
                    button = widgetwithmodel.ButtonListModel(contact_object, self.view.mw)
                    self.view.buttonListLayout.addWidget(button)

        if search_tag != "" and search_name == "":
            tagcontactmodel = TagContactModel()
            tagcontactmodel.setTag(search_tag)
            ids = tagcontactmodel.searchContactsFromTag()

            for id in ids:
                if (id[0] != None or id[0] != ""):
                    contact_model.setId(id[0])
                    contacts = contact_model.getContactFromId()
                    for contact in contacts:
                        contact_object = contactModel()
                        contact_object.setfield(id[0], contact[0], contact[1], contact[2], contact[3], contact[4],
                                               contact[5])
                        button = widgetwithmodel.ButtonListModel(contact_object, self.view.mw)
                        self.view.buttonListLayout.addWidget(button)

        if search_tag != "" and search_name != "":
            tagcontactmodel = TagContactModel()
            tagcontactmodel.setTag(search_tag)

            contacts = tagcontactmodel.getContactFromTagAndText(search_name)
            for contact in contacts:
                contact_object = contactModel()
                contact_object.setfield(contact[0], contact[1], contact[2], contact[3], contact[4], contact[5],
                                       contact[6])
                button = widgetwithmodel.ButtonListModel(contact_object, self.view.mw)
                self.view.buttonListLayout.addWidget(button)

    # go to contactadder view
    def goToContactAdderView(self):
        self.view.homWindow = QtWidgets.QMainWindow()
        self.view.ui = contactadder_controller.ContactAdderController()
        self.view.mw.close()
        self.view.ui.show()

    # go to tagadder view
    def goToTagAdderView(self):
        self.view.homWindow = QtWidgets.QMainWindow()
        self.view.ui = tagadder_controller.TagAdderController()
        self.view.mw.close()
        self.view.ui.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listcontrol = ContactListController()
    listcontrol.show()
    sys.exit(app.exec_())