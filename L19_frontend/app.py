from flask import Flask,request, render_template
from views import product_app

app = Flask(__name__)
app.register_blueprint(product_app, url_prefix="/products")

@app.route("/", methods=['POST', 'GET']) # обработчик индекса "/"
def index():
    name = "World"
    if request.method == 'POST':
        name = request.form.get('name', default='WORLD')
    return render_template("index.html", name="World")

# app.add_url_rule("/", "index", index) # устаревшая альтернатива декоратору @app.route
# app.add_url_rule("/", view_func=index)

@app.route("/hello/")
@app.route("/hello/<string:name>/")
def hello(name=None):
    if name is None:
        name = 'WORLD'
    return f"<h1>Hello, {name}!</h1>"

# @app.route("/post/<post_id>/")
# def alt_show_post(post_id):
#     post_id > 0
#     return f"Post (str) {post_id}"

@app.route("/post/<int:post_id>/")
def show_post(post_id):
    return f"Post (int) {post_id}"

