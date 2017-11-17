from ycp import List, String, Integer, Boolean, Float, Value
from ycp import Term as YCPTerm

import time, inspect, os
from random import randint as pyrand_range

# returns the caller n frames back
def get_caller_loginfo(frames):
    frame = inspect.currentframe()
    for i in range(0, frames):
        frame = frame.f_back
    info = inspect.getframeinfo(frame)
    details = "%s:%s "%(os.path.basename(info[0]), info[1])
    return details

# placeholder for proper logging function
# currently just dumps to stderr (should
# however write to yast log file)
def y2milestone(*args):
    print get_caller_loginfo(2) + sformat(*args)

# placeholder for proper logging function
# currently just dumps to stderr (should
# however write to yast log file
def y2warning(*args):
    print get_caller_loginfo(2) + sformat(*args)

# placeholder for proper logging function
# currently just dumps to stderr (should
# however write to yast log file)
def y2error(*args):
    print get_caller_loginfo(2) + sformat(*args)

# placeholder for proper logging function
# currently just dumps to stderr (should 
# however write to yast log file)
def y2debug(*args):
    print get_caller_loginfo(2) + sformat(*args)

# placeholder for proper logging function
# currently just dumps to stderr (should 
# however write to yast log file)
def y2internal(*args):
    print get_caller_loginfo(2) + sformat(*args)

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
        for item in pyvalue:
            l.add(convert_to_ycp(item))
        return l
    elif isinstance(pyvalue, dict):
        m = Map()
        for key, value in pyvalue.iteritems():
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
    elif isinstance(listOrMap, List) or isinstance(listOrMap, YCPTerm):
         ycpvalue = convert_to_ycp(key)
         listOrMap.add(ycpvalue)
    else: # assume list
        listOrMap.append(key)
    # should we clone the listOrMap here ?
    return listOrMap

def size(listMapOrTerm):
    if isinstance(listMapOrTerm, YCPTerm):
        return listMapOrTerm.size()
    # assume list or map 
    return len(listMapOrTerm)

def sleep(millisecs):
    
    time.sleep(float(millisecs)/1000)

def tostring(val):
    try:
        return val.toString()
    except:
        return str(val)

def sformat(*pars):
    list_pars = list(pars)
    form = list_pars.pop(0)
    placeholders = ['%1', '%2', '%3', '%4', '%5', '%6', '%7', '%8', '%9', '%%']
    arg_positions = []
    for placeholder in placeholders:
        index = 0
        if placeholder in form:
            while True:
                index = form.find(placeholder, index)
                if index == -1:
                    break
                pos = form[index + 1]
       	        if pos != '%':
                    try:
                        # assume YCP value
                        arg_positions.append(pars[int(pos)].toString())
                    except:
                        arg_positions.append(pars[int(pos)])

                    form = form.replace(placeholder, '%s')
                index = index + 2
    if len(arg_positions):
        return form%tuple(arg_positions)
    return form 

def flatten(lists):
    newlist = []
    for l in lists:
        newlist = newlist + l
    return newlist

def union(list1, list2):
    return list(set().union(list1, list2))

def random(maxint):
    return pyrand_range(0, maxint)

def mergestring(listofstrings, glue):
    first = True
    result = None
    for item in listofstrings:
        if first:
            result = item
            first = False
        else:
            result = result + glue + item 
    return result
