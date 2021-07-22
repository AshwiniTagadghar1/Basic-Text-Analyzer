from website import create_app
import os
from werkzeug.utils import secure_filename
from flask import request, flash, redirect, flash, url_for, render_template
import nltk

app = create_app()

@app.route('/upload')
def show():
   return render_template('upload.html')

@app.route('/uploader', methods = ['POST'])
def upload_file():
    f = request.files['file']
    if f.filename== '':             # if no file is submited, prompt user to upload a file 
        flash('No selected file')
        return redirect((url_for('show')))
    #f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))  #for saving file but no need to save for now
    content = f.read()                  #stores content of file in 'byte' stream format
    data = content.decode('utf-8')      #changes byte stream to string format
    res = []
    res.append(secure_filename(f.filename))     #res[0] filename
    if len(data) < 1024:
        size = len(data)                   # here result is in bytes
        size_in = 'B'
        res.append([size, size_in])
    elif round(len(data)/1024,2) < 0:
        size = round(len(data)/1024,2)    # here result is in Kilo-bytes
        size_in = 'KB'
        res.append([size, size_in])
    else:
        size = round(len(data)/(1024*1024),2) # here result is in Mega-bytes
        size_in = 'MB'
        res.append([size, size_in])         # access res[1][0] for size n res[1][1] for which type size

    #f_size = round(len(data)/(1024*1024),2) #len(data) - gives no. of bytes of entire data, dividing by 1024 gives in KB n another 1024 in MB3
    new_str = data.replace("\n"," ")       # just replacin newline with space for preprocessing file

    data = sorted(data.split(' '))       #first splits data wherever sapce is der, basically list of words and then sorts the data according to character
    fdist1 = nltk.FreqDist(data)
   
    len_data = len(data) 
    res.append(len_data)            #res[2] no. of words in file
    len_fdist1 = len(fdist1)
    res.append(len_fdist1)          #res[3] no. of unique words in file
    res.append(fdist1)              #res[4] is dictionary
    #flash("No. of words in text file:",len_data)
    #flash("No. of distinct words:",len_fdist1)
    #flash("Most frequent 25 words: \n",fdist1.most_common(25)) # can apply dictionary method here as well to display
    #fdist1.plot(25) #gives a plot 

    #for i,j in fdist1.items():         # a way to print dictionary, (key val pairs) (here word-count pairs)
     #     print(i,j)

    return render_template("output.html",res=res) 



if __name__ == '__main__':
    app.run(debug=True)
    