from flask import Flask
from routes.products import products_blueprint


app = Flask(__name__)
app.register_blueprint(products_blueprint)



@app.route("/")
def home():
    return "Inventory Management System"




if __name__ == "__main__":
    app.run(debug=True)