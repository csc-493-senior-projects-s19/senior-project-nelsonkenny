''' This controller oversees user actions related to the messaging feature.'''
from app.allImports import * # Imports flask and libraries needed 

@app.route("/messages", methods=["GET"])
def getMessages():
    
    user = User.get(User.username =='nelsonk') # user is meant to be the logged in user
    
    messages = Message.select().where(Message.sender == user.UID) # select all the messages that the logged in user has either sent or received
    
    return render_template('messages.html', messages = messages)
    
    

@app.route("/writeMessage/<REID>", methods=["GET","POST"])
def writeMessages(REID):
    ''' This function directs the user to the interface they need to write a new '''
    return render_template('writeMessage.html', REID)
    
@app.route("/respondMessage/<receiver>/<sender>", methods=["GET","POST"])
def respondMessage(receiver, sender):
 
 return render_template('writeMessage.html', receiver = receiver, sender = sender)

@app.route("/submitMessage/<receiver>/<sender>", methods=["POST"])
def submitMessage(receiver, sender):
    data = request.form 
    
    now = datetime.datetime.now()
    
    date = now.strftime("%Y-%m-%d")
    
    time = now.strftime("%H:%M")
    
    receiver = User.get(User.UID == receiver)
    
    sender = User.get(User.UID == sender)
    
    content = data['content']
    
    message = Message(sender = sender, receiver = receiver, content = content, date = date, time = time)
    
    message.save()
    
    return redirect(url_for('getMessages'))

@app.route("/messageRider/<REID>", methods=["GET","POST"])
def messageRider(REID):
    
    return render_template('messageRider.html', REID = REID)

@app.route("/sendMessageRider/<REID>", methods=["POST"])
def sendMessageRider(REID):
    data = request.form 
    
    now = datetime.datetime.now()
    
    date = now.strftime("%Y-%m-%d")
    
    time = now.strftime("%H:%M")
    
    requestForm = Request.get(Request.REID == REID)
    
    driver = Driver.get(Driver.DID == requestForm.driver)
    
    rider = Rider.get(Rider.RID == requestForm.rider)
    
    print(driver.DID, rider.RID)
    
    content = data['content']
    
    message = Message(sender = driver.user, receiver = rider.user, content = content, date = date, time = time)
    
    message.save()
    
    return redirect(url_for('viewMyOffers'))
    
@app.route("/messageDriver/<REID>", methods=["GET","POST"])
def messageDriver(REID):
    
    return render_template('messageDriver.html', REID = REID)

@app.route("/sendMessageDriver/<REID>", methods=["POST"])
def sendMessageDriver(REID):
    data = request.form 
    
    now = datetime.datetime.now()
    
    date = now.strftime("%Y-%m-%d")
    
    time = now.strftime("%H:%M")
    
    requestForm = Request.get(Request.REID == REID)
    
    driver = Driver.get(Driver.DID == requestForm.driver)
    
    rider = Rider.get(Rider.RID == requestForm.rider)
    
    content = data['content']
    
    message = Message(sender = rider.user, receiver = driver.user, content = content, date = date, time = time)
    
    message.save()
    
    return redirect(url_for('viewMyRequests'))