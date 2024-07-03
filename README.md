# Smart Shop Billing System

Welcome to the Smart Shop Billing System GitHub repository! This repository contains a Python application for managing billing and inventory in a shop. Below is a brief overview of the application's features and how to use it.

## Features

- **Login System**: Users can log in with their username and password.
- **Dashboard**: Provides an overview of the shop's operations.
- **Add Products**: Allows users to add new products to the inventory.
- **Billing/Invoicing**: Enables users to generate invoices for purchases.
- **Barcode Generation**: Generates barcodes for products using QR codes.
- **Database Integration**: Utilizes SQLite for storing product and user data.

## Installation

To run the Smart Shop Billing System locally, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Atul-dubal/Python-Billing-System.git
   ```

2. Navigate to the project directory:

   ```bash
   cd smart-shop-billing-system
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python main.py
   ```
## Default Credentials
Username : admin

Password : admin123
## Usage

Upon launching the application, you will be prompted to log in with your username and password. Once logged in, you can access the dashboard, add products to the inventory, and generate invoices for purchases.

### Login

- Enter your username and password to log in.

### Dashboard

- Provides an overview of the shop's operations.

### Add Products

- Enter the product name, quantity, and price to add a new product to the inventory.
- Click the "Make Barcode" button to generate a QR code for the product.

### Billing/Invoicing

- Select products from the inventory to add them to the invoice.
- Click the "Print" button to generate and print the invoice.

## Contributing

Contributions to the Smart Shop Billing System are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new pull request.

## Author

This tool is developed by Atul Dattatray Dubal.

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) 4.0 International License.](LICENSE).

## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI (Graphical User Interface) package.
- [SQLite](https://www.sqlite.org/index.html) - A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
- [PyQRCode](https://pypi.org/project/PyQRCode/) - A QR Code generator library for Python.
- [ReportLab](https://www.reportlab.com/devspot/) - A Python library for generating PDF documents.
