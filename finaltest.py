import nltk
nltk.download('punkt')
grammar = nltk.grammar.CFG.fromstring("""
S -> NP VP | NP AuxP | NP VtP
NP -> NPrp | NProSub | NounPhrase | DemP | DemS
NounPhrase -> DemP NounPlural | NounPlural | DemS NounA | DemS NounAn | DetG Noun | DetA NounA | DetAn NounAn | NounSpecial
NounPhrase -> DemP AdjP NounPlural | AdjP NounPlural | DemS AdjP NounA | DemS AdjP NounAn | DetG AdjP Noun | DetA AdjP NounA | DetAn AdjP NounAn | AdjP NounSpecial 
NounPhrase -> NounPhrase PP
Noun -> NounPlural | NounA | NounAn | NounSpecial 
NPPro -> NPrp | NProObj | NounPhrase
NPComp ->  NPPro | ConjObj S
AdjP -> Adj | Adj AdjP
PP -> P NPPro | ConjAdv S 
PP -> P NPPro PP | PP ConjAdv S
Vi -> ViS | ViPa 
VP -> Vi | Vi PVP ViS | Vi AdvP PVP ViS
VP -> VP AdvP | Adv VP
AdvP -> Adv | Adv PP | PP
VtSP -> VtS NPComp | VtS NPComp NPComp | VtS NPComp PVP ViS
VtPing -> VtPr NPComp | VtPr NPComp NPComp | VtPr NPComp PVP ViS
ParticipleHave -> PerfectHaves | Modal Have 
ParticipleBe -> PerfectHaves Been Being | Modal Have Been Being | AuxBe Being 
ParticipleBeenP -> AuxBe | AuxBe Adv | Modal BeS| Modal BeS Adv  
ParticipleBeenP -> PerfectHaves Been | PerfectHaves Been Adv | PerfectHaves Adv Been
ParticipleBeenP -> Modal Have Been | Modal Have Been Adv | Modal Have Adv Been
AuxP -> Modal ViS | Modal Adv ViS | Modal VtSP | Modal Adv VtSP | Modal BeS VtPing | Modal BeS Adv VtPing
AuxP -> ParticipleHave ViPP | ParticipleHave VtPP NPComp | ParticipleHave VtPP NPComp NPComp | ParticipleHave Adv VtPP NPComp | ParticipleHave Adv VtPP NPComp NPComp
AuxP -> ParticipleBe ViPP | ParticipleBe VtPP 
AuxP -> ParticipleBeenP ViPP | ParticipleBeenP ViPr | ParticipleBeenP VtPP
AuxP -> Adv AuxP | AuxP AdvP 
VtP -> VtPa NPComp | VtPa NPComp NPComp| | VtPa NPComp PVP ViS
VtP -> Adv VtP | VtP AdvP
DetA -> 'a' 
DetAn -> 'an'
DetG -> 'the' | 'my'| 'her' | 'his' | 'their' | 'our' | 'your'
DemS -> 'this' | 'that' 
DemP -> 'these' | 'those'
NProSub -> 'I' | 'you' | 'he' | 'she' | 'it' | 'we' | 'they'
NProObj -> 'me' | 'you' | 'him' | 'her' | 'it' | 'us' | 'them'
NPrp -> 'Nadia' | 'Marseilles' | 'Google' | 'Ross' | 'Paris'
NounA -> 'cat' | 'fur' | 'rutabaga' | 'boat' | 'poodle' | 'cloth' | 'cheese' | 'man' | 'hovercraft' | 'help' | 'menu' | 'left' | 'shot' | 'jump' | 'win' | 'saw' | 'reward' | 'demand' | 'find' | 'film'
NounAn -> 'eggplant' | 'autoclave' | 'elephant' | 'autopoiesis' 
NounPlural -> 'cats' | 'furs'| 'rutabagas' | 'eggplants' | 'boats' | 'poodles' | 'autoclaves' | 'cloths' | 'cheeses' | 'men' | 'elephants' | 'hovercrafts' | 'autopoieses' | 'menus' | 'shots' | 'jumps'| 'wins' | 'saws' | 'rewards' | 'demands' | 'finds'
NounSpecial -> 'fur' | 'rutabaga'| 'eggplant' |'cheese'| 'help' | 'autopoiesis' | 'want'
P -> 'with' | 'for' | 'on' | 'onto' | 'to' | 'of' | 'from' | 'before' | 'after'
PVP -> 'to'
Adv -> 'slowly' | 'immediately' | 'already' | 'really' | 'always' | 'before' | 'after' | 'yesterday' | 'soon' | 'early' | 'pretty'
Adj -> 'handsome' | 'tall' | 'long' | 'soft' | 'fur'
ConjObj -> 'that'
ConjAdv -> 'before' | 'after'
Modal -> 'can' | 'may' | 'could' | 'should' | 'shall' | 'might' | 'must' | 'would' | 'will'
PerfectHaves -> 'have' | 'has' | 'had'
Have -> 'have'
AuxBe -> 'is' | 'are' | 'am' | 'was' | 'were'
Been -> 'been'
BeS -> 'be'
Being -> 'being'
ViS -> 'help' | 'be' | 'arrive' | 'aspire' | 'leave' | 'shoot' | 'eat' | 'fondle' | 'jump' | 'believe' | 'win' | 'see' | 'want' | 'demand' | 'give'
ViPr -> 'helping' | 'being' | 'arriving' | 'aspiring' | 'leaving' | 'shooting' | 'eating' | 'fondling' | 'jumping' | 'believing' | 'winning' | 'seeing' | 'wanting' | 'demanding' | 'giving'
ViPa -> 'helped' | 'was' | 'were'| 'arrived' | 'aspired' | 'left' | 'shot' | 'ate' | 'fondled' | 'jumped' | 'believed' | 'won' | 'saw' | 'wanted' | 'demanded' | 'gave' | 'returned'
ViPP -> 'helped' | 'been' | 'arrived' | 'aspired' | 'left' | 'shot' | 'eaten' | 'fondled' | 'jumped' | 'believed' | 'won' | 'seen' | 'wanted' | 'demanded' | 'given' | 'returned'
VtS -> 'help' | 'have' | 'be' | 'arrive' | 'aspire' | 'leave' | 'shoot' | 'eat' | 'fondle' |'buy' | 'tell' |'jump' | 'believe' | 'win' | 'see' | 'want' | 'demand' | 'give'  | 'remind' | 'reward' | 'give'
VtPr -> 'helping' | 'having' | 'arriving' | 'aspiring' | 'leaving' | 'shooting' | 'eating' | 'fondling' | 'buying' | 'telling' | 'jumping' | 'believing' | 'winning' | 'seeing' | 'wanting' | 'reminding' | 'rewarding' | 'demanding' | 'finding' | 'giving'
VtPa -> 'helped' | 'had' | 'was' | 'were' | 'left' | 'shot' | 'ate' | 'fondled' | 'brought' | 'told' | 'jumped' | 'believed' | 'won' | 'saw' | 'wanted' | 'reminded' | 'rewarded' | 'demanded' | 'found' | 'gave'
VtPP -> 'helped' | 'had' | 'been' | 'left' | 'shot' | 'eaten' | 'fondled' | 'brought' | 'told' | 'jumped' | 'believed' | 'won' | 'seen' | 'wanted' | 'reminded' | 'rewarded' | 'demanded' | 'found' | 'given'
""")

