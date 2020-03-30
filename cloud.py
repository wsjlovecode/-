from os import path
# from imageio import imread
from PIL import Image
# import cv2
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS

d = path.dirname(__file__)

text=open(path.join(d,'coldplay.txt')).read()

# coldplay_mask=imread('coldplay.png')
# coldplay_mask=cv2.imread('coldplay.png')
coldplay_mask = np.array(Image.open(path.join(d,'coldplay.png')))

stopwords=set(STOPWORDS)
stopwords.add('Trust')

wc= WordCloud(background_color="white", max_words=2000, mask=coldplay_mask, stopwords=stopwords)
wc.generate(text)
# wc.to_file(path.join(d,'coldplay.png'))

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(coldplay_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()


# print(coldplay_mask)

