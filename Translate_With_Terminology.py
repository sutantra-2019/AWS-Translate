import boto3

potterText = "Adaptation of the first of J.K. Rowling's popular children's novels about Harry Potter, a boy who learns on his eleventh birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. He is summoned from his life as an unwanted child to become a student at Hogwarts, an English boarding school for wizards. There, he meets several friends who become his closest allies and help him discover the truth about his parents' mysterious deaths."   
sourceLang = 'en'
targetLang = 'hi'

tranlateObj = boto3.client(service_name='translate')

with open('C:/MachineLearning/Translate/Potter_Terminology.tmx', 'rb') as f:
    Terminology = f.read()

Term_data = bytearray(Terminology)

termImport = tranlateObj.import_terminology(Name='Potter-Terminology', MergeStrategy='OVERWRITE', TerminologyData={"File": Term_data, "Format": 'TMX'})
print(termImport.get('TerminologyProperties')) 

termGet = tranlateObj.get_terminology(Name='Potter-Terminology', TerminologyDataFormat='TMX')
print(termGet.get('TerminologyProperties'))
  
response = tranlateObj.list_terminologies(MaxResults=10)
print(response.get('TerminologyPropertiesList'))

 
print("Translating 'potterText' from English to Hindi with no terminology...")
response = tranlateObj.translate_text(Text=potterText, SourceLanguageCode=sourceLang, TargetLanguageCode=targetLang)
print("Translated text: " + response.get('TranslatedText'))

 
print("Translating 'potterText' from English to Hindi with the 'Potter-Terminology' terminology...")
response = tranlateObj.translate_text(Text=potterText, TerminologyNames=["Potter-Terminology"], SourceLanguageCode=sourceLang, TargetLanguageCode=targetLang)
print("Translated text: " + response.get('TranslatedText'))
