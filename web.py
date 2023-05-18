from flask import Flask, render_template,request


web = Flask(__name__)



GPUS = [
    {
        'id' : 1,
        'name' : 'RX-570',
        'price' : '12,000$',
        'image' : '/static/gpu1.webp'

    },
    {
        'id' : 2,
        'name' : 'RX-571',
        'price' : '12,000$',
        'image' : '/static/gpu2.webp'

    },
    {
        'id' : 3,
        'name' : 'RX-572',
        'price' : '12,000$',
        'image' : '/static/gpu3.webp'

    },
    {
        'id' : 4,
        'name' : 'RX-573',
        'price' : '12,000$',
        'image' : '/static/gpu1.webp'

    },
    {
        'id' : 5,
        'name' : 'RX-574',
        'price' : '12,000$',
        'image' : '/static/gpu2.webp'

    },
    {
        'id' : 6,
        'name' : 'RX-575',
        'price' : '12,000$',
        'image' : '/static/gpu3.webp'

    },
    {
        'id' : 7,
        'name' : 'RX-576',
        'price' : '12,000$',
        'image' : '/static/gpu1.webp'

    },
    {
        'id' : 8,
        'name' : 'RX-577',
        'price' : '12,000$',
        'image' : '/static/gpu2.webp'

    },
    {
        'id' : 9,
        'name' : 'RX-578',
        'price' : '12,000$',
        'image' : '/static/gpu3.webp'

    },
]




@web.route("/")
@web.route("/home")
def home():
    return render_template("index.html")


@web.route("/product")
def product():
    return render_template("product.html", gpus = GPUS)
    

@web.route('/gpu/<int:product_id>', methods=['GET'])
def button_action(product_id):
    global ID
    ID = product_id
    return render_template('gpu.html', id=ID, gpus=GPUS)
if __name__ == "__main__":
    web.run(host='0.0.0.0', debug=True)
