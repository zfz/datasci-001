import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    if record[0] == 'a':
        for k in range(5):
            key = (record[1], k)
            value = ('a', k, record[3])
            print 'map:'
            print key
            mr.emit_intermediate(key, value)
    elif record[0] == 'b':
        for i in range(5):
            key = (i, record[2])
            value = ('b', i, record[3])
            print 'map:'
            print key
            mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
        if v[0] == 'a':
            for l in list_of_values:
                if l[0] == 'b' and l[1] == v[1]:
                    total += v[2] * l[2]
        else:
            pass
    print 'reduce:'
    print key
    mr.emit((key[0], key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
