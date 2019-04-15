from app.allImports import *


@app.route("/", methods=["GET"])
def home():
    driver_count = Driver.select().wrapped_count()
    rider_count = Rider.select().wrapped_count()
    request_count = Request.select().wrapped_count()
    
    return render_template('index.html', driver_count = driver_count, rider_count = rider_count, request_count = request_count)