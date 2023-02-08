'''
The function build_the_tree takes a dictionary as an input and creates 
a tree-structure based on information inside and returns the roots of this tree.

The function get_line_dict build the abovementioned dictionary. 
It extracts information needed to build the tree from the derivation 
saved in a prolog files that can be found at https://github.com/kovvalsky/LangPro
# input: the string version of the derivation
# output: line_dict (that will be the input of build_the_tree)

traverse_tree function is a simple template function for visiting every node in the graph.
'''
from TreeNode import TreeNode


# Extract the information needed to build the tree from the derivation
# input: the string version of the derivation
# output: line_dict(will be the input of build_the_tree)
def get_line_dict(ccg_derivation):
  lines = ccg_derivation.splitlines()

  # measure the indent of each line:
  line_dict = {}

  for i, line in enumerate(lines):
    # If there are no brackets, discard this line:
    if "(" not in line:
      continue
    # discard ccg line as well:
    if "ccg" in line:
      continue

    #look for brackets and split it there:
    splitted_line = line.split("(")
    # cathegory will be at the first spot. Remove blanks from the cathegory and count them:
    cathegory = splitted_line[0]
    indent = 0
    while cathegory[0] == " ":
      cathegory = cathegory[1:]
      indent +=1
    
    # tr(s:_G854478/ (s:_G854484\np),
    # delete the ':del/:ng' in category
    s = "(".join(splitted_line[1:])
    while s.find(':') != -1:
      l1 = s.find(':')
      for j in range(1,10):
        if s[l1 + j] == '\\' or s[l1 + j] == '/' or s[l1 + j] == ',' or s[l1 + j] == ')':
          l2 = l1 + j
          break
      s = s[:l1] + s[l2:]
    # delete the '_'
    s = s.replace('_','')
    line_dict[i] = [indent, cathegory, s[:-1]]
    # print(line_dict[i])

  return line_dict

def build_the_tree(subtree_structure_dict, child=None, parent_nodes=[]):

  # if there is no subtree, return:
  if not subtree_structure_dict:
    return parent_nodes, None

  # Create the tree from the first item:
  m = min(subtree_structure_dict.keys())
  current_leaf = subtree_structure_dict.pop(m)
  current_leaf_tree = TreeNode(current_leaf, child=child)

  roots = parent_nodes.copy()

  # check if the current leaf is a root:
  if "t" in current_leaf[1]:
    roots.append(current_leaf_tree)
    current_leaf_tree.simplify_cathegory()
    # current_leaf_tree.set_POS()
    return roots, current_leaf_tree


  #############
  # Proceed: 
  # define two parents of current child node: the first one is the current Node, the second one is the node with the same depth 
  idx = min(subtree_structure_dict.keys())
  first_parent = subtree_structure_dict.pop(idx)
  first_parent_depth = first_parent[0]

  second_parent = None

  # Iterate over the subtree structure dict. Until you find a node of the same depth, this is the first subtree. 
  tree_copy = subtree_structure_dict.copy()
  first_parent_subtree = {idx:first_parent}
  for key in subtree_structure_dict.keys():
    # If the depth is the same, that is our second parent's scope starting:
    if subtree_structure_dict[key][0] == first_parent_depth:
      second_parent = key
      break
    else:
      first_parent_subtree[key] = tree_copy.pop(key)

  # the second subtree is the remaining part of tree_copy:
  second_parent_subtree = tree_copy.copy()
  
  # recursively run the function on both parents:
  r1, parent_1 = build_the_tree(first_parent_subtree, child=current_leaf_tree, parent_nodes=roots)
  r2, parent_2 = build_the_tree(second_parent_subtree, child=current_leaf_tree, parent_nodes=roots)
  
  roots = r1 + r2
  current_leaf_tree.set_parent_left(parent_1)
  current_leaf_tree.set_parent_right(parent_2)
  
  return roots, current_leaf_tree


def traverse_tree(node):
  print("\n\n")
  print(node.get_cathegory())
  print(node.get_compositional_semantics())
  print(node.get_compositional_rule())
  
  parent_1 = node.get_parent_left()
  parent_2 = node.get_parent_right()
  
  if parent_1:
    traverse_tree(parent_1)
  if parent_2:
    traverse_tree(parent_2)

  return
