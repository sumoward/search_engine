"""
    very first steps input/output, a GUI, an application server and persistence
"""
# import pymongo
import bottle


# # connect to database
# print('connected to database')
# connection = pymongo.Connection('mongodb://localhost', safe=True)
# db = connection.test
# saved = db.saved

# our search page
@bottle.route('/search')
def search():
    print('Go here to log in go')
    return bottle.template('search')


# return the input to the user
@bottle.route('/answer')
@bottle.post('/answer')
def answer():
    print('Logged in')
    username = bottle.request.forms.get('username')
    password = bottle.request.forms.get('password')
    # check if our answer is a string
    if username != '':
        save_to_DB(username)
    else:
        username = 'put your answer in the bloody box'
    return bottle.template('answer', username=username, password=password)


# save our answer to a database
def save_to_DB(answer):
    # saved.insert({'answer': answer})
    print('Saved to database')


# start bottle
bottle.debug(True)
bottle.run(host='0.0.0.0', port=8082)
