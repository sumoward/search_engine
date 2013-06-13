"""
    very first steps input/output, a GUI, an application server and persistence
"""
import pymongo
import bottle 

#connect to database
print('connected to database')
connection = pymongo.Connection('mongodb://localhost', safe =True)
db = connection.test
saved =db.saved

#our search page
@bottle.route('/search')
def search():
    print('Search engine go')
    return bottle.template('search')

#return the input to the user
@bottle.route('/answer')
@bottle.post('/answer')
def answer():
    print('Search engine answer')
    answer =bottle.request.forms.get('answer')
    
    #check if our answer is a string
    if answer != '':
        save_to_DB(answer)
    else:
        answer ='put your answer in the bloody box'
        
    return bottle.template('answer', answer = answer)

#save our answer to a database
def save_to_DB(answer):
    pass
    saved.insert({'answer':answer})
    print('Saved to database')

#start bottle
bottle.debug(True)
bottle.run(host='localhost', port=8082)