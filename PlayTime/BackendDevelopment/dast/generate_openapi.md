OpenAPI (Swagger) schemas serve as a precise, machine-readable “contract” for your HTTP APIs. Their primary uses are:

* **Interactive Documentation**
  Expose a user-friendly UI (Swagger UI or ReDoc) so developers can explore endpoints, parameters and responses without reading code.

* **Client & Server Code Generation**
  Automatically generate type-safe client SDKs (in Python, TypeScript, Java, etc.) or server stubs, accelerating development and ensuring consistency.

* **Request/Response Validation**
  Validate incoming requests and outgoing responses against the schema to catch mismatches early and enforce data integrity.

* **API Testing & Mocking**
  Drive automated tests or spin up mock servers that mimic your real API’s behavior, enabling integration tests before the backend is complete.

* **Contract-First Design**
  Define your API surface before implementation, align frontend/backend teams around a shared specification, and prevent breaking changes through versioned schemas.

* **Tooling & Ecosystem Integration**
  Leverage API gateways, documentation portals, monitoring tools, and CI pipelines that consume OpenAPI specs for validation, rate-limiting or performance checks.

In short, OpenAPI schemas make your API self-documenting, discoverable, and safe to evolve.


In FastAPI, OpenAPI (formerly “Swagger”) schemas are generated for you automatically. You can also retrieve or customize the raw schema in code:

```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI(title="My API", version="1.0.0")

@app.get("/items/{item_id}", tags=["items"])
def read_item(item_id: int):
    return {"item_id": item_id}

# Optionally override or inspect the generated schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description="This is my custom OpenAPI schema",
        routes=app.routes,
    )
    # … you can mutate openapi_schema here …
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
```

* **Automatic endpoint**: FastAPI mounts the schema at `/openapi.json`
* **Interactive docs**: `/docs` (Swagger UI) and `/redoc` (ReDoc)

---

### Other frameworks with built-in schema support

* **Django REST Framework**

  ```python
  from rest_framework import serializers, viewsets, routers
  from django.urls import path, include
  from rest_framework.schemas import get_schema_view

  class ItemSerializer(serializers.Serializer):
      item_id = serializers.IntegerField()

  class ItemViewSet(viewsets.ViewSet):
      def retrieve(self, request, pk=None):
          return Response({"item_id": pk})

  router = routers.DefaultRouter()
  router.register(r'items', ItemViewSet, basename='item')

  schema_view = get_schema_view(title="My DRF API", version="1.0.0")

  urlpatterns = [
      path('schema/', schema_view),
      path('', include(router.urls)),
  ]
  ```

* **Flask-RESTX** (successor to Flask-RESTPlus)

  ```python
  from flask import Flask
  from flask_restx import Api, Resource, fields

  app = Flask(__name__)
  api = Api(app, version='1.0', title='My API', description='A simple API')

  item_model = api.model('Item', {
      'item_id': fields.Integer(required=True, description='The item identifier'),
  })

  @api.route('/items/<int:item_id>')
  class Item(Resource):
      @api.doc('get_item')
      @api.marshal_with(item_model)
      def get(self, item_id):
          return {'item_id': item_id}

  if __name__ == '__main__':
      app.run(debug=True)
  ```

  * Schema is available at `/swagger.json` or rendered via Swagger UI at `/`.

* **NestJS** (TypeScript)
  Nest bundles Swagger support via `@nestjs/swagger`:

  ```ts
  import { NestFactory } from '@nestjs/core';
  import { AppModule } from './app.module';
  import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';

  async function bootstrap() {
    const app = await NestFactory.create(AppModule);

    const config = new DocumentBuilder()
      .setTitle('My API')
      .setVersion('1.0')
      .build();
    const document = SwaggerModule.createDocument(app, config);
    SwaggerModule.setup('api-docs', app, document);

    await app.listen(3000);
  }
  bootstrap();
  ```

Each of these frameworks auto-generates an OpenAPI/Swagger schema and provides interactive documentation out of the box.
