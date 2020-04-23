if __name__ == '__main__':
    import nltk

    groucho_grammar = nltk.CFG.fromstring("""
    S -> NP VP | VP | Modal NP VP | WhoP VP | WhatP NP VPW | WhereP NP VPWhere
    NP -> N 
    NP -> Det N 
    NP -> Adj N 
    NP -> Det N PP 
    PP -> P NP
    VP -> V Adv
    VP -> V NP Adv
    VP -> V NP Adv PP
    VP -> V
    VPW -> V 
    VPW -> V Adv
    VPW ->  V Adv PP
    VPWhere -> V
    VPWhere -> V Adv
    VPWhere -> V NP Adv
    WhoP -> PronounWho
    WhoP -> PronounWho Modal
    WhatP -> PronounWhat Modal
    WhereP -> ProAdvarb Modal
    Det -> 'the' | 'their' | 'your'
    Adj -> 'old' | 'red' | 'happy'
    Adv -> 'quickly' | 'slowly'
    N -> 'dogs' | 'parks' | 'statues' | 'people'
    V -> 'race' | 'walk' | 'eat'
    P -> 'in' | 'to' | 'on' | 'under' | 'with'
    Modal -> 'will' | 'should'
    PronounWho -> 'who'
    PronounWhat -> 'what'
    ProAdvarb -> 'where'
    """)

    groucho_grammar.start()
    groucho_grammar.productions()
    sent = ['who', 'walk', 'your', 'dogs', 'quickly', 'in', 'parks']
    parser = nltk.ChartParser(groucho_grammar)
    for tree in parser.parse(sent):
        print(tree)
        
