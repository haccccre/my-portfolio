from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def home():
    return render_template('index.html')

app.run(host='0.0.0.0', port=5000)
