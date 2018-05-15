from flask import Flask, request, render_template,jsonify
from flask_pymongo import PyMongo
import os,json


app=Flask(__name__)

#Using MongoDb Service provider Mlab free sandbox
app.config['MONGO_DBNAME']='ps_time_table'
app.config['MONGO_URI']='mongodb://devuser:sipan123.#@ds139262.mlab.com:39262/ps_time_table'


mongo = PyMongo(app)


@app.route('/')
def home_page():
    # dist={}
    # dist= mongo.db.census.aggregate([{"$group":{"_id":"$sex","count":{"$sum":1}}}])
    return render_template('index.html')

@app.route('/grap')
def getCount():
    male_count = mongo.db.census.find({'sex':'Male'}).count()
    female_count=mongo.db.census.find({'sex':'Female'}).count()
    r = {'Male': male_count, 'Female': female_count}
    return jsonify(json.dumps(r) )


# if __name__ == '__main__':
#   app.run()

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

# port = int(os.environ.get('PORT', 5000))
# app.run(host="0.0.0.0", port=port, debug=True)