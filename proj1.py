from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    html = '''  <div class="form-group">
                    <label for="usr">Name:</label>
                    <input type="text" class="form-control" id="usr">
                </div>
                <div class="form-group">
                    <label for="pwd">Password:</label>
                    <input type="password" class="form-control" id="pwd">
                </div> '''
    
    
    return (html)

if __name__ == "__main__":
    app.run()