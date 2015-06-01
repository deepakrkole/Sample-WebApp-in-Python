from flask import Flask
from flask import render_template
import os


app = Flask(__name__)
path='C:\Users\DEEPAK\Desktop\Latest_Resumes'    # Path to the folder whose contents needs to be displayed

def directory():
    message=[]
    for root, dirl, files in os.walk(path):     #Loop 1: For Root-Directory with the help of os.walk() method of os module
        dirlist = root
        dirlist=dirlist.split("\\")[-1]
        message.append(dirlist)
    for fname in files:                         #Loop 2:  For Files under the Root-Directory
        filelist = fname
        filelist=filelist.split("\\")[-1]
        message.append(filelist)
        print message
    #return message
    return message

def filesStr(directory):                        #Function 2: function for displaying sub directory contents through parameter passing
    directoryStr=[]
    for root, dirl, files in os.walk(directory): #Loop 1: For NonRoot-Directory with the help of os.walk() method of os module
        dirlist = root
        dirlist=dirlist.split("\\")[-1]
        directoryStr.append(dirlist)
    for fname in files:                           #Loop 2:  For Files under the NonRoot-Sub-Directory, if exists
        filelist = fname
        filelist=filelist.split("\\")[-1]
        directoryStr.append(filelist)
    return directoryStr

@app.route('/')                                 # end Point for inital page load, which will generate Get reguest
def hello_world():
    return render_template('directory.html', directories = directory())  # Send directory structure with html name


@app.route('/<directory>')          # end Point for directoris, sub-directories through end-point
def hello(directory):
    print directory
    #direct=request.args.
    directory=path+'\\'+directory
    return render_template('Files.html', directories = filesStr(directory))

if __name__ == '__main__':
    app.run()
