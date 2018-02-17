import sqlite3

#database for the storage of contacts and tags
class Db:
    def __init__(self):
        self.connection = sqlite3.connect("contacts.db")
        self.createTable()
        self.createTagTable()
        self.createTagContactTable()

    #create database tables (contacts, tags, tagcontact)
    def createTable(self):
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS CONTACTS(C_ID TEXT, FIRST_NAME TEXT, LAST_NAME TEXT, TELEPHONE TEXT, EMAIL TEXT, URL TEXT, NOTES TEXT)")
        self.connection.commit()

    def createTagTable(self):
        self.connection.execute("CREATE TABLE IF NOT EXISTS TAGS(TAG TEXT)")
        self.connection.commit()

    def createTagContactTable(self):
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS TAGCONTACT(ID TEXT, TAG TEXT )")
        self.connection.commit()


    # handles conctacts table
    # save contact in database
    def saveContact(self, id, first_name, last_name, telephone, e_mail, url, notes):
        self.connection.execute("INSERT INTO CONTACTS VALUES(?,?,?,?,?,?,?)", (id, first_name, last_name, telephone, e_mail, url, notes))
        self.connection.commit()

    # get contact from database given a specific id
    def getContactfromId(self,id):
        result = self.connection.execute("SELECT FIRST_NAME, LAST_NAME, TELEPHONE, EMAIL, URL, NOTES FROM CONTACTS WHERE C_ID = '" + id + "' ")
        return result

    # get contact where the text is the firstname/lastname or the initial letters of firstname/lastname
    def getContactFromText(self, text):
        result = self.connection.execute("SELECT C_ID, FIRST_NAME, LAST_NAME, TELEPHONE, EMAIL, URL, NOTES FROM CONTACTS WHERE (FIRST_NAME  LIKE '"+ text +"%' OR LAST_NAME LIKE '"+ text +"%') ORDER BY lower(FIRST_NAME) ASC, LOWER(LAST_NAME) ASC")
        return result

    # get all contact of the database order by name
    def getContacts(self):
        result = self.connection.execute("SELECT * FROM CONTACTS ORDER BY lower(FIRST_NAME) ASC, LOWER(LAST_NAME) ASC")
        return result

    # update a contact with new data
    def updateContact(self,first_name, last_name, telephone, email, url, company, id):
        self.connection.execute("""UPDATE CONTACTS SET FIRST_NAME=?, LAST_NAME=?,TELEPHONE=?, EMAIL=?, URL=?,NOTES=? WHERE C_ID=?""", (first_name,last_name,telephone,email,url,company,id))
        self.connection.commit()

    #delete a contact
    def deleteContact(self, id):
        self.connection.execute("DELETE FROM CONTACTS WHERE C_ID = ?", (id,))
        self.connection.commit()



    # handles tags table
    def insertTag(self, tag):
        self.connection.execute("INSERT INTO TAGS VALUES(?)",(tag,))
        self.connection.commit()

    # get all tags of the database
    def getTags(self):
        result = self.connection.execute("SELECT * FROM TAGS")
        return result



    # handles tagcontact table
    def insertTagContact(self, id , tag):
        self.connection.execute("INSERT INTO TAGCONTACT VALUES(?,?)", (id,tag))
        self.connection.commit()

    # get tags associated to a specific id
    def getTagsFromId(self, id):
        result = self.connection.execute("SELECT TAG FROM TAGCONTACT WHERE ID = '"+ id +"' ")
        return result

    # get contacts belonging to the same specific tag
    def getContactsFromTag(self, tag):
        result = self.connection.execute("SELECT ID FROM CONTACTS INNER JOIN TAGCONTACT ON CONTACTS.C_ID = TAGCONTACT.ID WHERE TAG = '" + tag + "' ORDER BY lower(FIRST_NAME) ASC, LOWER(LAST_NAME) ASC ")
        return result

    # delete all the rows of the table with a specific id
    def deleteContactTagsFromId(self,id):
        self.connection.execute("DELETE FROM TAGCONTACT WHERE ID = ?", (id,))
        self.connection.commit()

    # get all contacts with a specific tag and a firstname/lastname equal to the text or
    # the first letters of firstname/lastname are equal to the text
    def getContactFromTagAndText(self, name, tag):
        result = self.connection.execute("SELECT C_ID, FIRST_NAME, LAST_NAME, TELEPHONE, EMAIL, URL, NOTES FROM CONTACTS INNER JOIN TAGCONTACT ON CONTACTS.C_ID = TAGCONTACT.ID WHERE (FIRST_NAME LIKE '"+ name +"%' OR LAST_NAME LIKE '"+ name +"%') AND TAG = '"+ tag +"' ORDER BY lower(FIRST_NAME) ASC, LOWER(LAST_NAME) ASC")
        return result

