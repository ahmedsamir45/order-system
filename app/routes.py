import os
from flask import render_template, flash, redirect, url_for, request, session
from app import app, db
from app.models import Product, Order
from werkzeug.utils import secure_filename
from sqlalchemy import or_
import os
from dotenv import load_dotenv

# Hardcoded credentials for simplicity
USERNAME = os.environ.get('USERNAME1')
PASSWORD = os.environ.get('PASSWORD')
print(USERNAME)
print(PASSWORD)

@app.route('/')
def index():
    
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        products = Product.query.filter(Product.name.like(f'%{query}%')).all()
    else:
        products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:id>', methods=['GET', 'POST'])
def product(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        new_order = Order(product_id=product.id, name=name, email=email, phone=phone, address=address)
        db.session.add(new_order)
        db.session.commit()
        flash('Order placed successfully!')
        return redirect(url_for('index'))
    return render_template('product.html', product=product,style="product")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            flash('You were successfully logged in')
            return redirect(url_for('admin'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were successfully logged out')
    return redirect(url_for('index'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_product = Product(name=name, description=description, price=price, image_filename=filename)
            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully!')
            return redirect(url_for('admin'))
    products = Product.query.all()
    orders = Order.query.all()
    return render_template('admin.html', products=products, orders=orders,style="admin")

@app.route('/admin/update/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    product = Product.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            product.name = request.form['name']
            product.description = request.form['description']
            product.price = float(request.form['price'])
            
            # Handle file upload if present
            if 'image' in request.files:
                file = request.files['image']
                if file and file.filename != '':
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    product.image_filename = filename

            db.session.commit()
            flash('Product updated successfully!', 'success')
            return redirect(url_for('admin'))
        except KeyError as e:
            flash(f'Missing field: {e.args[0]}', 'danger')
        except ValueError:
            flash('Invalid price value', 'danger')
    
    return render_template('update_product.html', product=product)

@app.route('/admin/delete/<int:id>', methods=['POST'])
def delete_product(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!')
    return redirect(url_for('admin'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
