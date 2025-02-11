# Use official Golang image as builder
FROM golang:latest AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy go.mod (but remove go.sum since it may not exist)
COPY go.mod ./

# Download dependencies (if any)
RUN go mod tidy

# Copy the rest of the application code
COPY . .

# Ensure correct architecture & compile the Go binary
RUN GOOS=linux GOARCH=amd64 go build -o main .

# Use a lightweight final image
FROM alpine:latest

# Set the working directory inside the container
WORKDIR /root/

# Copy the compiled binary from the builder stage
COPY --from=builder /app/main .

# Ensure the binary has execution permissions
RUN chmod +x main

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["./main"]
