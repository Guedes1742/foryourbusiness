from flask import Flask, render_template, request, jsonify
import pyautogui
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run-process', methods=['POST'])
def run_process():
    process_name = request.json.get('process')
    if process_name == 'abrir_calculadora':
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('Calculadora')
        pyautogui.press('enter')
        return jsonify({"status": "Calculadora aberta com sucesso!"})
    return jsonify({"error": "Processo não reconhecido"}), 400


if __name__ == '__main__':
    app.run(debug=True)
