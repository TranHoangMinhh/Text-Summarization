from flask import Flask, request,   render_template, url_for
from gensim.summarization.summarizer import summarize
from underthesea import sent_tokenize

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("base.html")

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['textarea_des']
    sentences = sent_tokenize(text)
    sum = ""
    if(len(sentences) <= 1):
        sum = "Need more than 1 sentence"
    else:
        sum = summarize(text, ratio = 0.2)      #summarize function can be altered to match user's intent
    if(sum == None or sum == ''):
        sum = "Need longer text"
    return render_template('base.html', first_input = text, final_summary = sum)

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    print("upload")
    fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", ""," Text files(*.txt)", options=options)
    f = open(fileName, "r", encoding = "utf-8").read()
    return render_template('base.html', first_input = f, final_summary = "")

if __name__ == "__main__":
    app.run(debug = True)