

def word_count(message):
    
    word_counts=dict()
    for word in message.split():
        if word[-1]==".":
            print(word)
            word=word[:-1]
            print(word)
        word=word.lower()
        if word in word_counts:
            word_counts[word]+=1
        else:
            word_counts[word]=1
    ans=[item for item in word_counts.items()]
    
    ans.sort(key = lambda item: (-item[1],item[0]))
    return ans
    
if __name__=="__main__":
    corpus = "She sells sea shells by the sea shore. The shells she sells are surely sea shells."
    ans=word_count(corpus)
    print(ans)
