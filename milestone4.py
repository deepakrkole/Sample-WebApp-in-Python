from flask import Flask
from flask import render_template

def directory():
    message=[]
    for root, dirl, files in os.walk(path):
        dirlist = root
        dirlist=dirlist.split("\\")[-1]
        message.append(dirlist)
    for fname in files:
        filelist = fname
        filelist=filelist.split("\\")[-1]
        message.append(filelist)
        print message
    #return message
    return message

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('directory.html', directories = directory())

if __name__ == '__main__':
    app.run()
