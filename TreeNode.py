'''
This file contains a class TreeNode, which is used to create a tree structure of CCG derivations.
Each node contains information about 
  parents, 
  children, 
  the word contained in the node and its lemma (if applicable)
  part of speech tag
  lemma of the word
  lexical semantics
  rule that was used in the CCG derivation

'''

class TreeNode:
  def __init__(self, cathegory, parent_left=None,parent_right=None, child=None):
    self.cathegory = cathegory
    self.parent_left = parent_left
    self.parent_right = parent_right
    self.child = child

    self.depth = None
    self.rule = self.cathegory[1] # fa,ba,t...

    self.compositional_semantics = None # [[word]]
    self.lexical_semantics = None

    self.word = None # originally word: boys/girls...
    self.lemma = None # the lemma of the word: boy/girl
    self.grammar = None # category: np/n...
    self.POS = None # POS tag

  def add_child(self, child):
    self.child = child
  
  ## SET and GET parents
  def set_parent_left(self, parent):
    self.parent_left=parent

  def set_parent_right(self, parent):
    self.parent_right=parent

  def get_parent_left(self):
    return self.parent_left

  def get_parent_right(self):
    return self.parent_right


  ## get and simplify the cathegory:
  def get_cathegory(self):
    return self.cathegory

  def simplify_cathegory(self):
    # [4, 't', "np/n,'The','The','DT','O','O')"]
    if self.cathegory[1] == 't':
      self.depth = self.cathegory[0]
      self.rule = self.cathegory[1]
      self.grammar= self.cathegory[2].split(',')[0]
      self.word = self.cathegory[2].split(',')[1]
      self.lemma = self.cathegory[2].split(',')[2]
      self.POS = self.cathegory[2].split(',')[3]
      self.cathegory = self.grammar

      # Get the compositional semantics:
      mw = self.word
      # mw can be "'"
      if mw == "'":
        mw = ","
        self.grammar = ","
        self.word = ","
        self.lemma = ","
        self.POS = ","
        self.cathegory = self.grammar
      else:
        if mw[0] == "'":
          mw = mw[1:]
        if mw[-1] =="'":
          mw = mw[:-1]

      compositional_semantics = f"[[{mw}]]"

      self.compositional_semantics = compositional_semantics
    
  def set_word(self, word):
    self.word = word

  def get_word(self):
    return self.word
  
  def get_lemma(self):
    return self.lemma
  
  def get_grammar(self):
    return self.grammar
  
  def get_POS(self):
    return self.POS

  def set_compositional_semantics(self, semantics):
    self.compositional_semantics = semantics

  def get_compositional_semantics(self):
    return self.compositional_semantics

  def get_compositional_rule(self):
    return self.rule

  def set_lexical_semantics(self, lx):
    self.lexical_semantics = lx

  def get_lexical_semantics(self):
    return self.lexical_semantics

  #def set_POS(self):
  #  if self.grammar is not None:
  #    self.POS = self.grammar[3]

  def __repr__(self):
    return(f"{self.cathegory}, {self.rule}, {self.grammar}, {self.compositional_semantics}")

  def __str__(self):
    return(f"{self.cathegory}, {self.rule}, {self.grammar}, {self.compositional_semantics}")
