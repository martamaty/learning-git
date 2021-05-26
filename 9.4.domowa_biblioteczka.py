<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tu tworzymy todo i widzimy listę</title>
    <style>
        table, th, tr, td {border: 1px solid black;}
    </style>
</head>

<h2>Lista zadań</h2>

<table>
    <thead>
    <th>Tytuł</th>
    <th>Opis</th>
    <th>Czy zrobione?</th>
    </thead>
{% for todo in todos %}
    <tr>
        <td><a href="/todos/{{ loop.index }}">{{ todo.title }}</a></td>
        <td>{{ todo.description }}</td>
        <td>{{ todo.done }}</td>
    </tr>
{% endfor %}
</table>
<div>
    <h2> Dodaj nowe zadanie: </h2>
    <form method="POST" action="/todos/">
        {{ form.hidden_tag() }}
        <table>
            {% for field in form if field.widget.input_type != 'hidden' %}
                <tr>
                    <th>{{ field.label }} {% if field.flags.required %}*{% endif %}</th>
                    <td>{{ field }}</td>
                </tr>
            {% endfor %}
        </table>
        <input type="submit" value="Go">
    </form>
</div>
</body>
</html>

[
  {
    "id": 1,
    "title": "Lekcja angielskiego",
    "description": "Czasowniki regularne",
    "done": false
  },
  {
    "id": 2,
    "title": "Python",
    "description": "Dekoratory",
    "done": false
  }
]
from flask import Flask, jsonify
from models import todos

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/api/v1/todos/", methods=["GET"])
def todos_list_api_v1():
    return jsonify(todos.all())


if __name__ == "__main__":
    app.run(debug=True)