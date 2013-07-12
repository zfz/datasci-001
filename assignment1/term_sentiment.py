import sys
import json
import re
from string import punctuation


def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))


#Extrace text from tweet entity.
def tweets_text(fp):
    texts = []
    tweets = fp.readlines()
    for tweet in tweets:
        try:
            texts.append(json.loads(tweet)['text'].encode('utf-8'))
        except:
            texts.append('')
    return texts


#Extract sentiment words to a dict.
def sentiment_dict(fp):
    d = {}
    words = fp.readlines()
    for word in words:
        l = word.split('\t')
        d[l[0].strip()] = int(l[1].strip())
    return d


#Caculate the score of each tweet.
def text_score(texts, d):
    scores = []
    for text in texts:
        try:
            words = text.split(' ')
            score = 0
            for word in words:
                if word in d:
                    score += d[word]
            #print '<sentiment:%f>' % float(score)
            scores.append(score)
        except:
            score = 0
            #print '<sentiment:%f>' % float(score)
            scores.append(score)
    return scores


#Format words for sentiment.
def formate_tweet(text):
    puncrx = re.compile(r'[{}\s]'.format(re.escape(punctuation)))
    return filter(lambda x: x.lower(), puncrx.split(text))


#Create the dictionary of words without sentiment.
def word_dict(texts, d):
    words_dict = {}
    for text in texts:
        try:
            words = formate_tweet(text)
            for word in words:
                if word not in d and word not in words_dict:
                    words_dict[word] = []
        except:
            pass
    return words_dict


#Index the dictionary of words without sentiment.
def index_word(words_dict, texts, d):
    for i in xrange(len(texts)):
        words = formate_tweet(texts[i])
        for word in words:
            if word not in d:
                words_dict[word].append(i)
    return words_dict


#Caculate the scores for words without sentiment.
def word_score(words_dict, scores):
    for w in words_dict:
        score = 0
        for i in words_dict[w]:
            score += scores[i]
        score = float(score) / len(words_dict[w])
        print "%s %f" % (w, score)


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    texts = tweets_text(tweet_file)
    d = sentiment_dict(sent_file)
    words_dict = word_dict(texts, d)
    scores = text_score(texts, d)
    words_dict = index_word(words_dict, texts, d)
    word_score(words_dict, scores)

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    lines(sent_file)
    lines(tweet_file)


if __name__ == '__main__':
    main()
