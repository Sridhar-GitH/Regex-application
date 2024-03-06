from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def match():
    if request.method == 'POST':
        regex = request.form['regex']
        string = request.form['string']
        count = 0
        spans = []

        for match in re.finditer(r"{}".format(regex), string):
            count += 1
            match_details = "Match \"{}\" at index: {}".format(match.group(), match.start())
            spans.append(match_details)

        if count > 0:
            return render_template("temp.html", count=count, spans=spans)
        else:
            return render_template("temp.html", count=-1)
    else:
        return render_template("temp.html", count=0)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
