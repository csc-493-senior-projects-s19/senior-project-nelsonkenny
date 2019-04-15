from peewee import *
import sys
import mysql.connector
from app.models import *


dir_name  = os.path.dirname(__file__) # Return the directory name of pathname _file_
cfg       = load_config(os.path.join(dir_name, 'app/config/config.yaml'))
db_name   = cfg['db']['db_name']
host      = cfg['db']['host']
username  = cfg['db']['username']
password  = cfg['db']['password']

# Create a connection to the mysql database
cnx = mysql.connector.connect(database=db_name, host = host, password = password, user = username)

cursor = cnx.cursor()

# add_user = ("INSERT INTO user (`username`, `firstName`,`lastName`, `phone`, `email`, `password`) VALUES ('nelsonk', 'Kenny', 'Nelson', '859-9799739', 'nelsonk@berea.edu', 'kellog')")
# cursor.execute(add_user)

# add_user = ("INSERT INTO user (`username`, `firstName`,`lastName`, `phone`, `email`, `password`) VALUES ('akaboguf', 'Favour', 'Akabogu', '859-9765986', 'akaboguf@berea.edu', 'kelloge')")
# cursor.execute(add_user)

# add_driver = ("INSERT INTO driver (`user_id`) VALUES (4)")
# cursor.execute(add_driver)

# add_rider = ("INSERT INTO rider (`user_id`) VALUES (5)")
# cursor.execute(add_rider)

# add_form = ("INSERT INTO form (`destination`, `origin`,`date`, `time`, `notes`) VALUES ('Richmond Mall', 'Berea College - Alumni Circle', '05-13-2019', '10:00 AM', 'Thank you for your help!')")
# cursor.execute(add_form)

add_requests = ("INSERT INTO request (`driver_id`, `rider_id`, `form_id`, `status`) VALUES (2, 1, 1, 0)")
cursor.execute(add_requests)

add_message = ("INSERT INTO message (`sender_id`, `receiver_id`, `content`, `date` , `time` ) VALUES (4, 5, 'Hello There!', '09-11-18', '10:00 AM')")
cursor.execute(add_message)

add_announcement = ("INSERT INTO announcement(`author_id`, `date`, `time`, `content` ) VALUES (5, '09-11-18', '10:00 AM', 'I am going to Kentucky for Spring Break.' )")
cursor.execute(add_announcement)

cnx.commit()
cursor.close()
cnx.close()
               