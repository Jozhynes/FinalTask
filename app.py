from flask import Flask, render_template, request,redirect,url_for
from models import Product
from connections import Sessionlocal

app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    db=Sessionlocal()
    if request.method=="POST":
        name=request.form['name']
        if name:
            new_product=Product(name=name)
            db.add(new_product)
            db.commit()
            db.refresh(new_product)
        db.close()
        
    return render_template('index.html')



@app.route('/show_product')
def show_product():
    db = Sessionlocal()
    product = db.query(Product).all()  
    db.close()
    return render_template('product.html', product=product)



@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        print(f"Message from {name} ({email}): {message}")

        return "Thank you for contacting us!"
    
    return render_template("contact.html")


if __name__=='__main__':
    app.run(debug=True)
    

    