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

    med=['acenextp', 'paracetamol', 'amoxicillin', 'vitamin d', 'ibuprofen', 'cetirizinehydrochloride', 'azithromycin', 'amlodipine besylate', 'albuterolsulfate', 'cyclobenzaprine hydrochloride', 'cephalexin', 'hydrochlorothiazide', 'lisinopril', 'amphetamine', 'dextroamphetamine', 'loratadine 10', 'amoxicillin-clavulanate potassium', 'folicacid', 'prednisone', 'benzonatate', 'gabapentin', 'zolpidemtartrate', 'sulfamethoxazole/trimethoprimds', 'methylprednisolone ', 'fluconazole', 'aspirin', 'atorvastatincalcium', 'ferroussulfate', 'cyanocobalamin', 'metronidazole', 'bromphen/pseudoephedrinehcl', 'dextromethorphanhbr', 'pantoprazolesodium', 'naproxen', 'alprazolam', 'oseltamivirphosphate', 'nitrofurantoinmonohydratemacrocrystals', 'losartan potassium', 'metoprololsuccinateer', 'fluticasonepropionate', 'chlorhexidinegluconate', 'doxycyclinehyclate', 'metoprolol tartrate', 'phenazopyridinehcl', 'latanoprosteyedrops', 'sertralinehcl', 'trazodonehydrochloride', 'omeprazole', 'ciprofloxacin hydrochloride', 'levothyroxinesodium', 'meloxicam', 'docusatesodium', 'triamcinoloneacetonidecream']
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
            else:
                return -1
        

    
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
    print(newlemma)
    #j=0

    for i in med:
        if i in newlemma:
            return i
    
    #medicine="not found"
    #while j<len(med):
     #   final=search(med[j],newlemma)
      #  print(final)
       # 
        #if final<0:
         #   j+=1
        #elif final>=0:
         #   medicine=med[j]
          #  break
        
    """
    final=search("paracetamol",newlemma)
    print(final)
    if final>=0:
        return "not found"
    else:
        return "paracetamol"
    """
   # return medicine
