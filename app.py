from flask import Flask, render_template, request
import os
import math

app = Flask(__name__, static_folder='static')

# prepare safe namespace exposing math functions/constants
_safe_math = {name: getattr(math, name) for name in dir(math) if not name.startswith('_')}
# include builtins we want
_safe_math.update({
    'pow': pow,
    'abs': abs,
    'round': round,
})

@app.route('/', methods=['GET','POST'])
def index():
    result = None
    expression = ''
    info = ''
    if request.method == 'POST':
        expression = request.form.get('expression', '') or ''
        # normalize common symbols
        expression = expression.replace('^', '**').replace('π', str(math.pi)).replace('π', str(math.pi))
        expression = expression.replace(',', '.')
        allowed_chars = '0123456789+-*/()., eEabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
        if all(c in allowed_chars for c in expression):
            try:
                result = eval(expression, {'__builtins__': None}, _safe_math)
            except Exception as e:
                result = 'Error'
                info = str(e)
        else:
            result = 'Invalid characters'
    return render_template('index.html', result=result, expression=expression, info=info)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
