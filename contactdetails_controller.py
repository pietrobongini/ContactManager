from PyQt5 import QtWidgets
from ui import contactdetails
from models import TagContactModel, tagModel, contactModel
import contactlist_controller

# controller for contact details view
class ContactDetailsController(QtWidgets.QMainWindow):
    def __init__(self,contact):
        super(ContactDetailsController, self).__init__()
        self.contact = contact
        self.view = contactdetails.Ui_MainWindow()
        self.view.setupUi(self)
        self.addBehavior()
        self.showDetails()
        self.showTags()

    # adds behavior to the buttons of the view
    def addBehavior(self):
        self.view.submit.clicked.connect(self.saveContact)
        self.view.back_button.clicked.connect(self.goToContactList)
        self.view.delete_button.clicked.connect(self.deleteContact)

    # shows the data for a specific contact
    def showDetails(self):
        self.view.contact_name.setText(self.contact.getFirstName() + " " + self.contact.getLastName())
        self.view.first_name.setText(self.contact.getFirstName())
        self.view.last_name.setText(self.contact.getLastName())
        self.view.telephone.setText(self.contact.getTelephone())
        self.view.email.setText(self.contact.getEmail())
        self.view.url.setText(self.contact.getUrl())
        self.view.notes.setText(self.contact.getNotes())

    # shows all the tags and checks all the tags associated with a specific contact
    # it uses the tagmodel and the tagcontactmodel to retrieve the data from the respective tables of the database
    # cycles on all tags of the database (adding a checkbox for each one) and checks only the tags associated to the contact
    def showTags(self):
        tag = tagModel()
        alltags = tag.getDBTags()
        tag_contact = TagContactModel()
        tag_contact.setId(self.contact.getId())
        contact_tags = tag_contact.getTagFromId()
        currentTags = []
        for t in contact_tags:
            currentTags.append(t[0])
        for tag in alltags:
            tagmodel = tagModel()
            tagmodel.setTag(tag[0])
            radiobutton = QtWidgets.QCheckBox()
            radiobutton.setText(tag[0])
            if tag[0] in currentTags:
                radiobutton.setChecked(True)
            self.view.buttonListLayout.addWidget(radiobutton)

    # delete a specific contact
    # delete data from contact table and data from contacttag table
    # it uses contactmodel and tagcontactmodel to delete contact's data from the respective table pf the database
    def deleteContact(self):
        first_name = self.view.first_name.text()
        last_name = self.view.last_name.text()
        telephone = self.view.telephone.text()
        email = self.view.email.text()
        url = self.view.url.text()
        notes = self.view.notes.toPlainText()

        contactToDelete = contactModel()
        id = self.contact.getId()
        contactToDelete.setfield(id, first_name,last_name,telephone,email,url,notes)
        contactToDelete.deleteContact()

        tag_contact = TagContactModel()
        tag_contact.setId(id)
        tag_contact.deleteContactTagsFromId()

        self.goToContactList()

    # update data of the contact
    # update the data in the row of the contact
    # delete all the rows in tagcontact table associated to this contact
    # then save all tags associated to the contact
    # it uses tagcontactmodel and contactmodel to handle the respective tables of the database
    def saveContact(self):
        first_name = self.view.first_name.text()
        last_name = self.view.last_name.text()
        telephone = self.view.telephone.text()
        email = self.view.email.text()
        url = self.view.url.text()
        notes = self.view.notes.toPlainText()

        if (first_name != None and first_name != "" and last_name != None and last_name != ""):
            id = self.contact.getId()
            newContact = contactModel()
            newContact.setfield(id, first_name, last_name, telephone, email, url, notes)
            newContact.updateContact()

            tag_contact_model = TagContactModel()
            tag_contact_model.setId(id)
            tag_contact_model.deleteContactTagsFromId()

            items = (self.view.buttonListLayout.itemAt(i).widget() for i in range(self.view.buttonListLayout.count()))
            for i in items:
                if i.isChecked() == True:
                    tag_contact_model.setId(id)
                    tag_contact_model.setTag(i.text())
                    tag_contact_model.saveContactTag()

        self.goToContactList()

    # change view and go to the contactlistview
    def goToContactList(self):
        self.view.homWindow = QtWidgets.QMainWindow()
        self.view.ui = contactlist_controller.ContactListController()
        self.view.mw.close()
        self.view.ui.show()
