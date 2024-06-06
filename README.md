**Language Chosen:** Portuguese

**Language Context:** Portuguese is a Romance language originating from Portugal that’s spoken in 9 countries; Angola, Brazil, Cape Verde, East Timor, Equatorial Guinea, Guinea-Bissau, Mozambique, Portugal, & São Tomé and Príncipe. This language has a grammar structure mainly based on SVO; Subject, verb and object, as can be seen in the grammar (most sentences go back to SBP VP OP; with only a couple going back to SBP VP and questions leading back to QP; where a rule similar to SBP VP OP is followed.)


**Grammar**

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


**Tests**

All tested sentences, valid and invalid, are listen in the tests.py file.

**Valid:**

    o livro tem uma cor avermelhada
    
    Cadê os meninos ?
    
    eu amo pizza
    
    os cachorros são bonitos
    
    eu gosto de fazer musculação todos os dias
    
    eu gosto de comer pizza todos os dias
    

**Invalid:**

    Cadê os meninos (no question mark)
    
    amo eu pizza
    
    pizza amo eu
    
    os bonitos cachorros são
    
    cachorros são bonitos

**Analysis:**

The Chomsky Hierarchy has four types of grammar; unrestricted, context-sensitive, context-free and regular.


According to this hierarchy, this grammar would be cataloged as a Context-Free Grammar. The defining characteristics that make this grammar a CFG are as follows:

Each rule has a single non-terminal on the left side.

Each rule can have a combination of terminals and non terminals on the right side.

Substitution can take place regardless of the context they’re in

etc.

For example, 


    S -> SBP VP OP | QP | SBP VP

    SBP -> ART PREP SB | SB

    VP -> V ADVP | V | ADVP V | PREP V | PREP V PREP | V PREP V

    OP -> O | O ADJ | ART O | ART O ADJ | ADJ | O ADVP 

    SB -> PLSB | SSB

    SPR -> 'eu' | 'você' | 'ela'

    V -> PLV | SV | IV

    SV -> 'amo' | 'ama' | 'visitou' | 'chama' | 'visita' | 'comprou' | 'tem' | 'gosto' | 'fazer' | 'comer'

    O -> 'pizza' | 'Brasil' | 'carro' | 'praia' | 'cor' | 'musculação' | 'dias'


On the left side of the arrow, there is only one non-terminal.
On the right side, there’s a selection of terminals and non-terminals that can be substituted regardless of the elements that may be surrounding them.

This is not a Context Sensitive Grammar because a CSG can have a context. This means that the left side can have multiple symbols and their replacement can depend on them. 
Another reason why it is not a context sensitive grammar is because one of the conditions of a CSG requires the left-hand side of the production to be shorter or equal in length to the right-hand side of the it.

An unrestricted grammar’s main characteristic is the lack of restrictions and conditions that conform it. Since this grammar conforms to the rules of a Context Free Grammar, this type is immediately discarded.


A regular grammar is more restricted than a CFG. Each rule can only have a non-terminal followed by a terminal on the right-hand side, or a terminal followed by a non-terminal). Since this grammar is conformed by multiple terminals and nonterminals on the right side of the production, this cannot be a regular grammar.

**Time Complexity**

In the worst case, the algorithm's time complexity is an exponential complexity O(2^n).

This is because the algorithm uses a recursive descent parser to match the grammar rules with the test sentences.
When the test is initiated, the parser starts at S. From there, it looks through every non-terminal to validate whether the sentence is correct or not according to the grammar.
This parser either succesfully applies a rule or it doesn't and has to backtrack. This means it'll have to go through another option provided by the grammar rule to attempt again.
As it goes through each non-terminal, and the sentence length increases, the amount of attempts grows exponentially. The total amount of attempts is around 2^n, leaving the time complexity as O(2^n).






**Why is this the best solution?**

Initially, this was the grammmar that I had designed for this evidence.

    S -> SBP VP OP | Q SBP VP OP QM | Q SBP QM | SBP VP OP QM
    SBP -> ART SB | ART PR SB | SB | SB PR V
    VP -> V ADV | V | ADV V
    OP -> O | O ADJ | ART O
    Q -> ‘Cadê’ | ‘Como’
    SB -> ‘eu’ | ‘menino’ | ‘menina’ | ‘você’
    ART -> ‘o’ | ‘a’
    ADV -> ‘muito’ | ‘já’ 
    V -> ‘amo’ | ‘ama’ | ‘visitou’ | ‘chama’
    O -> ‘pizza’ | ‘Brasil’
    ADJ -> ‘grande’ 
    PR -> ‘teu’ | ‘se’
    QM -> ‘?’

This grammar is shorter, but it's ambiguous. We cannot know if a verb is in singular or plural. We can't tell from this grammar whether the subject that's being talked about in the sentence is plural or singular.

Not only is the grammar ambiguous but it's very prone to left recursion. If there's left recursion in the grammar, parsing it in order to have a correct sentence form is extremely complicated. Incorrect sentences are bound to be accepted as correct. For example, in portuguese, plural subjects must be followed by plural verbs and/or adjectives, and preceded by plural articles. 

That's why in this second design, the most important change was adding specificity for each part of the sentences that would be tested. Plural verbs and singular verbs are specified by the non terminals PV and SV. 

    
    S -> SBP VP OP | Q SBP VP OP QM | Q SBP QM | SBP VP OP QM | SVP VP VP OP
    SBP -> ART SB | ART PR SB | SB | SB PR V
    VP -> V ADV | V | ADV V | PR V | PR V PR
    OP -> O | O ADJ | ART O
    Q -> 'Cadê' | 'Como'
    SB -> PLSB | SSB
    PLSB -> PLPR | PLN
    PLPR -> 'vocês' | 'nós' | 'eles' | 'elas'
    PLN -> 'meninos' | 'meninas' | 'cachorros' | 'gatos'
    SSB -> SPR | SN
    SPR -> 'eu' | 'você' | 'ela'
    SN -> 'menino' | 'menina'
    ART -> 'o' | 'a' | 'um'
    ADV -> 'muito' | 'já'
    PR -> 'de' | 'para'
    V -> PLV | SV | IV
    PLV -> 'amam' | 'visitaram' | 'chamam' | 'gostam'
    SV -> 'amo' | 'ama' | 'visitou' | 'chama' | 'visita' | 'comprou'
    IV -> 'viajar'
    O -> 'pizza' | 'Brasil' | 'carro' | 'praia'
    ADJ -> 'grande' | 'novo'
    QM -> '?'

For the final design, question sentences were specified in order to avoid left recursion and to add order to the grammar. Plural articles are specified now, too.

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

Left recursion has been eliminated and the algorithm can run all the tests successfully.
    


**References**

<ins>Best Practices for Python:</ins>

Python Enhancement Proposals. (N/A). _PEP 8 - Style Guide for Python Code_. Retrieved from https://peps.python.org/pep-0008/#maximum-line-length

<ins>Chomsky Hierarchy:</ins>

GeeksForGeeks. (2023). _Chomsky Hierarchy in Theory of Computation_. Retrieved from https://www.geeksforgeeks.org/chomsky-hierarchy-in-theory-of-computation/

<ins>Big O Notation for Time Complexity Analysis</ins>

Olawanle, J. (2022). _Big O Cheat Sheet – Time Complexity Chart._ Retrieved from https://www.freecodecamp.org/news/big-o-cheat-sheet-time-complexity-chart/#:~:text=You%20get%20exponential%20time%20complexity,sequence%20is%20a%20good%20example.


