import expression.nouns as nouns

men = []
women = []

def man(name):
     new_man = nouns.ProperNoun(name)
     men.append(new_man)
     return new_man

def woman(name):
     new_woman = nouns.ProperNoun(name)
     women.append(new_woman)
     return new_woman
