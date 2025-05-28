In Go, your project’s directory tree directly maps to packages and import paths.  Here’s how it all hangs together when you have multiple top-level folders (e.g. `cmd/`, `internal/`, `someother/`), plus sub-directories under `internal/`:

---

## 1. `go.mod` defines your module path

At the root you have:

```text
myapp/
└── go.mod
```

Inside `go.mod` you’ll declare:

```go
module github.com/yourname/myapp

go 1.20
```

All import paths under this module start with `github.com/yourname/myapp`.

---

## 2. Top-level “command” packages (`cmd/`)

Every subdirectory under `cmd/` is its own `package main` and compiles to a separate binary:

```
myapp/
├── cmd/
│   ├── server/
│   │   └── main.go      ← package main, imports your shared code
│   └── worker/
│       └── main.go      ← package main, imports your shared code
```

**Example: `cmd/server/main.go`**

```go
package main

import "github.com/yourname/myapp/internal/server"

func main() {
    server.Start()
}
```

**Build:**

```bash
go build -o bin/server ./cmd/server
```

---

## 3. Shared/internal packages (`internal/`)

Code under `internal/` can be imported **only** by code in the same module (not by external modules). You can further organize `internal/` into sub-packages:

```
myapp/
└── internal/
    ├── server/
    │   └── server.go     ← package server
    ├── worker/
    │   └── worker.go     ← package worker
    └── db/
        └── db.go         ← package db
```

* **`internal/server/server.go`**

  ```go
  package server

  import "github.com/yourname/myapp/internal/db"

  func Start() {
      db.Connect()
      // ...
  }
  ```

* **`internal/db/db.go`**

  ```go
  package db

  func Connect() {
      // open connections, migrations, etc.
  }
  ```

To import from `cmd/worker/main.go`:

```go
package main

import (
    "github.com/yourname/myapp/internal/worker"
    "github.com/yourname/myapp/internal/db"
)

func main() {
    db.Connect()
    worker.Run()
}
```

---

## 4. Other top-level packages (`someother/`)

Any other directory under your module (e.g. for reusable “public” packages) is imported by its path:

```
myapp/
├── someother/
│   ├── utils.go        ← package someother
│   └── helper.go
```

* **`someother/utils.go`**

  ```go
  package someother

  func UsefulFunc() { /* … */ }
  ```

Then anywhere in your module:

```go
import "github.com/yourname/myapp/someother"

func Foo() {
    someother.UsefulFunc()
}
```

---

## 5. Rules of thumb

1. **One package per directory.**
2. **Directory name = import path element**, so keep them short and descriptive.
3. **`package main` only** for entry-point dirs (under `cmd/`, or a top-level `main.go` if you prefer).
4. **Internal code under `internal/`** is hidden from external consumers.
5. **Public packages** (for reuse inside or outside your module) live outside `internal/` (e.g. in `pkg/` or `someother/`).

---

### Example full tree

```
myapp/
├── go.mod
├── cmd/
│   ├── server/
│   │   └── main.go   ← package main
│   └── worker/
│       └── main.go   ← package main
├── internal/
│   ├── server/
│   │   └── server.go ← package server
│   ├── worker/
│   │   └── worker.go ← package worker
│   └── db/
│       └── db.go     ← package db
└── pkg/
    └── logger.go     ← package pkg (or better: `logger`)
```

* Build your binaries with

  ```bash
  go build -o bin/server ./cmd/server
  go build -o bin/worker ./cmd/worker
  ```
* Shared code is imported via its full path, e.g.
  `import "github.com/yourname/myapp/internal/db"`

That’s the canonical Go project layout: clear separation of entry points, internal (private) functionality, and any public/shared libraries.
