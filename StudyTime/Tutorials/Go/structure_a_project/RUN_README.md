## Go Project Structure & Setup Guide

A quick reference for initializing, organizing, and building a simple Go project with multiple binaries (`cmd/`) and shared code (`internal/`).

---

### 1. Create & Structure Your Project Directory

1. **Create a new project directory** and enter it:

   ```bash
   mkdir myapp && cd myapp
   ```
2. **Set up the folder layout**:

   ```
   myapp/
   ├── cmd/         ← entry-point binaries
   ├── internal/    ← shared/internal packages
   └── go.mod       ← module definition
   ```

---

### 2. Initialize Your Module

1. **Create a new project directory** and `cd` into it:

   ```bash
   mkdir myapp && cd myapp
   ```
2. **Initialize Go modules** with your module path (replace with your repo path):

   ```bash
   go mod init github.com/yourname/myapp
   ```
3. **Verify** `go.mod` was created:

   ```go
   module github.com/yourname/myapp

   go 1.24.3
   ```

---

### 2. Create Entry-Point Binaries (`cmd/`)

Each subdirectory under `cmd/` becomes its own `package main` and compiles to a separate binary.

```
myapp/
├── cmd/
│   ├── server/
│   │   └── main.go   ← binary: server
│   └── worker/
│       └── main.go   ← binary: worker
```

#### Example `cmd/server/main.go`

```go
package main

import (
    "log"
    "github.com/yourname/myapp/internal/server"
)

func main() {
    if err := server.Start(); err != nil {
        log.Fatalf("server failed: %v", err)
    }
}
```

#### Example `cmd/worker/main.go`

```go
package main

import (
    "log"
    "github.com/yourname/myapp/internal/db"
    "github.com/yourname/myapp/internal/worker"
)

func main() {
    if err := db.Connect(); err != nil {
        log.Fatalf("db connect: %v", err)
    }
    worker.Run()
}
```

---

### 3. Add Shared Code (`internal/`)

Code under `internal/` is private to your module. Organize into sub-packages by feature.

```
myapp/
└── internal/
    ├── db/
    │   └── db.go        ← package db
    ├── server/
    │   └── server.go    ← package server
    └── worker/
        └── worker.go    ← package worker
```

#### Example `internal/db/db.go`

```go
package db

import "database/sql"

// Connect opens and verifies a database connection.
func Connect() (*sql.DB, error) {
    // db, err := sql.Open(...)
    // if err != nil { return nil, err }
    // return db.Ping();
    return nil, nil
}
```

#### Example `internal/server/server.go`

```go
package server

import (
    "net/http"
    "github.com/yourname/myapp/internal/db"
)

// Start launches the HTTP server.
func Start() error {
    // initialize DB
    if _, err := db.Connect(); err != nil {
        return err
    }
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        w.Write([]byte("Hello, world!"))
    })
    // listen on port 8080
    return http.ListenAndServe(":8080", nil)
}
```

#### Example `internal/worker/worker.go`

```go
package worker

import (
    "fmt"
    "time"
)

// Run executes the worker loop.
func Run() {
    fmt.Println("Worker starting…")
    for i := 1; i <= 5; i++ {
        fmt.Printf("Processing task #%d...\n", i)
        time.Sleep(500 * time.Millisecond)
    }
    fmt.Println("Worker finished.")
}
```

---

### 4. Build Your Binaries

From your project root, run:

```bash
# Build server binary
go build -o bin/server ./cmd/server

# Build worker binary
go build -o bin/worker ./cmd/worker
```

Or to compile all commands at once:

```bash
go build ./cmd/...
```

---

### 5. Useful Commands

- **Tidy dependencies**:

```bash
go mod tidy
```
- **Run a single binary**:
```bash
go run ./cmd/server
```

- **Test all packages**:

```bash
go test ./...
```


---

### 6. Managing Dependencies

Go modules handle your project’s dependencies via **`go.mod`** and **`go.sum`**. When you import or update packages, use the following commands:

```bash
# Add or upgrade a dependency (use @version or @latest)
go get github.com/some/dependency@v1.2.3

go get github.com/another/dependency@latest

# Remove unused dependencies and tidy module files
go mod tidy

# List current dependencies and their versions
go list -m all

# Upgrade all direct dependencies to the latest patch/minor versions
# (x.y.* for semantic import versions)
go get -u ./...

# Pin a module to a specific version across your project
go get github.com/some/dependency@v1.4.0

```

- `go.mod` records your direct requirements and module path.
- `go.sum` locks checksums for all modules (direct and indirect) for reproducible builds.
- To vendor dependencies (store them in vendor/), run:
    `go mod vendor`
    `go build -mod=vendor ./...`

---

### 7. Best Practices

- **One package per directory**. Keep `package main` only in `cmd/` folders.
- **Use `internal/`** for code that shouldn’t be imported externally.
- **Use descriptive directory names** matching the package name.
- **Keep `go.mod` at the project root**.
- **Version control** all source code, then others can fetch via:

```bash
go get github.com/yourname/myapp@latest
```
