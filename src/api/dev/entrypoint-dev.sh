# Exit immediately if a command fails
set -e

# We execute migrations.
core makemigrations --noinput
core migrate --noinput

# Execute the command passed as an argument.
exec "$@"
