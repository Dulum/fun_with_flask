from flask import Flask, render_template
app = Flask(__name__)

# with open('home.html', 'r') as f:
#     html = f.read()

@app.route('/')
def home():
    return render_template("homeee.html")

if __name__ == '__main__':
    app.run()