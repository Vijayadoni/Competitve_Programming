res = None

def is_binary_search_tree(root):
    global res
    res = None
    return isabst(root)

def isabst(root):
    global res 
    if not  root :
        return True
    if not isabst(root.left) :
        return False
    if res and res.value > root.value:
        return False
    res = root
    return isabst(root.right) 
