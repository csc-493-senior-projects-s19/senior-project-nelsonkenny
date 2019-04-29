from app.allImports import *


@app.route("/request", methods=['GET'])
def newRequest():
    return render_template('requestRides.html')
    
    
@app.route("/request/submit", methods=['POST'])
def requestSubmit():
    data = request.form
    
    form = Form(destination = data['destination'], origin = data['origin'], date = data['date'], time = data['time'], notes = data['notes'])
    form.save()
    
    user = User.get(User.email==data['email'])
    
    rider = Rider.get(Rider.user == user.UID)
    rider_id = rider.RID

    ride_request = Request(rider = rider_id , form = form, status = 0)
    ride_request.save()
    
    flash("Your ride request was successfully submitted!")
    return redirect(url_for('home'))
    
@app.route("/view/myrequests", methods=['GET'])
def viewMyRequests():
    user = User.get(User.username == "nelsonk")
    rider = Rider.get(Rider.user == user.UID)
    rider_id = rider.RID
    my_requests = Request.select().where(Request.rider == rider_id ).distinct()
   
    return render_template("myRideRequests.html", my_requests = my_requests)

@app.route("/view/myrideoffers", methods=['GET'])
def viewMyOffers():
    user = User.get(User.username == "nelsonk")
    driver = Driver.get(Driver.user == user.UID)
    driver_id = driver.DID
    
    my_offers = Request.select().where(Request.driver == driver_id)

    return render_template("myRideOffers.html", my_offers = my_offers)