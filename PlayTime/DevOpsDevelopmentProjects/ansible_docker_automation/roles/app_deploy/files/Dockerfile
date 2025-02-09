FROM golang:1.19
WORKDIR /app
COPY main.go .
RUN go build -o server main.go
CMD ["./server"]
EXPOSE 8080
