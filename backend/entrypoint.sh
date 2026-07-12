#!/bin/bash
set -e

echo "=== 2K Solutions Backend Entrypoint ==="
echo "Python version: $(python --version)"
echo "PORT: $PORT"

echo "--- Installing dependencies ---"
pip install --quiet --no-cache-dir -r requirements.txt 2>&1

echo "--- Creating tables ---"
python -c "
from app import create_app
from config import Config
app = create_app(Config)
with app.app_context():
    from app.extensions import db
    db.create_all()
    print('Tables created successfully')
" 2>&1

echo "--- Starting gunicorn on port $PORT ---"
exec gunicorn run:app --bind 0.0.0.0:$PORT --workers 4 --timeout 120 --log-level debug --access-logfile -
