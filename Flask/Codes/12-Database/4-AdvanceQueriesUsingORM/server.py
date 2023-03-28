from app import app, db
from routing import api


if __name__ == '__main__':
    db.init_app(app)
    app.run()
