from app.allImports import *

     
@app.route("/announcements", methods=["GET"])
def getAnnouncements():
    announcements = Announcement.select()
    return render_template('announcements.html', announcements = announcements)

 
@app.route("/makeAnnouncement", methods=["GET"])
def makeAnnouncements():
    
    return render_template('makeAnnouncements.html')


@app.route("/submitAnnouncement", methods=["POST"])
def submitAnnouncements():
    
    author = User.get(User.username == "nelsonk")
    
    data = request.form 
    
    now = datetime.datetime.now()
    
    date = now.strftime("%Y-%m-%d")
    
    time = now.strftime("%H:%M")
    
    content = data['announcement']
    
    announcement = Announcement(author = author.UID, date = date, time = time, content = content)
    
    announcement.save()
    
    return redirect(url_for('getAnnouncements'))
    
    
@app.route("/respondAnnouncement/<author>", methods=["GET"])
def respondAnnouncements(author):
    return render_template('respondAnnouncement.html', author = author)
    

    
@app.route("/respondAnnouncementSubmit/<author>", methods=["POST"])
def submitAnnouncementResponse(author):
    
    responder = User.get(User.username == "nelsonk")
    
    author = User.get(User.UID == int(author))
    
    data = request.form 
    
    
    now = datetime.datetime.now()
    
    date = now.strftime("%Y-%m-%d")
    
    time = now.strftime("%H:%M")
    
    content = "[Response to Announcement] " + data['announcement']

    message = Message(sender = responder.UID, receiver = author.UID, content = content, date = date, time = time)
    
    message.save()
    
    return redirect(url_for("getAnnouncements"))