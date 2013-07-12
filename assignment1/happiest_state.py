import sys
import json

states = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'National': 'NA',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands': 'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
}

scores = {
        'AK': 0,
        'AL': 0,
        'AR': 0,
        'AS': 0,
        'AZ': 0,
        'CA': 0,
        'CO': 0,
        'CT': 0,
        'DC': 0,
        'DE': 0,
        'FL': 0,
        'GA': 0,
        'GU': 0,
        'HI': 0,
        'IA': 0,
        'ID': 0,
        'IL': 0,
        'IN': 0,
        'KS': 0,
        'KY': 0,
        'LA': 0,
        'MA': 0,
        'MD': 0,
        'ME': 0,
        'MI': 0,
        'MN': 0,
        'MO': 0,
        'MP': 0,
        'MS': 0,
        'MT': 0,
        'NA': 0,
        'NC': 0,
        'ND': 0,
        'NE': 0,
        'NH': 0,
        'NJ': 0,
        'NM': 0,
        'NV': 0,
        'NY': 0,
        'OH': 0,
        'OK': 0,
        'OR': 0,
        'PA': 0,
        'PR': 0,
        'RI': 0,
        'SC': 0,
        'SD': 0,
        'TN': 0,
        'TX': 0,
        'UT': 0,
        'VA': 0,
        'VI': 0,
        'VT': 0,
        'WA': 0,
        'WI': 0,
        'WV': 0,
        'WY': 0,
}


def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))


#Extrace sentiment from tweet entity.
def tweets_states(fp, d):
    lines = fp.readlines()
    for line in lines:
        try:
            tweet = json.loads(line)
            if tweet['place']['country_code'] == 'US':
                state = formate_state(tweet['place']['full_name'])
                scores[state] += text_score(tweet['text'], d)
        except:
            pass


#Format state name.
def formate_state(name):
    names = name.split(',')
    names = [n.strip() for n in names]
    if names[1] in scores.keys():
        return names[1]
    elif names[0] in states.keys():
        return states[names[0]]
    else:
        return None


#Extract sentiment words to a dict.
def sentiment_dict(fp):
    d = {}
    words = fp.readlines()
    for word in words:
        l = word.split('\t')
        d[l[0].strip()] = int(l[1].strip())
    return d


#Caculate the score of each tweet.
def text_score(text, d):
    try:
        words = text.split(' ')
        score = 0
        for word in words:
            #word = trip_word(word)
            if word.lower() in d:
                score += d[word]
    except:
        score = 0
    return score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    d = sentiment_dict(sent_file)
    tweets_states(tweet_file, d)
    #print scores
    print max(scores, key=scores.get)


if __name__ == '__main__':
    main()
