from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run-process', methods=['POST'])
def run_process():
  
  
    time.sleep(1)
    return jsonify({"status": "Calculadora aberta com sucesso!"})
  


if __name__ == '__main__':
    app.run(debug=True)



