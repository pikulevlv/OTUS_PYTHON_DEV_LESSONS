# from flask import request
# request.args.get()
# request.args.getlist()
from app import app

app.config.update(
    DEBUG=True,
)

if __name__ == '__main__':
    app.run(debug=True)