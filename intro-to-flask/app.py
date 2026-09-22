from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "My server is running."


@app.route('/todos')
def todos():
    return {
            "my todos": [
                {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    },
    {
        "userId": 1,
        "id": 2,
        "title": "quis ut nam facilis et officia qui",
        "completed": False
    },
        ]
    }



if __name__ == "__main__":
    app.run(debug=True)