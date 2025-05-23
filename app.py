
from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    language = request.form['language']
    code = request.form['code']
    output = ''

    try:
        if language == 'python':
            with open('temp.py', 'w') as f:
                f.write(code)
            result = subprocess.run(['python', 'temp.py'], capture_output=True, text=True, timeout=5)
            output = result.stdout + result.stderr

        elif language == 'c':
            with open('temp.c', 'w') as f:
                f.write(code)
            compile = subprocess.run(['gcc', 'temp.c', '-o', 'temp.exe'], capture_output=True, text=True)
            if compile.returncode == 0:
                result = subprocess.run(['temp.exe'], capture_output=True, text=True, timeout=5)
                output = result.stdout + result.stderr
            else:
                output = compile.stderr

        elif language == 'java':
            with open('Main.java', 'w') as f:
                f.write(code)
            compile = subprocess.run(['javac', 'Main.java'], capture_output=True, text=True)
            if compile.returncode == 0:
                result = subprocess.run(['java', 'Main'], capture_output=True, text=True, timeout=5)
                output = result.stdout + result.stderr
            else:
                output = compile.stderr
        else:
            output = 'Unsupported language'

    except Exception as e:
        output = 'Error: ' + str(e)

    return output

if __name__ == '__main__':
    app.run(debug=True)
