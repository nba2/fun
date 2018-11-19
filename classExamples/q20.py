from tree import Tree

def play(db):
    if db.isLeaf: // aha! we can make a guess!
        guess = db.value
        response = input("Is it {}? [yes/no]".format(guess))
        while response not in ['yes', 'no']:
            response = input("Is it {}? [yes/no]".format(guess))
        if reponse == 'yes':
            print("I win!")
        else:
            object = input("Darn! What were you thinking of? ")
            question = input("What is a question that distinguishes {} [yes] from {} [no]? ".format(object,guess))
            db = Tree(question, Tree(object), Tree(guess))
    else: // more questions...
        question = db.value
        positive = db.left
        negative = db.right
        response = input(question)
        while response not in ['yes', 'no']:
            response = input(question)
        if response == 'yes':
            positive = play(positive)
        else:
            negative = play(negative)
        db = Tree(question,positive,negative)

    return db

def twentyQuestions(filename):
    db = Tree("a toaster")
    while input('Do you want to play? ') == 'yes':
        db = play(db)
