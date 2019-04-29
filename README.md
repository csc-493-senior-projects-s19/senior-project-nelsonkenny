## Built With

* [Flask](http://flask.pocoo.org/docs/0.11/)  - Python Based Web Framework Used
* [Jinja2](http://jinja.pocoo.org/docs/dev/) - HTML Templating Language for Python
* [Peewee](http://docs.peewee-orm.com/en/latest/index.html) - A small, expressive ORM used for database communications
* [SQLite](https://mysql.org/) - SQL database engine

# Setting Up a Development Environment
### Getting Started On Cloud9 ###
[Cloud9](https://c9.io/?redirect=0) is the preferred IDE to run iRide!

### Create a Workspace with Bitbucket using SSH Protocol

When you first log into your cloud9 account, select the tab that says **workspaces**. 
After you open this tab you should see an option to create a new workspace, it should look like the image below.

![creatework.PNG](https://bitbucket.org/repo/bEXb4L/images/4213557604-creatework.PNG) 

After you click the button go ahead and input a name and description for this workspace.

![description.PNG](https://bitbucket.org/repo/bEXb4L/images/2446581179-description.PNG)
![public.PNG](https://bitbucket.org/repo/bEXb4L/images/69137571-public.PNG)

Once you have a workspace, clone the iRide repository from github in the terminal using the git clone command in the terminal. 

3 steps before you can run iRide on cloud9:

**Step One: Activate Your Virtual Environment**

Run the command ```source setup.sh``` into the Linux terminar. This command git installs all the dependencies and libraries you will need. Once the setup is completed you should see the words ```(venv)``` at the front of your terminal.

**Step Two: Setup Your Database**

A couple of elements are necessary in order to get your database established. The first step is creating the SQLite file, we can create the file in the desired location through the use of one of our scripts.

**Create Database** : 
 - Type the command: mysql-ctl install, which creates a mysql instance in c9
 - In app/config/config.yaml, on line 5 chnage the username field to your c9 username
 - Type the command ```python create_db.py```. This command will create the sql database and the tables needed to store data for the application 
 **To visualize the database in a phpmyadmin instance, in the terminal, type the command, phpmyadmin-ctl install which will give you a URL to copy in your browser.
 I recomment using phpmyadmin because it allows you to visualize the data better.**


**Step Three: Running the Application**

The only remaining step to getting your development environment deployed is running the actual application. This can be achieved through the command ```python app.py```, when you run this command you should see a URL created for you. 

![run.PNG](https://bitbucket.org/repo/bEXb4L/images/1543001500-run.PNG)

The URL will take you to the application and allow you to see any changes you make to the system. 
That's all that has to be done in order to get the development environment created and ready for editing.

iRide is built on an MVC model. As a result, all user interface code is in the templates 
folder while all the database related code is in the models folder and the python code for 
data retrieval and processing is in the controllers folder. 

# These are the controllers that process of the user actions in the application. 
from app.controllers.offerRides import *
from app.controllers.requestRides import *
from app.controllers.main import *
from app.controllers.message import *
from app.controllers.announcement import *

# These are the database tables that store data for the application
from app.models.Form import *
from app.models.Request import *
from app.models.OfferPassenger import * 
from app.models.Offer import *
from app.models.User import *
from app.models.Driver import *
from app.models.Rider import *
from app.models.Announcement import *
from app.models.Message import *