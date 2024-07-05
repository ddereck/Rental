
---

# Car Rental Application

This project is a car rental application built with Django for the backend and Vue.js for the frontend. The application allows users to register, browse cars, make rentals, manage payments, leave testimonials, and receive notifications.

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Setup](#setup)
- [Backend (Django)](#backend-django)
- [Frontend (Vue.js)](#frontend-vuejs)
- [APIs](#apis)
- [Microservices](#microservices)
- [Database Schema](#database-schema)
- [License](#license)

## Features
- User registration and authentication
- Car listing and searching
- Rental booking and management
- Payment processing
- User testimonials
- Notification system
- Discounts and promotions

## Architecture
The application follows a microservices architecture. The primary services are:
- **User Service**: Manages user accounts and authentication.
- **Car Service**: Manages car listings and inventory.
- **Rental Service**: Manages rental bookings.
- **Payment Service**: Handles payment transactions.
- **Notification Service**: Sends notifications to users.
- **Stats Service**: Generates statistics and reports.
- **Discount Service**: Manages discounts and promotions.

## Setup

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or Yarn
- PostgreSQL

### Backend (Django)
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/car-rental-app.git
    cd car-rental-app/backend
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database and update the `DATABASES` settings in `settings.py`.

5. Run migrations:
    ```sh
    python manage.py migrate
    ```

6. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

7. Start the development server:
    ```sh
    python manage.py runserver
    ```

### Frontend (Vue.js)
1. Navigate to the frontend directory:
    ```sh
    cd ../frontend
    ```

2. Install the dependencies:
    ```sh
    npm install
    ```

3. Start the development server:
    ```sh
    npm run serve
    ```

## APIs
The application exposes various RESTful APIs for different functionalities. Below are the key endpoints:

### User Service
- `POST /api/users/register/`: Register a new user
- `POST /api/users/login/`: Login a user
- `POST /api/users/logout/`: Logout a user
- `GET /api/users/profile/`: Get user profile

### Car Service
- `GET /api/cars/`: List all cars
- `GET /api/cars/{id}/`: Get details of a specific car
- `POST /api/cars/`: Add a new car
- `PUT /api/cars/{id}/`: Update car details
- `DELETE /api/cars/{id}/`: Delete a car

### Rental Service
- `GET /api/rentals/`: List all rentals
- `GET /api/rentals/{id}/`: Get details of a specific rental
- `POST /api/rentals/`: Create a new rental
- `PUT /api/rentals/{id}/`: Update rental details
- `DELETE /api/rentals/{id}/`: Cancel a rental

### Payment Service
- `GET /api/payments/`: List all payments
- `GET /api/payments/{id}/`: Get details of a specific payment
- `POST /api/payments/`: Create a new payment
- `PUT /api/payments/{id}/`: Update payment details
- `DELETE /api/payments/{id}/`: Delete a payment

### Testimonial Service
- `GET /api/testimonials/`: List all testimonials
- `GET /api/testimonials/{id}/`: Get details of a specific testimonial
- `POST /api/testimonials/`: Add a new testimonial
- `PUT /api/testimonials/{id}/`: Update testimonial
- `DELETE /api/testimonials/{id}/`: Delete a testimonial

### Notification Service
- `GET /api/notifications/`: List all notifications
- `GET /api/notifications/{id}/`: Get details of a specific notification
- `POST /api/notifications/`: Create a new notification

### Discount Service
- `GET /api/discounts/`: List all discounts
- `GET /api/discounts/{id}/`: Get details of a specific discount
- `POST /api/discounts/`: Create a new discount
- `PUT /api/discounts/{id}/`: Update discount
- `DELETE /api/discounts/{id}/`: Delete a discount

## Microservices
Each service is designed to handle a specific domain of the application:
- **User Service**: Handles user registration, login, profile management.
- **Car Service**: Manages car listings, availability.
- **Rental Service**: Handles rental bookings, updates.
- **Payment Service**: Processes payments, manages payment status.
- **Testimonial Service**: Manages user testimonials about cars.
- **Notification Service**: Sends notifications to users about rental status, payments.
- **Discount Service**: Manages discount codes, promotions.

## Database Schema
Here is the database schema for the application:

### users
- `id`: Integer (Primary Key)
- `username`: Varchar
- `email`: Varchar
- `password`: Varchar
- `first_name`: Varchar
- `last_name`: Varchar
- `phone_number`: Varchar
- `created_at`: Timestamp
- `updated_at`: Timestamp

### cars
- `id`: Integer (Primary Key)
- `make`: Varchar
- `model`: Varchar
- `year`: Integer
- `license_plate`: Varchar
- `daily_rate`: Decimal
- `status`: Varchar
- `created_at`: Timestamp
- `updated_at`: Timestamp

### rentals
- `id`: Integer (Primary Key)
- `user_id`: Integer (Foreign Key)
- `car_id`: Integer (Foreign Key)
- `start_date`: Date
- `end_date`: Date
- `total_amount`: Decimal
- `status`: Varchar
- `created_at`: Timestamp
- `updated_at`: Timestamp

### payments
- `id`: Integer (Primary Key)
- `rental_id`: Integer (Foreign Key)
- `amount`: Decimal
- `payment_date`: Timestamp
- `payment_method`: Varchar
- `status`: Varchar
- `created_at`: Timestamp
- `updated_at`: Timestamp

### testimonials
- `id`: Integer (Primary Key)
- `user_id`: Integer (Foreign Key)
- `rental_id`: Integer (Foreign Key)
- `rating`: Integer
- `comment`: Text
- `created_at`: Timestamp
- `updated_at`: Timestamp

### notifications
- `id`: Integer (Primary Key)
- `user_id`: Integer (Foreign Key)
- `message`: Text
- `sent_at`: Timestamp
- `status`: Varchar

### discounts
- `id`: Integer (Primary Key)
- `code`: Varchar
- `description`: Text
- `percentage`: Decimal
- `valid_from`: Date
- `valid_to`: Date
- `created_at`: Timestamp
- `updated_at`: Timestamp
- `type`: Varchar

### user_discounts
- `user_id`: Integer (Foreign Key)
- `discount_id`: Integer (Foreign Key)
- `assigned_at`: Timestamp

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
