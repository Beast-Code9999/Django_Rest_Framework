# Django REST Framework - Tutorial 1: Serialization

## Overview
Built a pastebin-style code snippet API with syntax highlighting. Learned how serialization works from the ground up.

## Key Concepts Learned

### 1. Models with Choices
- Use `get_all_lexers()` from Pygments to generate language choices
- `get_all_styles()` for syntax highlighting styles
- Create choice lists for dropdown fields

### 2. Serializers (Manual)
- Define fields explicitly with validation rules
- Implement `create()` method for creating new instances
- Implement `update()` method for modifying existing instances
- Similar to Django Forms but for JSON/API data

### 3. ModelSerializer (Shortcut)
- Auto-generates fields from model
- Automatic `create()` and `update()` implementations
- Much more concise than manual serializers

### 4. Serialization Process
```python
# Object → JSON
serializer = SnippetSerializer(snippet)
content = JSONRenderer().render(serializer.data)

# JSON → Object
data = JSONParser().parse(stream)
serializer = SnippetSerializer(data=data)
serializer.is_valid()
serializer.save()
```

### 5. Function-Based Views
- Manual CRUD operations with `@csrf_exempt`
- Handle GET, POST, PUT, DELETE manually
- Return `JsonResponse` with appropriate status codes

### 6. URL Routing
- Map URLs to views with `<int:pk>` for capturing IDs
- Include app URLs in main `urls.py`

## Project Structure
```
tutorial/
├── manage.py
├── snippets/
│   ├── models.py        # Snippet model
│   ├── serializers.py   # SnippetSerializer
│   ├── views.py         # snippet_list, snippet_detail
│   └── urls.py          # URL patterns
└── tutorial/
    └── settings.py
```

## Setup Commands
```bash
# Install dependencies
pip install django djangorestframework pygments

# Database setup
python manage.py makemigrations snippets
python manage.py migrate

# Run server
python manage.py runserver
```

## Model Created
```python
class Snippet(models.Model):
    created = DateTimeField(auto_now_add=True)
    title = CharField(max_length=100, blank=True)
    code = TextField()
    linenos = BooleanField(default=False)
    language = ChoiceField(choices=LANGUAGE_CHOICES)
    style = ChoiceField(choices=STYLE_CHOICES)
```

## API Endpoints
- `GET /snippets/` - List all snippets
- `POST /snippets/` - Create snippet
- `GET /snippets/{id}/` - Get specific snippet
- `PUT /snippets/{id}/` - Update snippet
- `DELETE /snippets/{id}/` - Delete snippet

## Testing Commands
```bash
# List all snippets
http GET http://127.0.0.1:8000/snippets/

# Get specific snippet
http GET http://127.0.0.1:8000/snippets/2/

# Create snippet
http POST http://127.0.0.1:8000/snippets/ code="print('test')"
```

## Key Learnings
- Serializers convert between Python objects and JSON
- `ModelSerializer` is shortcut for common patterns
- Manual views give full control but are verbose
- `@csrf_exempt` needed for POST without CSRF tokens (temporary solution)
- `many=True` flag for serializing querysets