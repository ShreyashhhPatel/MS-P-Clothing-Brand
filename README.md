  # Clothing Brand Project

![Django](https://img.shields.io/badge/Django-4.0-green?style=for-the-badge&logo=django) ![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python) ![JWT](https://img.shields.io/badge/JWT-Authentication-yellow?style=for-the-badge&logo=jsonwebtokens) ![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?style=for-the-badge&logo=sqlite) 


## Project Members
- Bibek shreshta - C0929407
- Shreyash V Patel - C0934529
- Megha Magar - C0933273

## Video link:  
https://drive.google.com/drive/folders/1KAYDYXZ-C3ljNZOi3nWKXPqP_5f_PX2Q?usp=sharing

## Project Description
This project is a **Clothing Brand Management System** built using Django. It provides functionality for customers to browse products, add items to the cart, and manage purchases. Admin users can manage products, view customer data, and oversee the inventory.

---

## Features
### 🛒 User Features
- **Authentication:** Secure login and signup using JWT.
- **Product Browsing:** View a catalog of suits and polo shirts.
- **Add to Cart:** Dynamically add and update items in the cart.
- **Checkout:** Manage purchases with dynamic inventory updates.

### 🛠️ Admin Features
- **User Management:** Add or delete users.
- **Product Management:** Add new products, update details, or delete inventory.
- **Admin Dashboard:** Comprehensive admin page for managing data.

---

## Technologies Used

### Backend
- **[Django](https://www.djangoproject.com/):** Python web framework.
- **[JWT (JSON Web Tokens)](https://jwt.io/):** Secure token-based authentication.

### Frontend
- **HTML5 & CSS3**

### Database
- **[SQLite](https://www.sqlite.org/):** Lightweight database for development.

---

## Setup Instructions

### Prerequisites
Ensure the following are installed on your system:
- [Python 3.12+](https://www.python.org/)
- [Pip (Python Package Installer)](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/clothing-brand.git
   cd clothing-brand
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```


4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Usage

### Endpoints
| Endpoint                  | Description                         |
|---------------------------|-------------------------------------|
| `/`                       | Home Page                          |
| `/login`                  | Login/Signup Page                  |
| `/suits`                  | View Suits Catalog                 |
| `/polo`                   | View Polo Shirts Catalog           |
| `/cart`                   | View Cart                          |
| `/admin`                  | Admin Dashboard                    |

### Admin Login Credentials
By default, an admin user can be created during setup. Update the database or create a superuser:
```bash
python manage.py createsuperuser
```

---

## Screenshots

### 🏠 Home Page
![Home Page](https://drive.google.com/file/d/1oPtO8b7YvlnfEWE_2UvmA_Yrc7n73tTV/view?usp=sharing)

### 📊 Admin Dashboard
![Admin Dashboard](https://drive.google.com/file/d/1oPtO8b7YvlnfEWE_2UvmA_Yrc7n73tTV/view?usp=sharing)

---

## References
- **[Django Documentation](https://docs.djangoproject.com/)**
- **[Bootstrap](https://getbootstrap.com/)**
- **[JWT Authentication](https://jwt.io/)**

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)

# MS-P-Clothing-Brand
Horizontal page with Django
