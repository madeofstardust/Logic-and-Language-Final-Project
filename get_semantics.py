'''
get_compositional_semantics function assigns lexical semantics to the roots of the tree, 
and the propagates the change further to the leaf.

get_lexical_semantics function finds appropriate lexical semantics in a dictionary

'''
from lexical_semantic_rules import lexical_semantic_rules
from nltk.sem.logic import *

read_expr = Expression.fromstring

## Start this function from the leaf.
def get_compositional_semantics(node):
  
  # get both of the parents:
  parent_1 = node.get_parent_left()
  parent_2 = node.get_parent_right()
  
  # never gets here!!!
  # if parents are None, it means we are at the roots. CS is defined for those, so just return
  if parent_1 is None and parent_2 is None:
    print("root")
    return
  
  # check if it's a situation where there is only one parent:
  if parent_1 is not None:
    # get the compositional semantics of parent_1:
    p1_cs = parent_1.get_compositional_semantics()
    p1_ls = parent_1.get_lexical_semantics()
    
    # if the parent doesn't have the compositional semantics, run this function on the parent:
    if p1_cs is None:
      _ = get_compositional_semantics(parent_1)
      p1_cs = parent_1.get_compositional_semantics()
      p1_ls = parent_1.get_lexical_semantics()

    #If there is no parent_2, it means that the rule was lx, which just changes the type of the node:
    # lx changes the lexical semantics of the node
    if parent_2 is None:
      # print(f"lx rule, the type should be {p1_cs}")
      lx = read_expr(f"(\\P\\Q(exist x.(P(x) & Q(x))))({p1_ls})").simplify()
      # print(f"lexical semantics should change to {lx}")
      node.set_compositional_semantics(p1_cs)
      node.set_lexical_semantics(lx)
      # print(node.get_cathegory())
      # print(node.get_lexical_semantics())
    
    else:
      # if there is the second parent, run repeat the steps done for parent one for this parent:
      p2_cs = parent_2.get_compositional_semantics()
      p2_ls = parent_2.get_lexical_semantics()
      if p2_cs is None:
        _ = get_compositional_semantics(parent_2)
        p2_cs = parent_2.get_compositional_semantics()
        p2_ls = parent_2.get_lexical_semantics()
  

      # print("\n")
      # print(f"node:{node}")
      # print(f"node.cathegory: {node.cathegory}")
      # print(f"parent 1: {parent_1} cs: {p1_cs} ls: {p1_ls}")
      # print(f"parent 2: {parent_2} cs: {p2_cs} ls: {p2_ls}")

      '''
      ## Important are the parents rules, so we get them:
      p1_ccg_cathegory = parent_1.get_cathegory()
      p2_ccg_cathegory = parent_2.get_cathegory()
      ARE THEY??
      '''
      ## to check the order, check the composition rule of this node.
      compositional_rule = node.get_compositional_rule()


      # check if there are any @ inside; if the semantic is compound, put it into brackets
      if "@" in p1_cs and p1_cs.split("and")[0]!="[[":
        p1_cs = f"({p1_cs})"
      if "@" in p2_cs and p2_cs.split("and")[0]!="[[":
        p2_cs = f"({p2_cs})"

      if p1_ls == "":
        node.set_compositional_semantics(f'{p1_cs}@{p2_cs}')
        node.set_lexical_semantics(read_expr(f"({p2_ls})").simplify())
        return
      if p2_ls == "":
        node.set_compositional_semantics(f'{p1_cs}@{p2_cs}')
        node.set_lexical_semantics(read_expr(f"({p1_ls})").simplify())
        return

      # apply rules"
      if compositional_rule=='fa':
        # print(f"forward application, the type should be {p1_cs}@{p2_cs}")
        node.set_compositional_semantics(f'{p1_cs}@{p2_cs}')
        node.set_lexical_semantics(read_expr(f"({p1_ls})({p2_ls})").simplify())

      elif compositional_rule=='ba':
        # print(f"backward application, the type should be {p2_cs}@{p1_cs}")
        node.set_compositional_semantics(f'{p2_cs}@{p1_cs}')
        node.set_lexical_semantics(read_expr(f"({p2_ls})({p1_ls})").simplify())

      elif compositional_rule =='conj':
        # print(f"conjunction, defining as {p1_cs}@{p2_cs}")
        node.set_compositional_semantics(f'{p1_cs}@{p2_cs}')
        node.set_lexical_semantics(read_expr(f"({p1_ls})({p2_ls})").simplify())

      elif compositional_rule == 'fc':
        # print(f"forward composition, the type should be \\x.{p1_cs}@({p2_cs}@x)")
        node.set_compositional_semantics(f'\\x.{p1_cs}@({p2_cs}@x)')
        node.set_lexical_semantics(read_expr(f"(\\x.{p1_ls})(({p2_ls})(x))").simplify())

      elif compositional_rule == 'bxc':
        # print(f"backward crossing composition, the type should be \\x.{p2_cs}@({p1_cs}@x)")
        node.set_compositional_semantics(f'\\x.{p2_cs}@({p1_cs}@x)')
        node.set_lexical_semantics(read_expr(f"(\\x.{p2_ls})(({p1_ls})(x))").simplify())
      
      elif compositional_rule =="lx":
        # print(f"lexical change., the type should be {p1_cs}")
        node.set_compositional_semantics(f'{p1_cs}')
        node.set_lexical_semantics(f"({p1_cs})")

      ##### ADD REMAINING RULES {'rp'}

    return node

def get_lexical_semantics(node):
    word = node.get_word().lower().strip('\'')
    lemma = node.get_lemma().lower().strip('\'')
    category = node.get_grammar()
    POS = node.get_POS()

    if lexical_semantic_rules.__contains__(word):
        lexical = lexical_semantic_rules[word].format(lemma = lemma)
    else:
        if lexical_semantic_rules.__contains__(category):
            if lexical_semantic_rules[category].__contains__(POS):
                lexical = lexical_semantic_rules[category][POS].format(lemma = lemma)
            else:
                lexical = lexical_semantic_rules[category]["common"].format(lemma = lemma)
        else:
          print(category + ' no such category')
  
    # print(lexical)
    node.set_lexical_semantics(lexical)
    return