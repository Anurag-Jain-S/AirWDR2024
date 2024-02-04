from flask import Flask, render_template, request, redirect, url_for
import os
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'ipynb'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Save the uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Execute the notebook
        run_notebook(file_path)

        # Redirect to the results page
        return redirect(url_for('show_results', filename=file.filename))

    return redirect(request.url)

@app.route('/results/<filename>')
def show_results(filename):
    return render_template('results.html', filename=filename)

def run_notebook(file_path):
    with open(file_path) as f:
        notebook_content = f.read()

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    notebook, _ = ep.preprocess(notebook_content, {})

    html_exporter = HTMLExporter()
    body, resources = html_exporter.from_notebook_node(notebook)

    # Save the results to an HTML file
    result_path = os.path.join(app.config['UPLOAD_FOLDER'], 'results', os.path.splitext(os.path.basename(file_path))[0] + '_result.html')
    with open(result_path, 'w') as f:
        f.write(body)

if __name__ == '__main__':
    app.run(debug=True)