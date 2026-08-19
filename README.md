# FastAPI Authentication System

A secure and modular authentication system built with **FastAPI**, implementing multiple authentication mechanisms including **JWT Authentication, OAuth2, and Session Key Authentication**.

The project follows a controller-based architecture and includes protected routes, authentication utilities, password security, and logging.

## 🚀 Features

* JWT-based authentication
* OAuth2 authentication
* Session Key authentication
* Controller-based architecture
* Protected API routes
* Password hashing and verification
* Authentication and security logging
* Modular authentication structure
* FastAPI automatic Swagger documentation
* Environment-based configuration support

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **JWT**
* **OAuth2**
* **Passlib**
* **Uvicorn**
* **Python Logging**

## 📁 Project Structure

```text
Fast_Api_With_Contoller/
│
├── fastapi_security/
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── jwt_auth.py
│   │   ├── oauth_auth.py
│   │   └── secret_key_auth.py
│   │
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── jwt_controller.py
│   │   ├── oauth_controller.py
│   │   └── secret_key_controller.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── logger.py
│   │
│   ├── main.py
│   └── .gitignore
│
├── requirements.txt
└── README.md
```

## 🔐 Authentication Methods

### 1. JWT Authentication

JSON Web Tokens are used to authenticate users after successful login.

```text
User Login
    ↓
Verify Credentials
    ↓
Generate JWT
    ↓
Return Access Token
    ↓
Client Sends Token
    ↓
Verify JWT
    ↓
Access Protected Route
```

JWT provides a stateless authentication mechanism where the server validates the token instead of maintaining authentication state for every request.

### 2. OAuth2 Authentication

OAuth2 is used to implement a standard authorization flow.

```text
Client
   ↓
Login
   ↓
OAuth2 Authentication
   ↓
Access Token
   ↓
Protected API
```

FastAPI's OAuth2 security utilities are used to protect authentication-dependent endpoints.

### 3. Session Key Authentication

The project also demonstrates session-key-based authentication.

```text
User Login
    ↓
Validate Credentials
    ↓
Generate Session Key
    ↓
Store/Validate Session
    ↓
Client Sends Session Key
    ↓
Protected Route
```

## 🏗️ Controller Architecture

Authentication logic is separated into dedicated controllers:

```text
controllers/
│
├── jwt_controller.py
├── oauth_controller.py
└── secret_key_controller.py
```

This keeps authentication logic organized and makes the application easier to maintain and extend.

## 🛡️ Protected Routes

Protected routes require valid authentication before allowing access.

```text
Request
   ↓
Authentication Check
   ↓
Valid Token/Session?
   ├── Yes → Allow Access
   └── No  → Unauthorized
```

This prevents unauthorized users from accessing protected API resources.

## 📝 Logging System

The project includes a logging utility for tracking authentication-related activities.

Examples of events that can be logged:

* Login attempts
* Successful authentication
* Failed authentication
* Unauthorized access
* Security-related events

Example:

```text
INFO | Login attempt for user: username
INFO | Login successful for user: username
WARNING | Unauthorized access attempt
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sanskar-novadule/fastapi-authentication-system.git
```

### 2. Enter the Project Directory

```bash
cd fastapi-authentication-system
```

### 3. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

From the project root:

```bash
uvicorn fastapi_security.main:app --reload
```

The API will start at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

You can use Swagger UI to test authentication, login endpoints, tokens, and protected routes.

## 🔄 Authentication Flow

The overall authentication process is:

```text
                    ┌──────────────┐
                    │     User     │
                    └──────┬───────┘
                           │
                           ↓
                    ┌──────────────┐
                    │    Login     │
                    └──────┬───────┘
                           │
                           ↓
                  ┌──────────────────┐
                  │ Verify Credentials│
                  └────────┬─────────┘
                           │
                           ↓
              ┌─────────────────────────┐
              │ Authentication Method   │
              ├─────────────────────────┤
              │ JWT                     │
              │ OAuth2                  │
              │ Session Key             │
              └────────────┬────────────┘
                           │
                           ↓
                   ┌──────────────┐
                   │ Access Token │
                   │ / Session Key│
                   └──────┬───────┘
                          │
                          ↓
                  ┌────────────────┐
                  │ Protected Route│
                  └───────┬────────┘
                          │
                          ↓
                  ┌────────────────┐
                  │ Validate Auth  │
                  └───────┬────────┘
                          │
                    ┌─────┴─────┐
                    ↓           ↓
                  Valid       Invalid
                    ↓           ↓
              Allow Access   401 Error
```

## 🔒 Security Best Practices

For production use:

* Store secrets in environment variables
* Never commit `.env` files
* Never expose JWT secret keys
* Never commit OAuth client secrets
* Use HTTPS in production
* Use strong secret keys
* Set appropriate token expiration times
* Validate and sanitize user input
* Monitor authentication logs
* Rotate compromised secrets immediately

## 📌 Example Environment Configuration

Create a `.env` file for sensitive configuration:

```env
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> Never commit your real `.env` file or secret values to GitHub.

## 🧪 Testing

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

Use Swagger UI to:

1. Test login
2. Generate authentication credentials
3. Authorize the API
4. Access protected routes
5. Test unauthorized requests
6. Check authentication logs

## 🎯 Project Objective

The main objective of this project is to understand and implement secure authentication in a FastAPI application using multiple authentication approaches.

The project demonstrates how to:

* Build authentication systems
* Generate and validate JWT tokens
* Implement OAuth2 security
* Manage session keys
* Protect API routes
* Separate authentication logic using controllers
* Implement security logging
* Structure a maintainable FastAPI project

## 🔮 Future Improvements

Possible future improvements include:

* PostgreSQL user database
* Refresh token implementation
* Token revocation
* Redis-based session management
* Role-based access control (RBAC)
* Email verification
* Password reset functionality
* Two-factor authentication (2FA)
* Rate limiting
* Automated tests
* Docker deployment

## 👨‍💻 Author

**Sanskar Ajmera**

GitHub: [Sanskar-novadule](https://github.com/Sanskar-novadule)

## 📄 License

This project is created for learning, development, and demonstration purposes.
