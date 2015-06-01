from flask import Flask
from flask import render_template
import os


app = Flask(__name__)
path='C:\Users\DEEPAK\Desktop\Latest_Resumes'
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

def filesStr(directory):
    directoryStr=[]
    for root, dirl, files in os.walk(directory):
        dirlist = root
        dirlist=dirlist.split("\\")[-1]
        directoryStr.append(dirlist)
    for fname in files:
        filelist = fname
        filelist=filelist.split("\\")[-1]
        directoryStr.append(filelist)
    return directoryStr

@app.route('/')
def hello_world():
    return render_template('directory.html', directories = directory())


@app.route('/<directory>')
def hello(directory):
    print directory
    #direct=request.args.
    directory=path+'\\'+directory
    return render_template('Files.html', directories = filesStr(directory))

if __name__ == '__main__':
    app.run()
