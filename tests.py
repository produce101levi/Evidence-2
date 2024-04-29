import nltk

from nltk import CFG

from nltk.parse import RecursiveDescentParser

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

parser = RecursiveDescentParser(grammar)

def validSentence(sentence):
    try: 
        parse_trees = list(parser.parse(sentence))
        if parse_trees:
            print("The sentence is valid within this grammar.")
            for tree in parse_trees:
                print(tree)
                tree.pretty_print()
        else:
            print("This sentence is not valid.")
    except ValueError as e:
        print("Error: ", e)

number = int(input("Insert the amount of sentences you'd like to try out: "))

i = 0
while i < number:
    print('Sentence number' , i+1, '/', number)
    sentence = input("Insert the sentence you'd like to try out: ").split()
    i += 1
    validSentence(sentence)


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