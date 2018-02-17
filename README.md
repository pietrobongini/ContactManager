# ContactManager

This project is an address book manager application made with Python. The interface is accomplished entirely with PyQt5.

## implementation

The application consists of 4 different views:
- contactadder which allows the user to add a contact (Fig. 1).
- contactlist which is the main view and displays all the contacts allowing the user to make different search for a specific contact (Fig. 2).
- contactdetails which allow the user to see/edit the data saved for a specific contact (Fig. 3).
- contactadder which allow the user to create a tag that will be associated to a contact (Fig. 4).

Fig. 1            |  Fig. 2
:-------------------------:|:-------------------------:
![](https://github.com/pietrobongini/ContactManager/blob/master/ui_img/contactadder.png "Fig. 1")  |  ![](https://github.com/pietrobongini/ContactManager/blob/master/ui_img/contactlist.png "Fig. 2")

Fig. 3            |  Fig. 4
:-------------------------:|:-------------------------:
![](https://github.com/pietrobongini/ContactManager/blob/master/ui_img/contactdetails.png "Fig. 3")  |  ![](https://github.com/pietrobongini/ContactManager/blob/master/ui_img/tagadder.png "Fig. 4")

Model View Controller (MVC) pattern is implemented. There are as seen before 4 view: contactadder.py, contactlist.py, contactdetails.py, tagadder.py. We can find them in ui folder. These views have been built with Qt Designer the .ui files of each view is located in ui_qt-designer. 
For each view a controller has been created. The controller are: 
- contactadder_controller.py for the ui/contactadder.py view.
- contactlist_controller.py for the ui/contactlist.py view.
- contactdetails_controller.py for the ui/contactdetails.py view.
- tagadder_controller.py for the ui/tagadder.py view.

It's useful to separate the view from the controller with PyQt in two different python files. In this way, editing the design of the view doesn't coinvolve the editing of the controller.

To store the data of the contact we used a sqlite database. Three different tables have been created: one to store the contact data (id, firstname, lastname, telephone, email, url, notes), one to store the tags (tagname) and another to associate a tag to a contact (contact_id, tag) 

| ID | firstname | lastname | telephone | email | url | notes|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  |  |  |  |  |

| tagname |
| :---: |
|  |

| ID | tagname|
| :---: | :---: | 
|  |  | 

Three models have been created; each one handles a different table of the database. 

---
## Requirments

Python 3.6.2 has been used to run this project.
The only package used in this work is PyQt5. You can install it:
- with pip `pip3 install PyQt5`
- with anaconda `conda install -c dsdale24 pyqt5`

---
## Run the project

To run the application:
- from terminal go to the directory in wich you have downloaded the project
- go inside the ContactManager-master folder --> `cd ContactManager-master`
- run the main view with the command `python contactlist_controller.py`



