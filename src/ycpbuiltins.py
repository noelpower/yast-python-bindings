from ycp import List, String, Integer, Boolean, Float, Value
from ycp import Term as YCPTerm

import time

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
# placeholder for proper logging function
# currently just dumps to stderr (should 
# however write to yast log file)
def y2debug(msg):
    print msg

# placeholder for Buildins.foreach
def foreach(listOrMap):
    try:
        iterator = iter(listOrMap)
    except:
        y2error("%s is not iterable %s"%type(listOrMap))
        return None
    return listOrMap

def convert_to_ycp(pyvalue):
    if isinstance(pyvalue, Value):
        return pyvalue
    elif isinstance(pyvalue, int):
        return Integer(pyvalue)
    elif isinstance(pyvalue, str):
        return String(pyvalue)
    elif isinstance(pyvalue, list):
        l = List()
        for item in key:
            l.add(convert_to_ycp(item))
        return l
    elif isinstance(pyvalue, dict):
        m = Map()
        for key, value in pyvalue:
            m.add(convert_to_ycp(key), convert_to_ycp(value))
        return m
    elif isinstance(pyvalue, float):
        f = Float(pyvalue)
        return f
    raise NotImplementedError()

# add — Add a key/value pair to a map or list
def add(listOrMap, key, value=None):
    if isinstance(listOrMap, dict):
        listOrMap[key] = value
    elif isinstance(listOrMap, List):
         ycpvalue = convert_to_ycp(key)
         listOrMap.add(ycpvalue)
    else: # assume list
        listOrMap.append(key)
    # should we clone the listOrMap here ?
    return listOrMap

def size(listMapOrTerm):
    if isinstance(listMapOrTerm, Term):
        return listMapOrTerm.size()
    # assume list or map 
    return len(listMapOrTerm)

def sleep(millisecs):
    time.sleep(millisecs/1000)
