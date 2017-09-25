import os

from app import create_app

CONFIG_NAME = os.getenv('APP_CONFIG')
if CONFIG_NAME != 'development':
    app = create_app('production')
    if __name__ == '__main__':
        app.run(debug=True)
else :
    app = create_app(CONFIG_NAME)
    if __name__ == '__main__':
        app.run(host='localhost', port=9874)
