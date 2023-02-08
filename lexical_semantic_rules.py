lexical_semantic_rules = {
  ## EXCEPTIONS
  ",": '',
  # conj + 'CC'
  'and': '\\A\\B\\C.(B(C) & A(C))',

#\\A\\B\\C.(exists x y.(x = B(C) & y = A(C) & continuation(x, y)))
  'but': '\\A\\B\\C.(exists x.exists y.(x=B(C) & y=A(C) & contrast(x,y)))',
  # np/n + 'DT'
  'a':        '\\P\\Q(exist x.(P(x) & Q(x)))',
  'an':       '\\P\\Q(exist x.(P(x) & Q(x)))',
  'some':     '\\P\\Q(exist x.(P(x) & Q(x)))',
  'no':       '\\P\\Q -(exists x.(P(x) & Q(x)))',
  'each':     '\\P\\Q -(exists x.-Q(x) & P(x))',
  'every':    '\\P\\Q(-(exists x.(-Q(x) & P(x))))',
  # 'the':      '\\P\\Q(exist x.(P(x) & all y.(P(y) -> x=y) & Q(x)))',
  'the':     '\\P\\Q(exists x.(P(x) & Q(x)))',
  'another':  '\\P\\Q(exist x.(P(x) & all y.(P(y) -> x!=y) & Q(x)))',
  # np + 'DT'
  'this':     '\\P.(exists x.({lemma}(x) & P(x)))',
  'that':     '\\P.(exists x.({lemma}(x) & P(x)))',
  'some{x}':  '\\P.(exists x.({lemma}(x) & P(x)))', # something/someone/somebody
  'any{x}':   '\\P.(exists x.({lemma}(x) & P(x)))',
  'every{x}': '\\P.(-(exists x.(-P(x) & {lemma}(x))))',
  'no{x}':    '\\P. (-(exists x.({lemma}(x) & P(x))))',
  # np/n + PRP$
  'his': '\\P\\Q.(exist x.(male(x) & exist y.(user(y,x) & P(y) & Q(y))))',
  'her': '\\P\\Q.(exist x.(female(x) & exist y.(user(y,x) & P(y) & Q(y))))', 
  'its': '\\P\\Q.(exist x.(P(y) & Q(y)))',
  'our': '\\P\\Q.(exist x.(exist y.(user(x,y) & person(y) & sub(y,speaker) & P(x)) & Q(x)))',
  'your': '\\P\\Q.(exist x.(exist y.(user(x,y) & person(y) & equal(y,hearer) & P(x)) & Q(x)))', 
  'my': '\\P\\Q.(exist x.(exist y.(user(x,y) & person(y) & equal(y,speaker) & P(x)) & Q(x)))', 
  # (s\np)/(s\np) + VBZ (most common words)
  'is': '\\P\\Q\\M.((P(Q))(\\N.M(N)))',
  'has': '\\x.x',
  'does': '\\P\\Q\\M.((P(Q))(\\N.M(N)))',
  # (s\np)/(s\np) + VBP (most common words)
  'are': '\\P\\Q\\M.((P(Q))(\\N.M(N)))',
  'do': '\\P\\Q\\M.((P(Q))(\\N.M(N)))',
  'have': '\\x.x',
  # (s\np)\(s\np) and (s\np)/(s\np) + RB
  'not': '\\P\\Q\\M.(Q(\\N.-((P(\\O.(O(N))))(M))))',
  # ((s\np)\ (s\np))/pp
  'instead': '\\A\\B\\C\\D.(B(C) (\\E.(-(A(E)) & D(E))))',
  'rather': '\\A\\B\\C\\D.(B(C) (\\E.(-(A(E)) & D(E))))',
  'np\\np':
  {
    "common": '\\x.x'  
  },
  'n\\n':
  {
      "common": '\\P\\Q.exist x.({lemma}(x) & argu1(Q,x) & P(Q))'
  },
  'pp/pp':
  {
      "common": '\\A\\B.(exists x.({lemma}(x) & argu1(B,x) & A(x)))'
  },

  'pp/ (s\\np)':
  {
      "common": '\\A\\B.((A (\\C.(exists x.(entity(x) & C(x)))))(\\D.argu1(B,D)))'
  },

  '(n/n)/ (n/n)':
  {
      "common": '\\x.x'
  },

  '(np/n)\\np':
  {
    "common": '\\A\\B\\C.(A (\\D.(exists x.((argu1(x,D) & B(x)) & (C(x))))))'  # *
  },

  'np/n':
  {
    "common": '\\P\\Q(exist x.(P(x) & Q(x)))'  
  },

  'n/n': # adjective
    {
      "common": '\\P\\Q.exist x.({lemma}(x) & argu1(Q,x) & P(Q))',
      "'JJ'": '\\P\\Q.exist x.({lemma}(x) & argu1(Q,x) & P(Q))', # most frequent POS
      "'NN'": '\\P\\Q.exists x.({lemma}(x) & argu1(Q,x) & P(Q))'
    },
  
  # add common
  'n': # noun
    {
      "common": '\\x.{lemma}(x)',
      "'NN'": '\\x.{lemma}(x)', # most frequent POS
      "'NNS'": '\\x.{lemma}(x)' # plural noun (lemmatize)
    },
  
  '(s\\np)/np': # transitive verb
    {
      "common": '\\P\\Q\\M.(Q(\\N.(P(\\O.exists e.({lemma}(e) & argu1(e,N) & argu2(e,O) & M(e))))))',
      "'VBG'": '\\P\\Q\\M.(Q(\\N.(P(\\O.exists e.({lemma}(e) & argu1(e,N) & argu2(e,O) & M(e))))))',
      "'VBZ'": '\\P\\Q\\M.(Q(\\N.(P(\\O.exists e({lemma}(e) & argu1(e,N) & argu2(e,O) & M(e))))))'
    }, # most frequent POS 
  
  's\\np': # intransitive verb
    {
        "common": '\\P\\Q.P(\\R.exists x.({lemma}(x) & argu1(x,R) & Q(x)))',
        "'VBG'": '\\P\\Q.P(\\R.exists x.({lemma}(x) & argu1(x,R) & Q(x)))', # most frequent POS
        "'VBN'": '\\P.\\Q.P(\\R. exists x. ({lemma}(x) & patient(x,R) & Q(x)))' # add this to handle passive voice
  },
  '(s\\np)\\ (s\\np)': # adverb
    {
      "common": '\\P\\Q\\M.((P(Q))(\\N.(exists s({lemma}(s) & argu1(N,s) & (M(N))))))',
      "'RB'": '\\P\\Q\\M.((P(Q))(\\N.(exists s({lemma}(s) & argu1(N,s) & (M(N))))))', 
      "'RP'": '\\P.P' # 'up' and 'out'
    },

  '(s\\np)/ (s\\np)': 
    {
      "common": '\\P\\Q\\M.((P(Q))(\\N.(M(N))))',
      "'RB'": '\\P\\Q\\M.((P(Q))(\\N.(exists s({lemma}(s) & argu1(N,s) & (M(N))))))', 
      "'RP'": '\\P.P' # 'up' and 'out'
    },
  
  'np': # constant
    {
      "common": '\\P.(exists x.({lemma}(x) & P(x)))',
      "'DT'": '\\P.(exists x.({lemma}(x) & P(x)))', 
      "'PRP'": '\\P.(exists x.({lemma}(x) & P(x)))'
    },
  
  '(np\\np)/np': # prepositions
    {
        "common": '\\P\\Q\\M.(Q(\\N.(P(\\O.({lemma}(N,O) & M(N))))))',
        "'IN'": '\\P\\Q\\M.(Q(\\N.(P(\\O.({lemma}(N,O) & M(N))))))'},
  
  '((s\\np)/ (s\\np))/np': # copy from below
    {
        "common": '\\A\\B\\C\\D.((B(C))(\\E.(A(\\F.({lemma}(E,F) & D(E))))))',
        "'IN'": '\\A\\B\\C\\D.((B(C))(\\E.(A(\\F.({lemma}(E,F) & D(E))))))'},
  '((s\\np)\\ (s\\np))/np': # prepositions
    {
        "common": '\\A\\B\\C\\D.((B(C))(\\E.(A(\\F.({lemma}(E,F) & D(E))))))',
        "'IN'": '\\A\\B\\C\\D.((B(C))(\\E.(A(\\F.({lemma}(E,F) & D(E))))))'},

   'pp/np': # prepositions
    {
        "common": '\\P\\Q.(P(\\M.{lemma}(Q,M)))',
        "'IN'": '\\P\\Q.(P(\\M.{lemma}(Q,M)))'},
  
  '(s\\np)/pp': # present continuous intransative verb
    {
        "common": '\\A\\B\\C.(B(\\D.(exists e.({lemma}(e) & argu1(e,D) & (A(e) & C(e))))))',
        "'VBG'": '\\A\\B\\C.(B(\\D.(exists e.({lemma}(e) & argu1(e,D) & (A(e) & C(e))))))'},
  
  '((s\\np)/pp)/np': 
    {
        "common": '\\A\\B\\C\\D.(C(\\E.(A(\\F.(exists e.({lemma}(e) & argu1(e,F) & argu2(e,E) & (B(e) & D(e))))))))',
        "'VBG'": '\\A\\B\\C\\D.(C(\\E.(A(\\F.(exists e.({lemma}(e) & argu1(e,F) & argu2(e,E) & (B(e) & D(e))))))))'}, # present continuous transative verb
  '(s\\np)/ (pp/np)': 
    {
        "common": '\\A\\B\\C\\D.(C(\\E.(A(\\F.(exists e.({lemma}(e) & argu1(e,F) & argu2(e,E) & (B(e) & D(e))))))))'}, # copy from above
  
  '(np\\np)/ (s\\np)': 
    {
        "common": '\\A\\B\\C.(B(\\D.(((A(\\E.E(D)))(\\F.x)) & C(D))))',
        "'WDT'": '\\A\\B\\C.(B(\\D.(((A(\\E.E(D)))(\\F.x)) & C(D))))'}, # 'which'--add an x to \F. to make it work
  '((s\\np)\\ (s\\np))/pp':
    {
      "common": '\\A\\B\\C\\D.((B(C)) (\\E(exists x.({lemma}(x) & argu1(E,x) & A(x) & D(E)))))'},
  '(np\\np)/pp':
  {
      "common": '\\A\\B\\C.(B (\\D.(exists e.({lemma}(e) & argu1(e,D) & (A(e) & C(D))))))'
  }

}