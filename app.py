from flask import Flask,render_template
import product_list

app = Flask(__name__)

@app.route("/")
def index():
    user_name = "Shimizu"
    return render_template("index.html",user_name=user_name)

@app.route("/product")
def product():
    product_list = ["computer1","computer2","computer3"]
    product_dict = {"product_name":"computer1","product_price":"4300","product_maker":"maker1"}
    return render_template("product.html",products=product_list,product_dict=product_dict)

@app.route("/user/<user_id>")
def userid(user_id):
    return "<h1>Your User ID is {0} {1} {2}</h1>".format(user_id[0],user_id[1],user_id[2])

@app.route("/user")
def user():
    user_list = [
        ["1","山田　太郎", "taro@test.com", "1"],
        ["2","鈴木　花子", "hanako@test.com", "0"],
        ["3","清水　義孝", "yoshitaka@test.com", "0"]
    ]
    return render_template("user.html", users=user_list)

@app.errorhandler(404)
def error_404(error):
    return render_template("error_pages/404.html"), 404
    
if __name__ == "__main__":
    app.run(debug=True)