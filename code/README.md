# Project Code

## Run instructions

```bash
sudo apt-get install python3
pip install virtualenv
cd Environments
virtualenv deco-env
source ./deco-env/bin/activate
pip install -r ./requirments.txt
cd ..
python3 server.py
```

## Architecture

### Flask Server

### Python Object Oriented Backend

#### UML

[UML Diagram](https://raw.githubusercontent.com/FaizAther/GPR-Analytics/main/code/Design/gpr_uml.png)

#### Type anotations and checking

1. mypy (in the works)

#### Design Patterns

1. Singleton Pattern
2. Observer Pattern
3. Visitor Pattern (adapted)

### SQLite Persistence

1.  [SQL](https://github.com/FaizAther/GPR-Analytics/blob/main/code/Instution/Database/creation.sql)

## References

- [Flask docs](https://flask.palletsprojects.com/en/2.0.x/])
- [SQLAlchemy docs](https://docs-sqlalchemy.readthedocs.io/ko/latest/)
- [WebRTC](https://webrtc.org/)

## TODO

### webrtc

- <https://webrtc.org/>
- <https://github.com/webrtc/FirebaseRTC/tree/master/public>
- <https://www.youtube.com/watch?v=WmR9IMUD_CY>
- <https://www.youtube.com/watch?v=DvlyzDZDEq4>