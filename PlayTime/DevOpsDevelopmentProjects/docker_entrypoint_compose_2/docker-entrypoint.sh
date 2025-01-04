#!/bin/sh

# Check if the database is ready (example for PostgreSQL)
# until PGPASSWORD=$POSTGRES_PASSWORD psql -h $POSTGRES_HOST -U $POSTGRES_USER -c '\q'; do
#   echo "Postgres is unavailable - sleeping..."
#   sleep 1
# done
# echo "Postgres is up."

# This is just an example and can be commented out if not needed.

# Run migrations (if you're using something like Flask-Migrate)
# flask db upgrade

# Finally, run the Flask app
exec flask run --host=0.0.0.0
