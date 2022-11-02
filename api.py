from flask import Flask, request, jsonify
import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import requests
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('brown')

app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def returntext():
    str1=""" """
    def search(pat, txt):
        M = len(pat)
        N = len(txt)
        # A loop to slide pat[] one by one */
        for i in range(N - M + 1):
            j = 0
            # For current index i, check
            # # for pattern match */
            while(j < M):
                if (txt[i + j] != pat[j]):
                    break
                j += 1
 
            if (j == M):
                return i

    
    str1 =str(request.args['query'])
    final2=[]
    final=""
    str1=str1.split("<br>")
    for i in str1:
        if "*" not in i:
            final2.append(i)
    #lowercase
    for i in final2:
        final+=i
    final=final.lower()
    #removing numbers
    final = re.sub(r'\d+', '', final)
    print(final)
    #removing punctuation
    nfinal=""
    for i in final:
        nfinal+=i
    translator = nfinal.maketrans('', '', string.punctuation)
    final=nfinal.translate(translator)
    #removing stopwords
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(final)
    final = [word for word in word_tokens if word not in stop_words]
    final1=" "
    final1=final1.join(final)
    
    #lemmatizing string
    lemmatizer = WordNetLemmatizer()
    word_tokens = word_tokenize(final1)
    # provide context i.e. part-of-speech
    final= [lemmatizer.lemmatize(word, pos ='v') for word in word_tokens]
    newlemma=""
    for i in final:
        if len(i) > 4:
            newlemma+=i
    final=search("paracetamol",newlemma)
    if final>0:
        return "paracetamol"
    else:
        return "not found"
   
@app.route('/search',methods=['GET'])
def returnt():
    str2=" "
    str2=str(request.args['query'])
    response= requests.get(url="https://en.wikipedia.org/wiki/"+str2,)
    soup = BeautifulSoup(response.text, 'html.parser')
    para=[]
    for paragraph in soup.select('p'):
        para.append(paragraph.getText())
    newpara=[]
    for i in para:
        newpara.append(i.replace("\n",""))
    paran=[]
    for i in newpara:
        if i !="":
            paran.append(i)
    
    return paran[0]

if __name__ =="__main__":
    app.run()