#Example `docker-entrypoint.sh`:
# Suppose you have a Python web application that connects to a PostgreSQL database. Before starting, you want to wait until the database is ready. Here's a simplified entrypoint script:

#!/bin/bash
set -e  # Exit on any error

# Wait for the database to be ready
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -c '\q'; do
  echo "Postgres is unavailable - sleeping..."
  sleep 1
done

echo "Postgres is up - starting the app."

# Start the main application
exec "$@"
