# Gas_utility_Task

## Overview
This is a Django-based web application designed to improve customer service management for a gas utility company. The system allows customers to submit service requests, track their status, and access their account information. Additionally, customer support representatives can manage and resolve service requests efficiently.

## Features
### For Customers:
- **Service Requests**: Customers can submit service requests online, specifying the type and details of the request, and attaching relevant files.
- **Request Tracking**: View the status, submission date, and resolution date of service requests.
- **Account Management**: Customers can view and update their account details.

### For Customer Support Representatives:
- **Request Management**: Support staff can view, update, and resolve customer requests.
- **Support Dashboard**: An interface to manage and track all ongoing service requests.

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript (Optional: React or Vue.js for a dynamic UI)
- **Database**: PostgreSQL / MySQL
- **Authentication**: Django authentication system
  
## Installation & Setup
### Prerequisites
- Python 3.x
- Django
- PostgreSQL / MySQL
- Virtual environment (venv)

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/gas-utility-service.git
   cd gas-utility-service
   ```
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up the database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the server**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/requests/` | GET | Retrieve all service requests |
| `/api/requests/` | POST | Create a new service request |
| `/api/requests/{id}/` | GET | Retrieve a specific request |
| `/api/requests/{id}/` | PUT | Update request details |
| `/api/requests/{id}/` | DELETE | Delete a service request |

## Bonus Points
- Structured Django application following best practices
- Modularized codebase using Django apps
- DRF for API development
- Docker support for easy deployment

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a pull request

## License
This project is licensed under the MIT License.

---
Feel free to modify the repository URL and project details before publishing it on GitHub.
