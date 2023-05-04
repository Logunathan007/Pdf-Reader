import subprocess as sp
import os
import datetime
from gtts import gTTS
from deep_translator import GoogleTranslator
class text_reader_translter:
    def __init__(self):
        self.file_name = "";
        
    def start(self):
        self.file_name = input("\n Enter a file name: ")
        if self.file_name == '':
            self.file_name=str(datetime.datetime.now())
        print("\n Folder Name is "+ self.file_name)
        sp.call(["mkdir", self.file_name])
        os.chdir(self.file_name)
        self.input_opener();
        txt = self.text();
        translated_txt = self.translate(txt);
        self.output_text(translated_txt)
        self.text_to_mp3(txt,translated_txt);

    def text(self):
        print("\n Translating To Tamil Please wait ...")
        x = open(self.file_name + "_OL" + ".txt", 'r')
        return x.read()
        
    def input_opener(self):
            sp.call(["gedit", self.file_name + "_OL" + ".txt"])
            print("\n Input File Name is "+ self.file_name + "_OL" + ".txt")
            text = input("\n Are you given input to "+self.file_name+ "_OL" + ".txt yes (or) no :")
            if(text.lower() == 'yes'):
                return;
            else:
                self.input_opener();

    def translate(self,txt):
        translated = GoogleTranslator(source='auto', target='ta').translate(text=txt)
        return translated

    def output_text(self,txt):
        y = open(self.file_name + "_Tamil" + ".txt", "a")
        y.writelines(str(txt))
        print("\n Successfully Translated & File Name is " + self.file_name + " Tamil" + ".txt")

    def text_to_mp3(self,oltxt,tatxt):
        print("\n Input Text Is Converted To Audio File Please wait ...")
        z = gTTS(text=oltxt,lang='en')
        z.save(self.file_name + "_OLAudio"+".mp3")
        print("\n Successfully Audio File Is Created & File Name is " + self.file_name + "_OLAudio" + ".mp3")
        print("\n Tamil Text Is Converted To Audio File Please wait ...")
        zz = gTTS(text=str(tatxt), lang='ta')
        zz.save(self.file_name + "_TamilAudio"+".mp3")
        print("\n Successfully Audio File Is Created & File Name is " + self.file_name + "_TamilAudio" + ".mp3")

t = text_reader_translter()
t.start()
