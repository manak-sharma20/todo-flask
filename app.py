from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
class todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)

    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(400),nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"


@app.route("/")
def hello_world():

    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)