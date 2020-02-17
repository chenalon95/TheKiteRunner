# coding=utf-8
import xml.etree.ElementTree as etree
import xml.dom.minidom as minidom

from nltk import regexp_tokenize, RegexpTokenizer
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from xml.sax.saxutils import unescape


def createXML():
    # create header
    root = etree.Element("root")
    teiHeader = etree.SubElement(root, "teiHeader")
    fileDesc = etree.SubElement(teiHeader, "fileDesc")
    titleStmt = etree.SubElement(fileDesc, "titleStmt")
    title = etree.SubElement(titleStmt, "title")
    title.text = "THE KITE RUNNER"
    author = etree.SubElement(titleStmt, "author")
    author.text = "KHALED HOSSEINI"

    # create XML from text
    text = etree.SubElement(root, "text")
    episodeName = "ONE \n"
    currPar = ""
    par = etree.SubElement(text, "p")
    newLineFlag = False
    episode = etree.SubElement(text, "div1")
    episode.set('Type', 'episode')
    head = etree.SubElement(episode, "head")
    head.text = episodeName[:-1]

    episodeNames = ['TWO \n', 'THREE \n', 'FOUR \n', 'FIVE \n', 'SIX \n', 'SEVEN \n', 'EIGHT \n', 'NINE \n', 'TEN \n',
                    'ELEVEN \n', 'TWELVE \n', 'THIRTEEN \n', 'FOURTEEN \n', 'FIFTEEN \n', 'SIXTEEN \n', 'SEVENTEEN \n',
                    'EIGHTEEN \n', 'NINETEEN \n', 'TWENTY \n', 'TWENTY-ONE \n', 'TWENTY-TWO \n', 'TWENTY-THREE \n',
                    'TWENTY-FOUR \n', 'TWENTY-FIVE \n']
    i = 0
    st = StanfordNERTagger(
        '/home/chen/הורדות/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz',
        '/home/chen/הורדות/stanford-ner-2018-10-16/stanford-ner.jar',
        encoding='utf-8')
    with open("/home/chen/PycharmProjects/TheKiteRunner.txt", 'r') as f:
        j = 0
        for line in f:
            j += 1
            if j > 1000:
                print (j)
            if line == '\n' or line == '\t':
                if not newLineFlag:
                    newLineFlag = True
                    currPar = currPar[:-1]
                    #tokenized_text = word_tokenize(currPar)
                    #tokenized_text = regexp_tokenize(currPar, r"\n|\t|,|[. ]", True, False)
                    lastWordWasLoc = False
                    locationWord = ""
                    tokenizer = RegexpTokenizer('\w+|[\d\.]+|\S+')
                    tokenized_text = tokenizer.tokenize(currPar)
                    classified_text = st.tag(tokenized_text)
                    par = etree.SubElement(episode, "p")
                    par.text = ""
                    skip_rounds = 0
                    for word, tag in classified_text:
                        if skip_rounds != 0: # prev word was "<"
                            skip_rounds -= 1
                            par.text = par.text + word + " "
                        elif len(word) > 1:
                            if word[0] == word[-1] == '_':
                                word = "<highlight>" + word[1:-1] + "</highlight>"
                                par.text = par.text + word + " "
                            else:  # not arabic, might be location
                                if tag == 'LOCATION':
                                    if lastWordWasLoc:
                                        locationWord += " " + word
                                    else:
                                        lastWordWasLoc = True
                                        locationWord = "<" + tag + ">" + word
                                    # word = "<" + tag + ">" + word + "</" + tag + ">"
                                elif lastWordWasLoc:  # ended location
                                    lastWordWasLoc = False  # reset
                                    locationWord += "</LOCATION>"
                                    par.text = par.text + locationWord
                                else:
                                    par.text = par.text + word + " "
                        else:
                            if word == '.' or word == ',' or '?':
                                # delete space before .,?
                                if par.text[-1] != ">":
                                    par.text = par.text[:-1] + word + " "
                                else:
                                    par.text = par.text + word + " "
                            else:
                                par.text = par.text + word + " "
                    currPar = ""
                else:
                    continue
            elif i < len(episodeNames) and line == episodeNames[i]:
                newLineFlag = False
                episode = etree.SubElement(text, "div1")
                episode.set('Type', 'episode')
                head = etree.SubElement(episode, "head")
                head.text = episodeNames[i][:-2]  # remove ' \n'
                i = i + 1
            elif line == episodeName:
                continue
            else:
                currPar = currPar + line
                newLineFlag = False

    ##################################################
    tree = etree.ElementTree(root)
    tree.write("/home/chen/PycharmProjects/kite_runner.xml")

    rough_string = etree.tostring(root)
    re_parsed = minidom.parseString(rough_string)
    indent = "\t"
    string_of_xml = re_parsed.toprettyxml(indent)
    new_f = open("/home/chen/PycharmProjects/kite_runner_string.txt", "w")
    new_f.write(string_of_xml)
    new_f.close()
    return


createXML()
