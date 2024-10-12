# Flask Order System Application

This is a simple Flask-based e-commerce application that allows users to browse products, place orders, and provides an admin interface for managing products and orders.

## Features

- **Product Browsing:** Users can view all available products and search for specific items.
- **Product Details:** Each product has a dedicated page with details and an option to place an order.
- **Admin Interface:** Admins can log in, add new products, update existing products, and delete products.
- **Order Management:** Orders placed by users are stored in the database for administrative review.

## Technologies Used

- **Flask:** The web framework for building the application.
- **SQLAlchemy:** ORM for database management.
- **HTML/CSS:** For front-end design.
- **Bootstrap:** For responsive design.
- **Werkzeug:** For secure file handling.

## Setup Instructions

### Prerequisites

- Python 3.x
- Flask
- SQLAlchemy
- A database (SQLite or any other supported by SQLAlchemy)
- [dotenv](https://pypi.org/project/python-dotenv/) for environment variable management

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ahmedsamir45/order-system.git
    cd order-system
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables by creating a `.env` file in the root directory:
    ```plaintext
    USERNAME1=your_username
    PASSWORD=your_password
    UPLOAD_FOLDER=/path/to/upload/folder
    ```

4. Initialize the database (create the necessary tables):
    ```bash
    flask shell
    from app import db
    db.create_all()
    exit()
    ```

5. Run the application:
    ```bash
    flask run
    ```

6. Open your browser and navigate to `http://127.0.0.1:5000/`.

## Routes

| Route                 | Method | Description                               |
|-----------------------|--------|-------------------------------------------|
| `/`                   | GET    | Home page displaying all products.       |
| `/search`             | GET    | Search for products by name.             |
| `/product/<int:id>`   | GET, POST | View product details and place an order. |
| `/login`              | GET, POST | Login page for admin users.              |
| `/logout`             | GET    | Logout and redirect to home.             |
| `/admin`              | GET, POST | Admin dashboard to manage products and orders. |
| `/admin/update/<int:id>` | GET, POST | Update product details.                  |
| `/admin/delete/<int:id>` | POST  | Delete a product.                        |
| `/about`              | GET    | About page.                               |
| `/contact`            | GET    | Contact page.                             |

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Bootstrap Documentation](https://getbootstrap.com/)
