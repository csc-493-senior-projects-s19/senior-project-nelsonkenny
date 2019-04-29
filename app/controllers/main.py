''' This controller simply loads the home page '''
from app.allImports import *


@app.route("/", methods=["GET"])
def home():
    driver_count = Driver.select().wrapped_count() # This is the number of people who have offered a ride on the application
    rider_count = Rider.select().wrapped_count() # This is the number of people who have requested a ride on the application
    request_count = Request.select().wrapped_count() # This is the number of ride requests submitted on the application 
    return render_template('index.html', driver_count = driver_count, rider_count = rider_count, request_count = request_count)