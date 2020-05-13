# coding: utf-8
from wordcloud import WordCloud


text_file = open("speech.txt")
bindata = text_file.read()
txt = bindata


wordcloud = WordCloud(background_color="white",
    font_path="System/Library/Fonts/HelveticaNeue.ttc",
    width=800,height=600).generate(txt)


wordcloud.to_file("./wordcloud_sample.png")
