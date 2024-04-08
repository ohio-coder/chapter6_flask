from app import app

@app.route('/')
def index():
    return 'Hello,world this is me'