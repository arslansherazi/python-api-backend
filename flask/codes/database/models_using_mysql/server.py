from controller import *  # To use views, it should be included here
from app import *


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)