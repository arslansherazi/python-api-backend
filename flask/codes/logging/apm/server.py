from api import division
from app import app, set_logging_handlers


if __name__ == '__main__':
    set_logging_handlers()
    app.run()
