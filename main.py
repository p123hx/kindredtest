# This is a sample Python script.
import kindred
import json
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def json2BioNLP(file):
    f= open(file)
    data = json.load(f)
    a1 = open("relations_test.a1", "a")
    a2 = open("relations_test.a2", "a")
    count1=1
    count2=1

    for triple in data:
        if triple["relation"] == "NA":
            continue
        t1 = count1
        t2 = count1+1
        head = "T"+str(count1)+" NA "+str(triple["head"]["start"])+" " +str(triple["head"]["start"]+triple["head"]["length"])+" "+triple["head"]["word"]+"\n"
        a1.write(head)
        count1+=1
        tail = "T"+str(count1)+" NA "+str(triple["tail"]["start"])+" " +str(triple["tail"]["start"]+triple["tail"]["length"])+" "+triple["tail"]["word"]+"\n"
        a1.write(tail)
        count1+=1
        relation = "E"+str(count2)+" "+triple["relation"]+" subj:T"+str(t2)+" obj:T"+str(t1)+"\n"
        a2.write(relation)
def helper():
    json2BioNLP("relations_test.json")
    corpus = kindred.load('json','relations_test')
    predicCorpus = corpus.clone()
    predicCorpus.removeRelations()
    classifier = kindred.RelationClassifier()
    classifier.train(corpus)
    classifier.predict(predicCorpus)
    f1score = kindred.evaluate(corpus,predicCorpus,metric='f1score')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    json2BioNLP("relations_test.json")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
