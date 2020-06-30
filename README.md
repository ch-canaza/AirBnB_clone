#0x00. AirBnB clone - The console#

Welcome to the AirBnB clone project! (The Holberton B&B)

In this project we are going to create the first part of the Airbnb clone, for this you want to create a console where you can manage Airbnb objects or instances.

#CONSOLE FUNCTIONALITIES#

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

#INSTALLATION#

git clone https://github.com/ch-canaza/AirBnB_clone.git
cd AirBnB_clone

#USABILITY#

INTERACTIVE MODE

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

NON-INTERACTIVE

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

#UNITTEST#

All the commands were tested and reviewed with unittest to ensure their 
functionality and minimize the probability of errors.

#DEPLOYMENT#

Your team must be Ubuntu or use a virtual machine with this operating system.

To install on your computer you must download the project folders from the git described above.

Enter the project folder.

Run the ./console.py code

Enjoy

#BUILT WITH#

Python3

#EXAMPLES#

#EXAMPLE FOR help#

./console.py

Help

Help create

This is the output

     Creates a new instance of BaseModel,
     saves it (to the JSON file) and prints the id.
     Ex: $ create BaseModel

help destroy

This is the output

    Deletes an instance based on the class name and id

#Example for all, create, show#

Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.

./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}

#EXAMPLE FOR DESTROY#



