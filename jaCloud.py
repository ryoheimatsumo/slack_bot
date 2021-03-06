from MeCab import Tagger


import matplotlib.pyplot as plt
from wordcloud import WordCloud

t = Tagger()
text = """
Wherever you are
作詞：Taka    作曲：ONE OK ROCK
ONE OK ROCK - Wherever you are
I'm telling you, oh yeah
I softly whisper
Tonight tonight
You are my angel

愛してるよ
2人は一つに
Tonight tonight
I just say…
Wherever you are, I always make you smile
Wherever you are, I'm always by your side
Whatever you say, 君を思う氣持ち
I promise you「forever」right now

I don't need a reason, oh yeah
I just want you baby
Alright alright
Day after day

この先長いことずっと uh yeah
どうかこんな僕とずっと
死ぬまで Stay with me
We carry on…
Wherever you are, I always make you smile
Wherever you are, I'm always by your side
Whatever you say, 君を思う氣持ち
I promise you「forever」right now
Wherever you are, I never make you cry
Wherever you are, I never say goodbye
Whatever you say, 君を思う氣持ち
I promise you「forever」right now
僕らが出逢った日は2人にとって
一番目の記念すべき日だね
そして今日という日は2人にとって
二番目の記念すべき日だね

心から愛せる人
心から愛しい人
この僕の愛の真ん中には
いつも心(きみ)がいるから
Wherever you are, I always make you smile
Wherever you are, I'm always by your side
Whatever you say, 君を思う氣持ち
I promise you「forever」right now
Wherever you are, wherever you are
Wherever you are

"""
splitted = " ".join([x.split("\t")[0] for x in t.parse(text).splitlines()[:-1]])
text2="この僕の愛の真ん中には"
print(t.parse(text2))
wc = WordCloud(font_path="/Users/matsumotoryouhei/Downloads/Noto-unhinted/NotoSansCJKjp-Regular.otf", regexp="[\w']+")
wc.generate(text)
plt.imshow(wc)
plt.show()
