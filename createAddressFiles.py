from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

with open("/home/chen/PycharmProjects/kite_runner_string.txt", 'r+') as f:
    # write addresses to new file called add_file
    with open("/home/chen/PycharmProjects/add_file.txt", 'w') as file_:
        for line in f:
            arr = line.split(' ')
            currAdd = ""
            addFlag = False
            for word in arr:
                if addFlag:  # last word was location
                    if word[-11:] == '</LOCATION>':
                        currAdd += word[:-11]
                        file_.write(currAdd)
                        file_.write("\n")
                        addFlag = False
                        currAdd = ""
                    else:
                        currAdd += word + " "
                # addFlag is false, last word wasnt location
                elif word[0:10] == '<LOCATION>':
                    if word[-11:] == '</LOCATION>':
                        file_.write(word[10:-11])
                        file_.write("\n")
                    else:  # location contains a few words
                        currAdd = word[10:] + " "
                        addFlag = True

f.close()
file_.close()

with open("/home/chen/PycharmProjects/part1_no_dups.txt", 'w') as no_dups_file:
    lines_seen = set()  # holds lines already seen
    for line in open("/home/chen/PycharmProjects/part1.txt", 'r'):
        if line not in lines_seen:  # not a duplicate
            no_dups_file.write(line)
            lines_seen.add(line)
no_dups_file.close()
with open("/home/chen/PycharmProjects/part2_no_dups.txt", 'w') as no_dups_file:
    lines_seen = set()  # holds lines already seen
    for line in open("/home/chen/PycharmProjects/part2.txt", 'r'):
        if line not in lines_seen:  # not a duplicate
            no_dups_file.write(line)
            lines_seen.add(line)
no_dups_file.close()
with open("/home/chen/PycharmProjects/part3_no_dups.txt", 'w') as no_dups_file:
    lines_seen = set()  # holds lines already seen
    for line in open("/home/chen/PycharmProjects/part3.txt", 'r'):
        if line not in lines_seen:  # not a duplicate
            no_dups_file.write(line)
            lines_seen.add(line)
no_dups_file.close()
