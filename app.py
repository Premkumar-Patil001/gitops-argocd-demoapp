from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    version = os.environ.get('APP_VERSION', '1.0')
    return f'''
    <!DOCTYPE html>
    <html>
    <body style="font-family:sans-serif;text-align:center;padding:50px;background:#f0f4f8">
      <div style="background:white;padding:40px;border-radius:12px;max-width:500px;margin:auto;box-shadow:0 2px 8px rgba(0,0,0,0.1)">
        <h1 style="color:#2d3748">GitOps Demo App</h1>
        <h2 style="color:#48bb78">Version 1.0</h2>
        <p style="color:#718096">Deployed automatically by ArgoCD</p>
        <p style="color:#718096">No kubectl commands used in production</p>
        <hr>
        <p style="color:#a0aec0;font-size:12px">
          Change k8s/deployment.yaml in GitHub<br>
          ArgoCD syncs the cluster automatically
        </p>
      </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
