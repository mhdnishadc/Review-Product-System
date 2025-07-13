# Review Product System API

This API provides endpoints for user registration, authentication, product management, and product reviews with role-based access control.

## Authentication

- **Session-based authentication** (login sets a session cookie).
- Users have roles: `admin` (manage products) and `user` (can review).

---

## Endpoints

### User

#### Register
- **POST** `/register/`
- **Body:**  
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string",
    "role": "user" // or "admin" (optional, defaults to "user")
  }
  ```
- **Response:** User details

#### Login
- **POST** `/login/`
- **Body:**  
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response:**  
  ```json
  {
    "message": "Login successful",
    "username": "string",
    "role": "string"
  }
  ```
- **Note:** Sets a session cookie for authentication.

#### Logout
- **POST** `/logout/`
- **Response:**  
  ```json
  {
    "message": "Logout successful"
  }
  ```

---

### Products

#### Create Product (Admin only)
- **POST** `/products/create/`
- **Body:**  
  ```json
  {
    "name": "string",
    "description": "string",
    "price": 0.0
  }
  ```
- **Authentication:** Admin session required

#### Retrieve, Update, Delete Product (by ID)
- **GET** `/products/<id>/`
- **PUT/PATCH/DELETE** `/products/<id>/` (Admin only)
- **Authentication:**  
  - GET: Public  
  - PUT/PATCH/DELETE: Admin session required

#### List Products
- **GET** `/products-list/`
- **Response:** List of products with average rating and reviews

---

### Reviews

#### Create Review (User only)
- **POST** `/reviews/create/`
- **Body:**  
  ```json
  {
    "product": <product_id>,
    "rating": 1-5,
    "feedback": "string"
  }
  ```
- **Authentication:** User session required

---

## Notes

- **Session Cookie:**  
  Authenticate via `/login/` and use the returned session cookie for all protected endpoints.
- **Role-based Access:**  
  - Only admins can create, update, or delete products.
  - Only authenticated users with role `user` can submit reviews.
  - Each user can review a product only once.
