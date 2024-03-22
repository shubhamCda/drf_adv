from flask import Flask

app = Flask(__name__)


items = [
    {"item": "apple", "price": 1.25},
    {"item": "banana", "price": 0.75}
]


@app.get('/get-items')
def get_items():
    return {"items": items}