from flask import Flask
from flask_cors import CORS
from controllers.livro_controller import livro_bp
import os

app = Flask(__name__)
CORS(app)
app.register_blueprint(livro_bp)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
