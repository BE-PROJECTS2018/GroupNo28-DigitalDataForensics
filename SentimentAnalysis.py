import nltk

import sys

import wx





class interface(wx.Frame):



    def __init__(self,parent,id):

        wx.Frame.__init__(self,parent,id,'Sentiment Analysis', size=(300,200))

        panel = wx.Panel(self)

        button = wx.Button(panel,label="Check Sentiment",pos=(150,100),size=(80,60))



        box=wx.TextEntryDialog(None,"Enter a statement to predict its sentiment","Sentiment Analysis","Type Something...")

        if box.ShowModal()==wx.ID_OK:

            sentiment_input = box.GetValue()

            sentiment_result = classifier.classify(format_sentence(sentiment_input))



            if sentiment_result== "pos":

                box=wx.MessageDialog(self,"It is a Positive Sentiment","Sentinent Analysis Result",wx.OK)

                box.ShowModal()

            else:

                box=wx.MessageDialog(self,"It is a Negative Sentiment","Sentinent Analysis Result",wx.OK)

                box.ShowModal()



def format_sentence(sent):

    return({word: True for word in nltk.word_tokenize(sent)})



pos = []

with open("tweets/pos_tweets.txt", encoding="utf8") as f:

    for i in f: 

        pos.append([format_sentence(i), 'pos'])



neg = []

with open("tweets/neg_tweets.txt", encoding="utf8") as f:

    for i in f: 

        neg.append([format_sentence(i), 'neg'])



training = pos[:int((.8)*len(pos))] + neg[:int((.8)*len(neg))]

test = pos[int((.8)*len(pos)):] + neg[int((.8)*len(neg)):]



from nltk.classify import NaiveBayesClassifier

classifier = NaiveBayesClassifier.train(training)





if __name__=='__main__':



	app=wx.App()

	frame=interface(parent=None,id=-1)

	app.MainLoop()

