import sys
import json
from collections import defaultdict

hash_dict = defaultdict(int)


#Count hashtags in tweets.
def hash_tag(fp):
    lines = fp.readlines()
    for line in lines:
        try:
            tweet = json.loads(line)
            if tweet['entities']['hashtags'] != []:
                for hashtag in tweet['entities']['hashtags']:
                    hash_dict[hashtag['text']] += 1
        except:
            pass


def main():
    tweet_file = open(sys.argv[1])
    hash_tag(tweet_file)
    for hashtag in sorted(hash_dict, key=hash_dict.get, reverse=True)[:10]:
        print hashtag + ' ' + str(float(hash_dict[hashtag]))

if __name__ == '__main__':
    main()
