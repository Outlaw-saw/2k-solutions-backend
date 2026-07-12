# 2K Solutions — Backend API

Production-ready REST API for the 2K Solutions ed-tech platform.

Built with **Python 3.13**, **Flask**, and **PostgreSQL**.

## Tech Stack

- **Framework:** Flask 3.1
- **ORM:** SQLAlchemy 2.x
- **Migrations:** Flask-Migrate (Alembic)
- **Auth:** JWT (Flask-JWT-Extended) with bcrypt password hashing
- **Validation:** Marshmallow
- **API Docs:** Swagger (flasgger)
- **Rate Limiting:** Flask-Limiter
- **CORS:** Flask-CORS
- **Server:** Gunicorn
- **Testing:** pytest
- **Deployment:** Docker

## Project Structure

```
backend/
├── run.py                     # Entry point
├── config.py                  # Configuration
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── gunicorn.conf.py
├── app/
│   ├── __init__.py            # App factory
│   ├── extensions.py          # db, migrate, jwt
│   ├── constants.py           # Enums
│   ├── models/                # SQLAlchemy models
│   ├── schemas/               # Marshmallow validation schemas
│   ├── repositories/          # Data access layer
│   ├── services/              # Business logic layer
│   ├── api/v1/                # Route blueprints
│   ├── middleware/             # Auth, error handlers, logging
│   ├── utils/                 # Helpers, pagination, errors
│   └── seed/seed_data.py      # Database seeder
├── migrations/                # Alembic migrations
└── tests/                     # pytest tests
```

## Quick Start

### Prerequisites

- Python 3.13+
- PostgreSQL 16+

### Setup

```bash
# Clone and enter backend directory
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
copy .env.example .env
# Edit .env with your PostgreSQL credentials

# Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Seed data
python -c "from app.seed.seed_data import run_seed; run_seed()"

# Run development server
python run.py
```

### Docker

```bash
docker-compose up --build
```

The API will be available at `http://localhost:5000`.

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register` | Create account |
| POST | `/api/v1/auth/login` | Sign in |
| POST | `/api/v1/auth/refresh` | Refresh JWT |
| POST | `/api/v1/auth/logout` | Logout |
| GET | `/api/v1/auth/me` | Current user |

### Courses
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/courses` | List courses (paginated) |
| GET | `/api/v1/courses/active` | List active courses |
| GET | `/api/v1/courses/:slug` | Get course with modules |
| POST | `/api/v1/courses` | Create course (admin) |
| PATCH | `/api/v1/courses/:slug` | Update course (admin) |

### Enrollments (authenticated)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/enrollments` | Enroll in course |
| GET | `/api/v1/enrollments` | User's enrollments |
| PATCH | `/api/v1/enrollments/:id` | Update enrollment |

### Contact
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/contact` | Submit contact form |
| GET | `/api/v1/contact` | List messages (admin) |
| PATCH | `/api/v1/contact/:id/read` | Mark as read (admin) |

### Content (public GET, admin for mutations)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/services` | List services |
| GET | `/api/v1/testimonials` | List testimonials |
| GET | `/api/v1/faqs` | List FAQs |
| GET | `/api/v1/technologies` | List technologies |
| GET | `/api/v1/milestones` | List milestones |
| GET | `/api/v1/steps` | List steps |
| GET | `/api/v1/differentiators` | List differentiators |

### Stats & Site
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/stats` | Dashboard stats |
| GET | `/api/v1/site` | Site settings |
| PATCH | `/api/v1/site` | Update site settings (admin) |

### Users (admin)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/users` | List users |
| GET | `/api/v1/users/:id` | Get user |
| PATCH | `/api/v1/users/:id` | Update user |

## Response Format

### Success
```json
{
  "success": true,
  "message": "",
  "data": {},
  "meta": { "page": 1, "per_page": 20, "total": 100 }
}
```

### Error
```json
{
  "success": false,
  "message": "Error description",
  "errors": [],
  "status": 400
}
```

## Default Admin Credentials

After seeding:
- Email: `admin@2ksolutions.com`
- Password: `admin123`

## Running Tests

```bash
pytest
# With coverage:
pytest --cov=app tests/
```
