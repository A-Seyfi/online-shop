# Online Shop

A full-featured e-commerce platform built with Django. This project provides a complete online shopping experience with product management, user accounts, shopping carts, orders, and a modular architecture for easy maintenance and expansion.

## Features

- **Product Management:** Browse products by category and brand with detailed specifications
- **Product Customization:** Select variants like color, RAM, storage, and warranty options with dynamic pricing
- **User Accounts:** User registration, authentication, and profile management
- **Favorites:** Save products to a personal favorites list
- **Shopping Cart:** Add/remove items with variant selection
- **Order Management:** Complete order workflow with tracking
- **Admin Dashboard:** Django admin interface for managing products, categories, brands, and orders
- **Search & Filtering:** Find products by category, brand, and tags
- **Reviews & Comments:** Hierarchical comment system with nested replies
- **Product Gallery:** Multi-image support for products
- **Iranian Localization:** Support for Persian (Farsi) language and Jalali calendar

## Tech Stack

- **Backend:** Django 4.x
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Image Processing:** Pillow, Sorl-Thumbnail
- **Date Handling:** django-jalali-date, jdatetime
- **Payment Integration:** Meli Payamak (SMS/payment gateway)
- **Utilities:** Django Widget Tweaks, Fuzzy-Wuzzy matching, requests

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/A-Seyfi/online-shop.git
   cd online-shop
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r req.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### Accessing the Application

- **Home Page:** `http://127.0.0.1:8000/`
- **Admin Panel:** `http://127.0.0.1:8000/admin/` (use superuser credentials)

### Core Workflows

**Browsing Products:**
Navigate to the product catalog, filter by category or brand, and view detailed specifications including processor, RAM, storage, and connectivity options.

**Managing Variants:**
Products support customization through:
- Colors with price adjustments
- RAM options
- Storage capacity
- Warranty plans

Select your preferences and the total price updates automatically.

**User Account:**
Sign up to access your profile, order history, and saved favorites.

**Placing Orders:**
Add products to your cart with selected variants, review your order, and proceed to checkout.

## Project Structure

```
online-shop/
├── eshop_project/          # Main project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routing
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
│
├── account_module/         # User authentication and profiles
├── product_module/         # Product catalog and management
├── order_module/           # Order processing
├── user_panel_module/      # User dashboard
├── home_module/            # Homepage and site navigation
├── contact_module/         # Contact and messaging
├── site_module/            # Site-wide settings
├── polls/                  # Polling functionality
│
├── templates/              # HTML templates
│   ├── emails/             # Email templates
│   └── shared/             # Shared template components
│
├── static/                 # CSS, JavaScript, and images
├── uploads/                # User-uploaded media
├── db.sqlite3              # Database file
├── manage.py               # Django CLI
└── req.txt                 # Python dependencies
```

## Configuration

Edit `eshop_project/settings.py` to customize:
- `DEBUG` mode for development/production
- `ALLOWED_HOSTS` for your domain
- `DATABASES` connection settings
- `LANGUAGE_CODE` (currently set to Persian)
- `TIME_ZONE` settings
- Media and static file paths

## Database Models

Key models in the application:

- **Product:** Main product entity with detailed specifications
- **ProductCategory & ProductBrand:** Product organization
- **Color, RAM, Storage, Warranty:** Product variants with pricing
- **Order & OrderItem:** Order management
- **ProductComment:** Nested comment system
- **ProductGallery:** Multi-image support
- **Favorite:** User's saved products
- **ProductVisit:** Analytics tracking

## Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit with clear messages (`git commit -m 'Add feature: ...'`)
5. Push to your branch (`git push origin feature/your-feature`)
6. Open a pull request

When contributing, please follow Django best practices and ensure backward compatibility with existing modules.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Last Updated:** October 2024
