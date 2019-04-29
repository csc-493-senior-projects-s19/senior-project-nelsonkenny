# This controller processes user actions as they relate to the announcement feature. 

from app.allImports import * # Imports flask and libraries needed 

     
@app.route("/announcements", methods=["GET"])
def getAnnouncements():
    
    announcements = Announcement.select() # select all the announcements in the database
    
    return render_template('announcements.html', announcements = announcements)

 
@app.route("/makeAnnouncement", methods=["GET"])
def makeAnnouncements(): 
    ''' This function directs the user to the interface they need to make a new 
    announcement on iRide!'''
    
    return render_template('makeAnnouncements.html')


@app.route("/submitAnnouncement", methods=["POST"])
def submitAnnouncements():
    ''' This function retrieves data from the form the user filled out when 
    making a new announcement and saves that data in the MYSQL db'''
    
    author = User.get(User.username == "nelsonk") # the author is meant to be the logged in user
    
    data = request.form # this is the information that the user imputted in the form 
    
    now = datetime.datetime.now() 
    
    date = now.strftime("%Y-%m-%d")
    
    time = now.strftime("%H:%M")
    
    content = data['announcement']
    
    announcement = Announcement(author = author.UID, date = date, time = time, content = content) # creates a new db instance in the Announcement table.
    
    announcement.save() # saves the new Announcement instance
    
    return redirect(url_for('getAnnouncements')) # redirects the user to the announcement home page. 
    
    
@app.route("/respondAnnouncement/<author>", methods=["GET"])
def respondAnnouncements(author):
    
    ''' This function directs the user to the interface they need to respond to an announcement'''
    # author is the user that originally made the announcement to which the logged in user is trying to respond to
    
    return render_template('respondAnnouncement.html', author = author)
    

    
@app.route("/respondAnnouncementSubmit/<author>", methods=["POST"])
def submitAnnouncementResponse(author):
    ''' This function retrieves data from the form the user filled out when 
    writing their response to the announcement and saves that data in the MySQL db.
    When a user responds to an announcement, that response is sent as a message to the author of that announcement.'''
   
    responder = User.get(User.username == "nelsonk") # the responder is meant to be the logged in user
    
    author = User.get(User.UID == int(author)) # the author is the user that created the original announcement
    
    data = request.form # this is the information that the user imputted in the form 
    
    now = datetime.datetime.now()
    
    date = now.strftime("%Y-%m-%d")
    
    time = now.strftime("%H:%M")
    
    content = "[Response to Announcement] " + data['announcement']

    message = Message(sender = responder.UID, receiver = author.UID, content = content, date = date, time = time) # creates a new db instance in the Message table.
    
    message.save() # saves the new Message instance

    return redirect(url_for("getAnnouncements")) # redirects the user to the announcement home page. 