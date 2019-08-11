from flask import Flask, jsonify
app = Flask(__name__)
Student = [
{
 'id': 1,
 'firstName': 'Aditya',
 'lastName': 'Malviya',
 'age': '24'
},
{
 'id': 2,
 'firstName': 'Aman',
 'lastName': 'Mehta',
 'age': '25'
},
{
 'id': 3,
 'firstName': 'Nuclear',
 'lastName': 'Geeks',
 'age': '26'
}
]
@app.route('/student/', methods=['GET'])
def get_Student():
   return jsonify({'tasks': Student})
if __name__ == '__main__':
        app.run()

@app.route('/student/', methods=['POST'])
def add_task():
    student = {
        'id': Student[-1]['id'] + 1,
        'firstName': request.json['firstName'],
        'lastName': request.json.get('lastName', ""),
        'age': request.json.get('age',"27")
}
    Student.append(student)
    return jsonify({'student': student}), 201
