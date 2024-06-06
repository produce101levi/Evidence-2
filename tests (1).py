import nltk

from nltk import CFG

from nltk.parse import RecursiveDescentParser


# Declare the variable "grammar" and assign the value of the grammar rules.

grammar = CFG.fromstring("""
    S -> SBP VP OP | QP | SBP VP
    QP -> Q SBP VP OP QM | Q SBP QM | SBP VP OP QM 
    SBP -> ART PREP SB | SB
    VP -> V ADVP | V | ADVP V | PREP V | PREP V PREP | V PREP V
    OP -> O | O ADJ | ART O | ART O ADJ | ADJ | O ADVP 
    Q -> 'Cadê' | 'Como'
    SB -> PLSB | SSB
    SSB -> SPR | SART SN
    SPR -> 'eu' | 'você' | 'ela'
    SN -> 'menino' | 'menina' | 'livro'
    PLSB -> PLPR | PLART PLN
    PLPR -> 'vocês' | 'nós' | 'eles' | 'elas'
    PLN -> 'meninos' | 'meninas' | 'cachorros' | 'gatos'
    ART -> PLART | SART
    PLART -> 'os' | 'uma'
    SART -> 'o' | 'a' | 'um'
    ADVP -> ADV | ADJ ART O
    ADV -> 'muito' | 'já'
    PREP -> 'de' | 'para' | 'teu' | 'se'
    V -> PLV | SV | IV
    PLV -> 'amam' | 'visitaram' | 'chamam' | 'gostam' | 'são'
    SV -> 'amo' | 'ama' | 'visitou' | 'chama' | 'visita' | 'comprou' | 'tem' | 'gosto' | 'fazer' | 'comer'
    IV -> 'viajar'
    O -> 'pizza' | 'Brasil' | 'carro' | 'praia' | 'cor' | 'musculação' | 'dias'
    ADJ -> PLADJ | SADJ
    SADJ -> 'grande' | 'novo' | 'avermelhada'
    PLADJ -> 'bonitos' | 'todos'
    QM -> '?'
""")

# Declare the parser.
parser = RecursiveDescentParser(grammar)

# Define a function to validate the sentence.
def valid_sentence(sentence):
    try: 
        parse_trees = parser.parse(sentence)
        if parse_trees:
            print("The sentence is valid within this grammar.")
            for tree in parse_trees:
                print(tree)
                tree.pretty_print()
        else:
            print("This sentence is not valid.")
    except ValueError as e:
        print("Error: ", e)

# Ask the user to insert an amount of sentences to validate.
number = int(input("Insert the amount of sentences you'd like to try out: "))

# Declare i as 0 for the while loop
i = 0

# Ask the user to insert the sentence they'd like to validate.
while i < number:
    print("Sentence number" , i+1, "/", number)
    sentence = input("Insert the sentence you'd like to try out: ").split()
    i += 1
    valid_sentence(sentence)


# Test sentences:


# Valid sentences:
# o livro tem uma cor avermelhada
# Cadê os meninos ?
# eu amo pizza
# os cachorros são bonitos
# eu gosto de fazer musculação todos os dias
# eu gosto de comer pizza todos os dias


# Invalid sentences:
# Cadê os meninos (no question mark)
# amo eu pizza
# pizza amo eu
# os bonitos cachorros são
# cachorros são bonitos
