from app.allImports import *

     
@app.route("/announcements", methods=["GET"])
def getAnnouncements():
    
    return render_template('announcements.html')

 
@app.route("/makeAnnouncement", methods=["GET"])
def makeAnnouncements():
    
    return render_template('makeAnnouncements.html')


@app.route("/submitAnnouncement", methods=["GET"])
def submitAnnouncements():
    
    return render_template('makeAnnouncements.html')
    
    
@app.route("/respondAnnouncement", methods=["GET"])
def respondAnnouncements():
    
    return render_template('respondAnnouncement.html')
    

    
@app.route("/respondAnnouncementSubmit", methods=["GET"])
def submitAnnouncementResponse():
    
    return redirect(url_for("getAnnouncements"))