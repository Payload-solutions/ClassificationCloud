from app import app 
from flask_script import Server, Manager


manager = Manager(app)
manager.add_command("runserver", Server(host='0.0.0.0', port=4000, use_debugger=True))

if __name__ == "__main__":
    manager.run()