from yast import Term

# placeholder for proper logging function
# currently just dumps to stderr (should 
# however write to yast log file)
def y2milestone(msg):
    print msg

# placeholder for proper logging function
# currently just dumps to stderr (should 
# however write to yast log file)
def y2error(msg):
    print msg

# placeholder for Buildins.foreach
def foreach(listOrMap):
    try:
        iterator = iter(listOrMap)
    except:
        y2error("%s is not iterable %s"%type(listOrMap))
        return None
    return listOrMap

# add — Add a key/value pair to a map or list
def add(listOrMap, key, value=None):
    if isinstance(listOrMap, dict):
        listOrMap[key] = value
    elif isinstance(listOrMap, Term):
         listOrMap.add(key)
    else: # assume list
        listOrMap.append(key)
    # should we clone the listOrMap here ?
    return listOrMap

def size(listMapOrTerm):
    if isinstance(listMapOrTerm, Term):
        return listMapOrTerm.size()
    # assume list or map 
    return len(listMapOrTerm)
