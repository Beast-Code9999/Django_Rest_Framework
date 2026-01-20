# Django REST Framework - Quickstart Tutorial

## Overview
Built a simple API for viewing and editing users and groups using Django REST Framework.

## Key Concepts Learned

### 1. Serializers
- Convert Django models to/from JSON
- `HyperlinkedModelSerializer` auto-generates fields from models
- Define which model fields to expose in API

### 2. ViewSets
- Handle all CRUD operations in one class
- `ModelViewSet` provides: list, create, retrieve, update, delete
- Configure with: `queryset`, `serializer_class`, `permission_classes`

### 3. Routers
- Auto-generate URL patterns from ViewSets
- `DefaultRouter()` creates RESTful URLs automatically
- `router.register()` maps ViewSets to URL paths

### 4. Permissions
- Control who can access API endpoints
- `IsAuthenticated` requires user login
- Set via `permission_classes` in ViewSet

### 5. API Flow
```
Model → Serializer → ViewSet → Router → URLs
```

## Project Structure
```
tutorial/
├── manage.py
├── tutorial/
│   ├── settings.py
│   ├── urls.py
│   └── quickstart/
│       ├── serializers.py  # Data formatting
│       ├── views.py        # API logic
│       └── models.py       # Database tables
└── env/
```

## Setup Commands
```bash
# Create virtual environment
python -m venv env
env\Scripts\activate

# Install dependencies
pip install djangorestframework

# Database setup
python manage.py migrate
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## API Endpoints Created
- `GET/POST /users/` - List/create users
- `GET/PUT/DELETE /users/{id}/` - Retrieve/update/delete user
- `GET/POST /groups/` - List/create groups
- `GET/PUT/DELETE /groups/{id}/` - Retrieve/update/delete group

## Testing the API
- **Browser**: http://127.0.0.1:8000/users/
- **curl**: `curl -u admin http://127.0.0.1:8000/users/`
- Must login to access (protected by `IsAuthenticated`)

## Settings Configured
```python
INSTALLED_APPS = ['rest_framework']

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}
```