test_positive = """Nadia left immediately 
the cat with the long soft fur slowly ate 
she arrived
Nadia will leave
Nadia has left 
Nadia may have been leaving 
Nadia fondled the eggplant 
the handsome poodle brought Ross to the autoclave 
Nadia brought a cloth for the cheese 
they told her to jump onto the elephant 
she believed that Ross was already on the hovercraft 
she really wanted help 
she really aspired to help 
cheese was always on the menu 
the eggplant reminded Nadia of Ross 
Nadia rewarded the man with the eggplant
Nadia won an elephant
a rutabaga could have been demanded 
autopoiesis always reminded her of Marseilles
I saw Nadia on a boat with my elephant
Nadia was reminded
an elephant had been being won
Nadia arrived
she arrived
the eggplant won
Nadia arrived soon
Ross slowly jumped
she arrived early
we slowly ate
a cat jumped immediately
the handsome tall men jumped slowly
the handsome tall men immediately jumped
the soft long long fur jumped slowly
the soft long long fur slowly jumped 
the soft long long fur slowly jumped with me
the soft long long fur slowly jumped with Nadia
the soft long long fur slowly jumped with a tall handsome cat
the soft long long fur slowly jumped on him
the eggplant won on the boat
the eggplant was leaving
the eggplant was slowly leaving
the eggplant was leaving slowly
Nadia was arriving
Nadia has been reminded
the soft long long fur was leaving slowly
the soft long long fur was slowly leaving 
the soft long long fur was slowly jumping with me
the soft long long fur was slowly jumping with Nadia
the soft long long fur was slowly jumping on him
the soft long long fur was jumping with a tall handsome cat
Nadia was eating with Google
Nadia was eating slowly with Google
the eggplant was eaten
the eggplant was eaten immediately
the eggplant was immediately eaten
the eggplant was being eaten
the eggplant has arrived yesterday
Nadia has left early to the boat
the cat has been shot 
the cat had been shot yesterday
the cat had been shooting on the boat
the cat has been being shot
Ross has been being shot
Ross had been shot
the eggplant will arrive with Google
the eggplant will arrive on the boat
Ross will jump slowly
Ross must jump on the boat slowly
the eggplant will arrive with the long soft fur cat
the eggplant will arrive on the boat with the long soft fur cat
the eggplant will arrive immediately on the boat with the long soft fur cat
the eggplant will arrive on the boat with the long soft fur cat soon
the eggplant may have arrived 
the eggplant may have arrived after
the eggplant may have been eaten
the eggplant must be arriving
the eggplant must be eaten before
I will be arriving
Ross will be arrived
Ross will be arrived soon
Ross will be arrived pretty soon
Ross will be arriving pretty soon
Ross will be arriving on the boat pretty soon
Ross will be eating an eggplant on the boat pretty soon
Google rewarded Nadia
Google rewarded Nadia pretty soon
Google rewarded the tall long fur cat immediately
Google reminded him of the tall long fur cat
Google immediately reminded him of the tall long fur cat
Ross gave him an eggplant
Ross gave him the tall long fur cat
Ross jumped on him
Ross slowly jumped on him
Ross ate an eggplant
Ross ate an eggplant before she arrived
Ross told Nadia to jump
Ross told Nadia to jump slowly
I will have a cat soon
I will immediately have a cat soon
she will shoot a cat
I could have demanded an eggplant"""

