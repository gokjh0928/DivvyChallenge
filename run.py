from app import create_app, db
from app.blueprints.api.models import DivvyTable

app = create_app()


@app.shell_context_processor
def make_context():
    return {
        'db': db,
        'DivvyTable': DivvyTable
    }