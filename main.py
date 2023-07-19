import re
import pandas as pd


def remove_newline(text):
    new_list = []
    for x in text:
        string = x.replace("\n", "")
        new_list.append(string.lstrip())
    return new_list

def remove_spaces(text):
    new_list = []
    for x in text:
        new_list.append(" ".join(x.split()))
    return new_list

def unique (list):
    new_list=[]

    for l in list:

        if not l in new_list:
            new_list.append(l.lstrip())

    return new_list
def replace (list):

    accepted = ['و', 'ف', 'ع', 'ي']
    new_list = []
    for l in list:
        string=''
        sen= l.split()
        for x in sen:
            if len(x)==1:
                if x == accepted[1]:
                    x= 'في '
                    #string = re.sub(r'\b%s\b' % re.escape('ف'), 'في ')
                    #new_list.append( 'في ')
                elif x == accepted[2]:
                    x=  'على'
                    #string = re.sub(r'\b%s\b' % re.escape('ع'), 'على')
                    #new_list.append('على')
                elif x == accepted[3]:
                    x= 'يا'
                    #string = re.sub(('ي', 'يا'))
                    #new_list.append('يا')# '
                elif x not in accepted:
                    x=''
            string= string+' '+x

        new_list.append(string)
    return new_list


def generate_N_grams(text, n):
    n_gramlist= []
    for x in text:
            words = [word for word in x.split(" ") ]
            temp = zip(*[words[i:] for i in range(0, n)])
            ans = [' '.join(n) for n in temp]
           # print(ans)
            n_gramlist.append(ans)
    list=[]
    for gram in n_gramlist:
        for g in gram:
            list.append(g)
 #           print(g)
    return unique(list)

def preprocess (Text) :

    return remove_spaces(replace(remove_newline(Text)))

def read_text(file):
    with open(file,'r', encoding="utf8", ) as read:
        reader = read.readlines()


    return preprocess(reader)

def count_freq(text, file):
    freq=[]
    Strings= read_text(file)
    Text=unique(text)
    for t in Text:
        result=0

        for s in Strings:
            print(t)
            print(s)
                    #if t in s:
            result = result+ len(re.findall(r'\b%s\b' % re.escape(t),s))
        freq.append([t,result])
    #prin# t(freq)
    return freq
def count_frequ(Text, s):
    freq=[]
    Strings= Text

    counter = 0
    for t in Text:
        string= t.split()
        for x in string:
            print(x)
            if s==x:
                print(t)
                counter= counter+ 1
        #freq.append([t,counter])
    #print(freq)
    return counter

def rearrange (list,filename):
    result= count_freq(list,filename)
    result.sort(key=lambda i: i[1], reverse=True )
    return result

def final (list):
    final_list=[]
    for l in list:
        final_list.append(l[0])
    print('------------')
    for i in final_list:
        print(i)
    return final_list

def to_excel (text, name):

        df = pd.DataFrame(text, columns=["word","freq"])
        df.to_excel(name+'.xlsx', index=False)


def to_txt (text, name):


    with open(name+'.txt','w', encoding="utf8") as writer:
        for string in text:
            writer.write("%s\n" % string[0])



filename= "//Users/tawasal/Desktop/Flutter_Projects/تطبيق للصم/LastDatasetv1/blogV2.txt"

#"C:\Users\tawas\Documents\Arabic Speaker\corpus (5).txt"
#"C:\Users\tawas\Documents\Arabic Speaker\new corpus.txt"
#"C:\Users\tawas\Documents\Arabic Speaker\corpus (1).txt"
Text= read_text(filename)

unigram= generate_N_grams(Text,1)
bigram= generate_N_grams(Text,2)
trigram= generate_N_grams(Text,3)
fourgram= generate_N_grams(Text,4)

final_unigram= rearrange(unigram,filename)
final_bigram= rearrange(bigram,filename)
final_trigram= rearrange(trigram,filename)
final_fourgram= rearrange(fourgram,filename)

#to_excel(final_unigram, 'unigram')
#to_excel(final_bigram,'bigram')
#to_excel(final_trigram, 'trigram')
#to_excel(final_fourgram,'fourgram')
to_txt(final_unigram, 'unigram')
to_txt(final_bigram, 'bigram')
to_txt(final_trigram, 'trigram')
to_txt(final_fourgram, 'fourgram')
#print(count_frequ(Text,'للح '))
#print(replace(remove_numbers(['ع123 الطاولة ف الغرفة ي رغد','ع الطاولة56 ف الغرفة ي رغد','ع الطاولة الطويلة789  ف الغرفة ي رغد' ])))
#final(final_bigram)