test_negative = """Nadia with the long soft fur slowly ate 
the cat with the tall her arrived 
Nadia will left 
Nadia has could leave 
Nadia has had left 
Nadia found 
Ross brought to him 
they told to jump onto the elephant
him ate
me ate slowly
the her jumped
she with the soft long fur already ate
her with the soft long fur ate soon
the handsome Google arrived early
the soft long long Nadia jumped slowly
the soft long long her slowly jumped with me
the soft long long fur slowly jumped with I
the soft long long fur slowly jumped on the him
her was leaving
the soft long long Google was leaving slowly
the soft long long fur was slowly jumping with I
the soft long long her was slowly jumping with me
the soft long long Nadia was slowly jumping on him
the soft long long fur was jumping on the him
him was eating with Google
him was eaten
Nadia was ate
the eggplant was be eaten
the eggplant was being ate
the eggplant has arriving 
the eggplant has arrive
her has arrived 
her has been shot 
Ross has been being shooting 
the cat have had been shot yesterday
Ross has been shoot
the cat must arriving
the eggplant will arriving
the eggplant will be ate
Nadia was eat with Google
Nadia was being eat slowly
Nadia could have been arrive early
Nadia has had been left early
the cat has had been shot
the cat has had been shooting
Ross has had been being shot
Ross had been has shot
the eggplant had will arrive with Google
the eggplant could will arrive on the boat
Ross will jumping slowly
Ross must jump on the Nadia slowly
the eggplant may has arrived 
the eggplant may had been eaten
the eggplant may has been eating 
Ross told slowly
Ross will gave"""

if __name__ == '__main__':
    parser = nltk.parse.BottomUpChartParser(grammar)
    test_suc=[s.split() for s in test_positive.split('\n')]
    success_count = 0
    for s in test_suc:
        try:
            if(len(list(parser.parse(s))) != 0):
                success_count += 1
            else:
                print(s)
        except Exception as e:
           print(e)
           pass
    print('Success: ' + str(success_count))
    if success_count != 101:
        print('Errors found in the positive cases')
    
    test_fail=[s.split() for s in test_negative.split('\n')]
    fail_count = 0
    for s in test_fail:
        try:
            if(len(list(parser.parse(s))) == 0):
                fail_count += 1
            else:
                print(s)
        except Exception as e:
           print(e)
           pass
    print('Failed: ' + str(fail_count))
    if fail_count != 56:
        print('Errors found in the negative cases')