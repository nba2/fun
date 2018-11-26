from tree import Tree
import pickle

def play(db):
    if db.isLeaf:
        guess = db.value
        response = input("Is it {}? [yes/no] ".format(guess))
        while response not in ['yes', 'no']:
            response = input("Is it {}? [yes/no] ".format(guess))
        if response == 'yes':
            print("I win!")
        else:
            object = input("Darn! What were you thinking of? ")
            question = input("What is a question that distinguishes {} [yes] from {} [no]? ".format(object,guess))
            db = Tree(question, Tree(object), Tree(guess))
    else:
        question = db.value
        positive = db.left
        negative = db.right
        response = input(question+' ')
        while response not in ['yes', 'no']:
            response = input(question)
        if response == 'yes':
            positive = play(positive)
        else:
            negative = play(negative)
        db = Tree(question,positive,negative)

    return db

def twentyQuestions(filename):
    if filename is not None:
        with open(filename+'.pickle', 'rb') as handle:
            db = pickle.load(handle)
    else:
        db = Tree("a toaster")
        filename = 'db'
    while input('Do you want to play? ') == 'yes':
        db = play(db)
    with open(filename+'.pickle', 'wb') as handle:
        pickle.dump(db, handle, protocol = pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    from sys import argv
    filename = argv[1] if len(argv) > 1 else None
    twentyQuestions(filename)
