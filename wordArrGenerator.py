import json

arr = ["keep going forward", "this is gonna be a hit", "LFG", "lets make this project a hit", "love this art works tho", "I love this project", "WAGMI", "let's grinddd", "GRINDDD",
"let's grind ppl", "I want this sooo bad", "niceee", "dont stop ppl", "we can do this", "keep going", "yeah, it looks dope tho", "LVL20 here I come", "lessgooo", "keep grinding ppl!",
"we can do this", "server is mad rn!", "you guys rock!", "we can hit the moon", "mooooon", "gooooooooo ppl we can do this", "server is live af", "love this server", "the hype is real",
"lets go fam!", "who love these sneak peaks", "this is an awesome project for sure", "just keep grinding", "this is gonna be a hella community", "imagine if you can hold a NFT helment, damn!", 
"that's nice tho", "i really Like that idea", "keep going, you can do this my friend", "hey newbie, wassup?", "i am not tired", "tired means weak lol", "this is crazy af", "ppl are going mad",
"y'll work so hard to get into the WL", "so much energy", "right on time!", "need this so bad"]

with open('random_phrase.json', 'w') as fp:
    json.dump(arr, fp)

print('JSON file created')    