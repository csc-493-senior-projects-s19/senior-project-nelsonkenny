from app.allImports import *

     
@app.route("/offer", methods=["GET"])
def offerRides():
    ride_requests = Request.select().where(Request.driver == None)
    return render_template('offerRides.html', ride_requests = ride_requests)
    
@app.route("/offer/accept/<reid>", methods=["GET"])
def acceptRequest(reid):
    request = Request.get(Request.REID == int(reid))
    request.driver = 2
    request.save()
    return redirect(url_for("offerRides"))
  