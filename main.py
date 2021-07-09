import flask
from flask import request, jsonify
#from bus.bus import Bus
#from category.category import Category

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.

cat = {'name':'tradicional',
       'base_ticket_cost':4.0,
       'cross_cost':0.6,
       'max_cross':4}

route1 = [
       {'name': 'N1',
        'region': 'norte',
        'timestamp': 10},
       {'name': 'N2',
        'region': 'norte',
        'timestamp': 11},
       {'name': 'L1',
        'region': 'leste',
        'timestamp':14},
       {'name': 'S1',
        'region': 'sul',
        'timestamp': 15}
]

bus = {
    'id':0,
    'route':route1,
    'category':cat
}

trips = [{
        'id':0,
        'boarding_time': 11,
        'boarding_station': 'N2',
        'disembark_time':14,
        'disembark_station':'L1',
        'trip_cost': 0.0
        },
        {
        'id':1,
        'boarding_time': 10,
        'boarding_station': 'N1',
        'disembark_time':15,
        'disembark_station':'L2',
        'trip_cost': 0.0
        }

]


def get_regions_crossed(bus, ini_time, end_time):
    regions = []
    count = 0
    for station in bus['route']:
        if station['timestamp'] >= ini_time and station['timestamp'] <= end_time and station['region'] not in regions:
            regions.append(station['region'])
            count = count +1
    return count

#127.0.0.1:5000/api/v1/trip/cost?id=0
@app.route('/api/v1/trip/cost', methods=['GET'])
def compute_cost():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    for trip in trips:
        if trip['id']==id:
            count=get_regions_crossed(bus,trip['boarding_time'],trip['disembark_time'])-1
            if count > bus['category']['max_cross']:
                count = bus['category']['max_cross']
            bill=count*bus['category']['cross_cost']+bus['category']['base_ticket_cost']
            trip['trip_cost']=bill
            break
    return jsonify(trip)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Computing travel costs</h1>
<p>A prototype API for computing travel costs.</p>'''


@app.route('/api/v1/trip/all', methods=['GET'])
def api_all():
    return jsonify(trips)


app.run()
