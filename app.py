import os,json
from flask import Flask, request, render_template,jsonify
from flask_caching import Cache
from flask_pymongo import PyMongo




app=Flask(__name__)

#Using MongoDb Service provider Mlab free sandbox
#Pymongo driver to connect mongodb
app.config['MONGO_DBNAME']='ps_time_table'
app.config['MONGO_URI']='mongodb://testdev:testdev@ds139262.mlab.com:39262/ps_time_table'

#Initialize cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

mongo = PyMongo(app)

'''
Main fuction to load census data ist fetching 10k data 
Cashing for 100 sec to get the time to fech the data from db
In that time use can use the appliction.
'''
@app.route('/')
@cache.cached(timeout=100)
def home_page():
    data= list(mongo.db.census.find().limit(1000))
    return render_template('index.html',data=data)

#To get the gender type  count
#Converting json array to dist type
@app.route('/gender')
def getMaleFemaleCount():
    result= list(mongo.db.census.aggregate([{"$group":{"_id":"$sex","count":{"$sum":1}}}]))
    countResult= {}
    for res in result:
        countResult[res.get('_id')] = res.get('count')
    return jsonify(json.dumps(countResult))

#To count relationship type count
#Converting json array to dist type 
@app.route('/relationship')
def getRelationshipCount():
    result= list(mongo.db.census.aggregate([{"$group":{"_id":"$relationship","count":{"$sum":1}}}]))
    countResult= {}
    for res in result:
        countResult[res.get('_id')] = res.get('count')
    return jsonify(json.dumps(countResult))

    
    
    
    
#This fucntion get all data from data base and save it
#In a cache 
# @cache.cached(timeout=50, key_prefix='censusData')
# def getFullData():
#     data= list(mongo.db.census.find().limit(5))
#     return data
    
# app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

port = int(os.environ.get('PORT', 5000))
app.run(host="0.0.0.0", port=port, debug=True)