import subprocess as sp
from textblob import TextBlob as tb
import datetime
from gtts import gTTS

file_name = input("\n Enter a file name: ")

if file_name == '':
    file_name=str(datetime.datetime.now())

print("\n Folder Name is "+ file_name)
sp.call(["mkdir", file_name])

class text_reader_translter:

    def input_opener(self):
        sp.call(["gedit", file_name + "/" + file_name + "_OL" + ".txt"])
        print("\n Input File Name is "+ file_name + "_OL" + ".txt")
       	text = input("\n Are you given input to "+file_name + "_OL" + ".txt yes (or) no :")
       	if(text.lower() == 'yes'):
            return;
        else:
            self.input_opener();
       	
    def text(self):
        print("\n Translating To Tamil Please wait ...")
        x = open(file_name + "//" + file_name + "_OL" + ".txt", 'r')
        self.txts=x.read()

    def translate(self):
        self.blob=tb(self.txts)
        self.translated_text=self.blob.translate(from_lang=self.blob.detect_language(),to='ta')

    def output_text(self):
        y = open(file_name + "/" + file_name + " Tamil" + ".txt", "a")
        y.writelines(str(self.translated_text))
        print("\n Successfully Translated & File Name is " + file_name + " Tamil" + ".txt")

    def text_to_mp3(self):
        print("\n Input Text Is Converted To Audio File Please wait ...")
        z = gTTS(text=self.txts,lang=self.blob.detect_language())
        z.save(file_name + "/" + file_name + "_OLAudio"+".mp3")
        print("\n Successfully Audio File Is Created & File Name is " + file_name + " OLAudio" + ".mp3")
        print("\n Tamil Text Is Converted To Audio File Please wait ...")
        zz = gTTS(text=str(self.translated_text), lang='ta')
        zz.save(file_name + "/" + file_name + "_TamilAudio"+".mp3")
        print("\n Successfully Audio File Is Created & File Name is " + file_name + " TamilAudio" + ".mp3")


t=text_reader_translter()
t.input_opener()
t.text()
t.translate()
t.output_text()
t.text_to_mp3()
