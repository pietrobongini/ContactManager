from database import Db

# model for the contact
# it handles the table of the database relative to the contact
class contactModel():
    def __init__(self):
        self.id = ""
        self.first_name = ""
        self.last_name = ""
        self.telephone = ""
        self.email = ""
        self.url = ""
        self.notes = ""

    # setter method for all data of the contact
    def setfield(self,id, fname, lname, tel, email, url, notes):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.telephone = tel
        self.email = email
        self.url = url
        self.notes = notes

    # setter for firstname
    def setFirstName(self, first_name):
        self.first_name = first_name

    # setter for lastname
    def setLastName(self,last_name):
        self.last_name = last_name

    # setter for the id
    def setId(self, id):
        self.id = id

    # getter methods
    def getId(self):
        return self.id

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getTelephone(self):
        return self.telephone

    def getEmail(self):
        return self.email

    def getUrl(self):
        return self.url

    def getNotes(self):
        return self.notes

    # store the data of the contact in the database
    def saveContact(self):
        id = self.id
        first_name = self.first_name
        last_name = self.last_name
        telephone = self.telephone
        email = self.email
        url = self.url
        notes = self.notes
        db = Db()
        if (first_name != None and first_name != "" and last_name != None and last_name != ""):
            db.saveContact(id,first_name,last_name,telephone,email, url,notes)

    # get all the contacts of the database
    def showContacts(self):
        db = Db()
        contacts = db.getContacts()
        return contacts

    # update a contact
    def updateContact(self):
       db = Db()
       db.updateContact(self.first_name,self.last_name,self.telephone,self.email,self.url,self.notes,self.id)

    # method to get from database all contacts with a firstname/lastname equal to text or
    # the first letters of the firstname/lastname are equals to text
    def getContactFromText(self,text):
        db = Db()
        contacts = db.getContactFromText(text)
        return contacts

    # method that return the data of contact with a specific id
    def getContactFromId(self):
        db = Db()
        contact = db.getContactfromId(self.id)
        return contact

    # delete a specific contact by id
    def deleteContact(self):
        db = Db()
        db.deleteContact(self.id)

# model for the tag
# it handles the table of the database relative to the tags
class tagModel():
    def __init__(self):
        self.tag = None

    # getter method for tag
    def getTag(self):
        return self.tag

    # setter method for tag
    def setTag(self, tag):
        self.tag = tag

    # save tag in database
    def saveTag(self):
        db = Db()
        tag_name = self.tag
        if ( tag_name !="" and tag_name != None):
            db.insertTag(tag_name)

    # retrieve from database all tags
    def getDBTags(self):
        db = Db()
        tags = db.getTags()
        return tags

# model for the tag and the contact
# it handles the table of the database relative to the contact and the tag
class TagContactModel():
    def __init__(self):
        self.tag = None
        self.id = None

    # getter method for id
    def getId(self):
        return self.id

    # setter method for id
    def setId(self,id):
        self.id = id

    # getter method for tag
    def getTag(self):
        return self.tag

    # setter method for tag
    def setTag(self, tag):
        self.tag = tag

    # return the ids of the contacts belonging to a specific tag
    def searchContactsFromTag(self):
        db = Db()
        ids = db.getContactsFromTag(self.tag)
        return ids

    # return all the tags associated to a specific contact id
    def getTagFromId(self):
        db = Db()
        tags = db.getTagsFromId(self.id)
        return tags

    # store in the database a specific couple id-tag
    def saveContactTag(self):
        db = Db()
        tag_name = self.tag
        id= self.id
        if ( tag_name !="" and tag_name != None and id != "" and id != None):
            db.insertTagContact(id,tag_name)

    # delete all tags associated to a specific id
    def deleteContactTagsFromId(self):
        db = Db()
        id = self.id
        db.deleteContactTagsFromId(id)

    # get contacts with from tag and having the firstname/last name equal to the text or
    # the first letters of firstname/lastname are equal to the text
    def getContactFromTagAndText(self,text):
        db = Db()
        result = db.getContactFromTagAndText(text,self.tag)
        return result
