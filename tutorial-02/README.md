# Django REST Framework - Tutorial 2: Requests and Responses

## Overview
Refactored views to use DRF's Request/Response objects and decorators for better API functionality.

## Key Concepts Learned

### 1. Response Object
- Replaces `JsonResponse`
- Handles content negotiation automatically
- Returns correct format based on client request
```python
return Response(data)  # Auto-renders to JSON, HTML, etc.
```

### 2. Status Codes
- Use named constants instead of numbers
- More readable and maintainable
```python
status.HTTP_201_CREATED  # Instead of 201
status.HTTP_400_BAD_REQUEST  # Instead of 400
status.HTTP_404_NOT_FOUND  # Instead of 404
status.HTTP_204_NO_CONTENT  # Instead of 204
```

### 3. @api_view Decorator
- Wraps function-based views
- Provides Request/Response objects
- Handles 405 Method Not Allowed automatically
- Handles ParseError exceptions
```python
@api_view(["GET", "POST"])
def snippet_list(request):
    # No more @csrf_exempt needed!
```

### 4. Request Object
- `request.data` handles JSON, form data, and other formats
- Replaces `JSONParser().parse(request)`
- Works with any content type

### 5. Format Suffixes
- Add `.json`, `.api` to URLs for specific formats
- Use `format_suffix_patterns()` to enable
```python
urlpatterns = format_suffix_patterns(urlpatterns)
```

### 6. Content Negotiation
- API responds based on `Accept` header
- Can request JSON, HTML, or other formats
- Browsable API renders HTML automatically in browser

## Code Changes

### Before (Tutorial 1)
```python
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def snippet_list(request):
    if request.method == "GET":
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        return JsonResponse(serializer.data, status=201)
```

### After (Tutorial 2)
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET", "POST"])
def snippet_list(request):
    if request.method == "GET":
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

## Improvements Made
- ✅ No more `@csrf_exempt`
- ✅ Named status codes (readable)
- ✅ Automatic content negotiation
- ✅ Better error handling
- ✅ Browsable API in browser
- ✅ Format suffixes support

## Testing Different Formats

**Request JSON:**
```bash
http http://127.0.0.1:8000/snippets/ Accept:application/json
```

**Request HTML:**
```bash
http http://127.0.0.1:8000/snippets/ Accept:text/html
```

**Using format suffix:**
```bash
http http://127.0.0.1:8000/snippets.json
http http://127.0.0.1:8000/snippets.api
```

**POST with different formats:**
```bash
# Form data
http --form POST http://127.0.0.1:8000/snippets/ code="print(123)"

# JSON
http --json POST http://127.0.0.1:8000/snippets/ code="print(456)"
```

## Browsable API
- Open `http://127.0.0.1:8000/snippets/` in browser
- Get fully interactive HTML interface
- Can test API directly in browser
- Huge usability win for developers

## Key Takeaways
- `Response` > `JsonResponse` (handles multiple formats)
- `@api_view` > `@csrf_exempt` (better DRF integration)
- `request.data` > `JSONParser()` (format-agnostic)
- Named status codes > numbers (readable)
- Content negotiation is automatic