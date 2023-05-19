from flask import Flask, render_template, request

from .context import Context

class WebRenderer:
    def __init__(self, context: Context):
        self.app = Flask(__name__)
        self.app.add_url_rule('/', 'index', self.index)
        self.context = context

    def index(self):
        models_result = {}
        for m in self.context.pool.models:
            models_result.update({
                "name": m.name, 
                "accuracy": m.score,
                "training_time": m.training_time
            })
        return render_template('index.html', results=models_result)

    def run(self):
        self.app.run(debug=False)