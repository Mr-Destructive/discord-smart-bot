arr = ["keep going forward", "this is gonna be a hit", "LFG", "lets make this project a hit", "love this art works tho", "I love this project", "WAGMI", "let's grinddd", "GRINDDD",
"let's grind ppl", "I want this sooo bad", "niceee", "dont stop ppl", "we can do this", "keep going", "yeah, it looks dope tho", "LVL20 here I come", "lessgooo", "keep grinding ppl!",
"we can do this", "server is mad rn!", "you guys rock!", "we can hit the moon", "mooooon", "gooooooooo ppl we can do this", "server is live af", "love this server", "the hype is real",
"lets go fam!", "who love these sneak peaks", "this is an awesome project for sure", "just keep grinding", "this is gonna be a hella community", "imagine if you can hold a NFT helment, damn!", 
"that's nice tho", "i really Like that idea", "keep going, you can do this my friend", "hey newbie, wassup?", "i am not tired", "tired means weak lol", "this is crazy af", "ppl are going mad",
"y'll work so hard to get into the WL", "so much energy", "right on time!", "need this so bad", "this community is the best", "yessir!", "maybe WL can be a life changing for us", "keep up guys!",
"never seen something like this before", "unique stuff", "wdym?", "keep going!", "like i said before, no pain - no gain", "don't give up", "try hard mode - ON", "that's great man!", "legit stuff",
"sweet!", "imma not gonna stop until LVL10", "keep going guys!", "moving forward"]

def messagesGen():
    try:        
        with open('messages.txt', mode='wt', encoding='utf-8') as myfile:
            myfile.write('\n'.join(arr))
            
        print(f'\n******* Text File created with {len(arr)} messages *******\n')   
        
    except Exception as err:
        print(err)
        
if __name__ == '__main__':
  messagesGen()