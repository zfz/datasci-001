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


#Format words for sentiment.
def formate_tweet(text):
    puncrx = re.compile(r'[{}\s]'.format(re.escape(punctuation)))
    return filter(lambda x: x.lower(), puncrx.split(text))


#Caculate the score of each tweet.
def text_score(texts, d):
    #scores = []
    for text in texts:
        try:
            words = formate_tweet(text)
            score = 0
            for word in words:
                #word = trip_word(word)
                if word.lower() in d:
                    score += d[word]
            print '%f' % float(score)
            #scores.append(score)
        except:
            score = 0
            print '%f' % float(score)
            #scores.append(score)
    #return scores


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    texts = tweets_text(tweet_file)
    #print len(texts)
    d = sentiment_dict(sent_file)
    #print len(d)
    text_score(texts, d)
    #print len(scores)

    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)


if __name__ == '__main__':
    main()
