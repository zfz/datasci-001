import sys
import json

tweet_file = open(sys.argv[1])


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


#Create the dictionary of words without sentiment.
def word_dict(texts):
    words_dict = {}
    for text in texts:
        try:
            words = text.split(' ')
            for word in words:
                if word.lower() not in words_dict:
                    words_dict[word.lower()] = 0
        except:
            pass
    return words_dict


#Index the dictionary of words without sentiment.
def index_word(words_dict, texts):
    for i in xrange(len(texts)):
        words = texts[i].split(' ')
        for word in words:
            words_dict[word.lower()] += 1
    return words_dict


def main():
    texts = tweets_text(tweet_file)
    words_dict = word_dict(texts)
    words_dict = index_word(words_dict, texts)
    for w in words_dict:
        print "%s %f" % (w, float(words_dict[w]) / len(words_dict))


if __name__ == '__main__':
    main()
