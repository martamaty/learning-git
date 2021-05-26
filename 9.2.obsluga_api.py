import os

from flask import Flask, render_template, request

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/images/", methods=["GET", "POST"])
def form_view():
    if request.method == "POST":
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return "File is uploaded"
    return render_template('form_with_image_example.html')

if __name__ == '__main__':
    app.run(debug=True)

import json

data = {"data": {
  "id": 1,
  "name": "Something",
  "colors": ["red", "blue"]
  }
}

print(type(data))
# <class 'dict'>

# zróbmy z tego JSON
data_as_json = json.dumps(data)
print(type(data_as_json))
# <class 'str'>
print(data_as_json)
# {"data": {"id": 1, "name": "Something", "colors": ["red", "blue"]}}

# zróbmy z JSON-a obiekt pythonowy
data_from_json = json.loads(data_as_json)
print(type(data_from_json))
# <class 'dict'>
print(data_from_json)
# {'data': {'id': 1, 'name': 'Something', 'colors': ['red', 'blue']}}

import pickle

tasks = [
    {
        'id': 1,
        'title': 'Zakupy',
        'description': 'Mleko, jajka, mąka, olej, papier toaletowy (jak będzie)',
        'done': False
    },
    {
        'id': 2,
        'title': 'Zrobić zadania z Pythona',
        'description': 'Przygotować projekt z modułu i wysłać Mentorowi',
        'done': False
    }
]

with open("todo.pickle", 'wb') as f:
    pickle.dump(tasks, f)