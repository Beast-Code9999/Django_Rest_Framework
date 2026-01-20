# Django REST Framework - Tutorial 3: Class-Based Views

## Overview
Refactored function-based views to class-based views, then progressively simplified using mixins and generic views.

## Key Concepts Learned

### 1. APIView (Basic Class-Based View)
- Inherit from `APIView`
- Define methods: `get()`, `post()`, `put()`, `delete()`
- Better separation of HTTP methods
```python
class SnippetList(APIView):
    def get(self, request, format=None):
        # Handle GET
    def post(self, request, format=None):
        # Handle POST
```

### 2. Mixins (Reusable Behavior)
- Combine multiple mixins for common operations
- `ListModelMixin` - list all objects
- `CreateModelMixin` - create object
- `RetrieveModelMixin` - get single object
- `UpdateModelMixin` - update object
- `DestroyModelMixin` - delete object
```python
class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
```

### 3. Generic Views (Most Concise)
- Pre-built views combining common mixins
- `ListCreateAPIView` - list + create
- `RetrieveUpdateDestroyAPIView` - get + update + delete
```python
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
```

## Evolution of Code

### Stage 1: Function-Based (Tutorial 2)
```python
@api_view(["GET", "POST"])
def snippet_list(request):
    if request.method == "GET":
        # 5+ lines of code
    elif request.method == "POST":
        # 5+ lines of code
```

### Stage 2: Class-Based (APIView)
```python
class SnippetList(APIView):
    def get(self, request, format=None):
        # GET logic
    def post(self, request, format=None):
        # POST logic
```

### Stage 3: Mixins
```python
class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
```

### Stage 4: Generic Views (Final)
```python
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
```

## URL Changes
Use `.as_view()` for class-based views:
```python
urlpatterns = [
    path("snippets/", views.SnippetList.as_view()),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view()),
]
```

## Generic Views Used
- `ListCreateAPIView` - GET (list) + POST (create)
- `RetrieveUpdateDestroyAPIView` - GET (retrieve) + PUT (update) + DELETE (destroy)

## Key Takeaways
- Class-based views = better code organization
- Mixins = reusable behavior
- Generic views = maximum code reuse
- Just 2 lines per view for full CRUD!
- DRY principle in action