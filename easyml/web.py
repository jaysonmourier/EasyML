from flask import Flask, render_template, request

from .context import Context

class WebRenderer:
    def __init__(self, context: Context):
        self.app = Flask(__name__)
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/hello', 'hello', self.hello)
        self.context = context

    def index(self):
        return render_template('index.html', score=self.context.model.model.score(self.context.dataset.Xtest, self.context.dataset.Ytest))

    def hello(self):
        print("Hello")
        return ''

    def run(self):
        self.app.run(debug=True)