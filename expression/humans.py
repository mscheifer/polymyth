import expression.nouns as nouns

men = []
women = []

def man(first_name, last_name):
     new_man = nouns.ProperNoun(first_name, last_name)
     men.append(new_man)
     return new_man

def woman(first_name, last_name):
     new_woman = nouns.ProperNoun(first_name, last_name)
     women.append(new_woman)
     return new_woman
