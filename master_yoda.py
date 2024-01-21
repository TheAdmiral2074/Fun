master_yoda1=('I am Home')
master_yoda2=('ready are we')

def master_knowledge(text):
    wordlist=text.split()
    rev_wordlist=wordlist[::-1]
    return " ".join(rev_wordlist)


print(master_knowledge(master_yoda1))
