# how to generate schema of fastapi endpoint's request body, I need to use them in github dast

To generate the **schema of a FastAPI endpoint's request body** (OpenAPI/Swagger schema), which can be used for tools like **GitHub DAST** (Dynamic Application Security Testing), you can extract or generate it using FastAPI’s built-in OpenAPI generation.

---

### ✅ Option 1: Use `app.openapi()` to extract schema programmatically

```python
from fastapi import FastAPI
import json

app = FastAPI()

# define your endpoints here...

# dump schema to file
with open("openapi_schema.json", "w") as f:
    json.dump(app.openapi(), f, indent=2)
```

> This file includes **all paths, request bodies, responses**, and can be used directly by DAST tools.

---

### ✅ Option 2: Extract specific endpoint's request schema

To extract just one endpoint's request body schema:

```python
schema = app.openapi()

# Example: Get schema for POST /items/
post_items_schema = schema["paths"]["/items/"]["post"]["requestBody"]["content"]["application/json"]["schema"]

print(json.dumps(post_items_schema, indent=2))
```

---

### ✅ Option 3: Use `pydantic` model directly (for isolated model)

If you just need the **request model schema**:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

print(Item.schema_json(indent=2))
```

---

### ✅ Use in GitHub DAST

- GitHub’s DAST tools (like CodeQL, or integrations with OWASP ZAP) typically accept an OpenAPI spec.
- Upload the `openapi_schema.json` you generated.
- This helps DAST tools **crawl and fuzz test your endpoints safely and intelligently**.

---

Would you like a GitHub Action that auto-generates this schema on every push or release?
