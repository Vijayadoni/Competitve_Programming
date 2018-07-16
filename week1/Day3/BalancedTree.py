lev = 0

def is_balanced(root):
    global lev
    if not root :
        return True
    lev = 0
    lh = deep(root.left)
    rh = deep(root.right) 
    if (abs(lh - rh) <= 1) and is_balanced(
    root.left)  and is_balanced( root.right) :
        return True
    if lev != 1:
        return False
    return True

def deep(root):
    global lev
    if not root:
        return 0
    elif not root.left  and not root.right :
        lev+=1
    return max(deep(root.left), deep(root.right)) + 1
