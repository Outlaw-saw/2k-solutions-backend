#!/bin/bash
set -e

echo "Running database migrations..."
flask db upgrade 2>/dev/null || python -c "
from app import create_app
from config import Config
app = create_app(Config)
with app.app_context():
    from app.extensions import db
    db.create_all()
    print('Tables created')
" || true

echo "Starting gunicorn..."
exec gunicorn run:app --bind 0.0.0.0:$PORT --workers 4 --timeout 120 --log-level info
