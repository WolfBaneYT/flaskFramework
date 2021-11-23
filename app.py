from flask import Flask, json,jsonify,request
#Constructor
app = Flask(__name__)
contacts = [
    {
        'Contact' : '0123456789',
        'Name' : 'Rick Astley',
        'done' : False,
        'id' : 1
    },
    {
        'Contact' : '1142536475869',
        'Name' : 'Eggman from China',
        'done' : False,
        'id' : 2
    }
]
@app.route("/add-data",methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide data'
        },400)
    contact={
        'id':contacts[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',''),
        'done':False
    }
    contacts.append(contact)
    return jsonify({
        'status':'success',
        'message':'task added successfully'
    })
@app.route('/get-data')
def get_task():
    return jsonify({
        'data':contacts
    })
if __name__ == "__main__":
    app.run()