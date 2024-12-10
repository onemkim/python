Reference:
- Documentation: https://fastapi.tiangolo.com
- Source Code: https://github.com/fastapi/fastapi

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

The key features are:
- Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
- Fast to code: Increase the speed to develop features by about 200% to 300%. *
- Fewer bugs: Reduce about 40% of human (developer) induced errors. *
- Intuitive: Great editor support. Completion everywhere. Less time debugging.
- Easy: Designed to be easy to use and learn. Less time reading docs.
- Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- Robust: Get production-ready code. With automatic interactive documentation.
- Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

Command
``` sh
# Install
fastapi dev main.py

# Run main.py file
fastapi dev main.py
# The fastapi dev server should reload automatically.

```

## In the browser
### Check it
http://127.0.0.1:8000/items/5?q=somequery

### Interactive API docs
Now go to http://127.0.0.1:8000/docs

### Alternative API docs
And now, go to http://127.0.0.1:8000/redoc