@app.route('/side',methods=['GET'])
def returnte():
    side= {"acenextp":["Side effects-possible side effects are Nausea,Vomiting,Stomach pain/epigastric pain.,Loss of appetite,HeartburnDiarrhea.","Avoid consumption-Avoid consuming alcohol"],
       "paracetamol":["Side effects-an allergic reaction, which can cause a rash and swelling. flushing, low blood pressure and a fast heartbeat.","avoid cold and allergy medicines that contain paracetamol or acetaminophen"],
       "amoxicillin":["Side effects-possible side effects are stomach cramps, stomach pains, tarry stools, loosening of the skin, bloating.blood in the urine.","Don't Take antibiotics with milk or fruit juice."],
       "vitamin d":["Side effects-causes nausea and vomiting, weakness, and frequent urination.","Avoid consumption- aluminum-containing phosphate binders."],
       "ibuprofen":["Side effects-Headaches,Feeling dizzy,nausea.","painkillers like aspirin or naproxen"],
       "cetirizinehydrochloride":["Side effects-headaches,dry mouth,feeling sick (nausea),feeling dizzy,diarrhoea,sore throat.","Avoid consumption- aclidinium, cimetropium, glycopyrrolate, glycopyrronium, ipratropium"],
       "azithromycin":["Side effects-Losing your appetite,Headaches,,Feeling dizzy or tired,Changes to your sense of taste","Avoid consumption- best not to take it with other medicines that have the same side effect. "],
       "amlodipine besylate":["Side effects-  swelling of the hands, feet, ankles, or lower legs, dizziness ,drowsiness. ","Avoid consumption- grapefruit or grapefruit juice "],
       "albuterolsulfate":["Side effects- nervousness or shakiness, headache, throat or nasal irritation, and muscle aches","Avoid consumption- Methacholine,Midodrine.,Linezolid,Propranolol. "],
       "cyclobenzaprine hydrochloride":["Side effects- Clumsiness, mental depression, problems in urinating","Avoid consumption- Avoid taking MAO inhibitors "],
       "cephalexin":["Side effects- stomach pain, blistering, peeling of the skin,clay-colored stools","Avoid consumption- Avoid multivitamin with minerals "],
       "hydrochlorothiazide":["Side effects- blood in the urine or stools, blue lips, chest pain  ","Avoid consumption- Herbs that have a diuretic effect "],
       "lisinopril":["Side effects- tickly cough,  mild skin rash,Blurred vision ","Avoid consumption- avoid alcohol, probenecid, allopurinol, aspirin "],
       "amphetamine":["Side effects- Agitation,anxiety,bladder pain,crying. ","Avoid consumption- You should avoid or limit the use of alcohol while being treated with amphetamine. "],
       "dextroamphetamine":["Side effects- agitation, hallucinations , fever, sweating, confusion, fast heartbeat ","Avoid consumption- isocarboxazid, linezolid, methylene blue injection, phenelzine, rasagiline "],
       "loratadine 10":["Side effects- mouth sores, difficulty falling asleep ,nervousness ,weakness. ","Avoid consumption- azelastine, benzodiazepines, bromperidol, orphenadrine, oxomemazine, and paraldehyde "],
       "amoxicillin-clavulanate potassium":["Side effects- diarrhea, upset stomach,vomiting,mild skin rash. ","Avoid consumption- Grapefruit , Excess Calcium "],
       "folicacid":["Side effects- Feeling sick , Loss of appetite ,Bloating ","Avoid consumption- indigestion remedies "],
       "prednisone":["Side effects- Weight gain ,Indigestion, Sweating a lot ","Avoid consumption- carbohydrates and concentrated sweets "],
       "benzonatate":["Side effects- stuffy nose, feeling chilly, burning in the eyes ","Avoid consumption- cough and cold medications, antihistamines, anti-seizure drugs "],
       "gabapentin":["Side effects- Mood changes , Swollen arms and legs , Blurred vision ","Avoid consumption- medicines that make you sleepy or dizzy "],
       "zolpidemtartrate":["Side effects- drowsy, dizzy, lightheaded, clumsy or unsteady ","Avoid consumption- Opioids and benzodiazepines "],
       "sulfamethoxazole/trimethoprimds":["Side effects- changes in skin color , chest pain ,  hoarseness ","Avoid consumption- No Salt, Salt Substitute, Lite Salt, and even high-potassium foods   "],
       "methylprednisolone":["Side effects- bloating, bloody vomit, bone pain. ","Avoid consumption- carbohydrates and concentrated sweets, Grapefruit juice "],
       "fluconazole":["Side effects- clay-colored stools, difficulty with swallowing, fast heartbeat. ","Avoid consumption- erythromycin "],
       "aspirin":["Side effects- chest pain or discomfort,convulsions, severe or continuing, decreased frequency or amount of urine. ","Avoid consumption- NSAIDs, steroid medication,anticoagulant medicines  "],
       "atorvastatincalcium":["Side effects- Fever, Blistering, peeling, red skin rash ,Unusual tiredness","Avoid consumption- Avoid eating foods high in fat or cholesterol  "],
       "ferroussulfate":["Side effects- loss of appetite , constipation ,diarrhoea ","Avoid consumption- tea, coffee, eggs, dairy products and soybean products "],
       "cyanocobalamin":["Side effects- chest pain ,coughing that sometimes produces a pink frothy sputum ,decreased urine output","Avoid consumption- vitamin C "],
       "metronidazole":["Side effects- feeling or being sick, stomach pain, hot flushes, difficulty breathing, a pounding heartbeat ","Avoid consumption- disulfiram "],
       "bromphen/pseudoephedrinehcl":["Side effects- Dizziness, Drowsiness ,Dry throut ","Avoid consumption- isocarboxazid, metaxalone, methylene blue, moclobemide "],
       "dextromethorphanhbr":["Side effects- shakiness and unsteady walk ,slowed breathing. ","Avoid consumption- selegiline  and tranylcypromine "],
       "pantoprazolesodium":["Side effects- Blurred vision, flushed, dry skin ,fruit-like breath odor. ","Avoid consumption- rich, spicy and fatty foods. "],
       "naproxen":["Side effects- Ringing in the ears ,Changes in vision ,Feeling sleepy or tired ","Avoid consumption- Avoid drinking alcohol "],
       "alprazolam":["Side effects- Being forgetful , changes in patterns and rhythms of speech ,clumsiness or unsteadiness. ","Avoid consumption- Avoid using illegal drugs "],
       "oseltamivirphosphate":["Side effects- drooling ,facial swelling ,fast or irregular heartbeat ","Avoid consumption- methotrexate ,pemetrexed ,probenecid ,tafamidis. "],
       "nitrofurantoinmonohydratemacrocrystals":["Side effects- Nausea, vomiting, loss of appetite, or headache may occur ","Avoid consumption- Avoid eating high-sugar foods, drinking excessive amounts of alcohol, and consuming large amounts of caffeine "],
       "losartan potassium":["Side effects- Headaches,Feeling sick, Pain in your joints or muscles ","Avoid consumption- Potassium supplements, potassium-containing salt substitutes "],
       "metoprololsuccinateer":["Side effects- may worsen the symptoms of heart failure ","Avoid consumption- meat, milk, bananas and sweet potatoes "],
       "fluticasonepropionate":["Side effects- Bloody nose ,muscle aches ,pain or tenderness around the eyes and cheekbones. ","Avoid consumption- ceritinib , cobicistat ,desmopressin. "],
       "chlorhexidinegluconate":["Side effects- staining and an increase in tartar (calculus) on your teeth. ","Avoid consumption- Nasal spray "],
       "doxycyclinehyclate":["Side effects- decreased appetite ,diarrhea, difficulty with swallowing. ","Avoid consumption- Penicillin,Antacids,Iron supplements "],
       "metoprolol tartrate":["Side effects- Drowsiness, dizziness, tiredness, diarrhea, and slow heartbeat   ","Avoid consumption- Salty foods,Processed foods,Excess caffeine. "],
       "phenazopyridinehcl":["Side effects- bloody urine, difficult or painful urination, frequent urge to urinate, or sudden decrease in the amount of urine ","Avoid consumption- Do not use any leftover medicine for future urinary tract problems "],
       "latanoprosteyedrops":["Side effects- change in eye color redness of the eye, inflamed eyelid , irritated eye ","Avoid consumption- tafluprost,Travoprost,bimatoprost "],
       "sertralinehcl":["Side effects- Dry mouth ,Feeling dizzy ,Feeling tired or weak. ","Avoid consumption- grapefruit juice "],
       "trazodonehydrochloride":["Side effects- nausea,vomiting ,diarrhea ,constipation. ","Avoid consumption- OTC medications and supplements "],
       "omeprazole":["Side effects- Stomach pain ,Constipation ,Farting ","Avoid consumption- Greasy or fatty foods "],
       "ciprofloxacin hydrochloride":["Side effects- heartburn,diarrhea,vaginal itching,pale skin. ","Avoid consumption- avoid dairy produce like milk, cheese and yoghurt "],
       "levothyroxinesodium":["Side effects- Chest pain,decreased urine output, difficult or labored breathing. ","Avoid consumption- antacids,calcium salts,iron salts. "],
       "meloxicam":["Side effects- Bleeding gums,bloating,blood in the urine. ","Avoid consumption- Do not drink alcohol and grapefruits "],
       "docusatesodium":["Side effects-  wheezing, tightness in the chest or throat, trouble breathing or talking. ","Avoid consumption- lactulose,linaclotide,mineral oil,phenolphthalein "],
       "triamcinoloneacetonidecream":["Side effects-  drying of the skin,acne,change in skin color. ","Avoid consumption- steroids "]
      }
    str2=""
    str2=str(request.args['query'])
    final=side[str2][0]+side[str2][1]
    return final

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
    final=paran[0]
    final = re.sub(r'\d+', '', final)
    nfinal=""
    for i in final:
        nfinal+=i
    translator = nfinal.maketrans('', '', string.punctuation)
    final=nfinal.translate(translator)
    
    return final

if __name__ =="__main__":
    app.run()