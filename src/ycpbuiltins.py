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


