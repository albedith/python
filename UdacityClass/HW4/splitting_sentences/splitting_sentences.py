'''
Created on Feb 20, 2014

@author: albedith
'''
def split_string(source, splitlist):
    """
    divides the source string by the
    characters in the splitlist and
    returns a list with each divided string.
    """
    split_list = []
    content_list = []
    content = source

    #convert splitlist into a list split_list
    i = 0
    while i < len(splitlist):
        split_list.append(splitlist[i])
        i += 1

    #divides the source string by the characters in the split_list
    j = 0
    while j < len(content):
        if content[j] in split_list:
            if (content[:j] != "") and (content[:j] not in split_list):
                content_list.append(content[:j])
                content = content[j:]
                j = -1
            elif (j+1) < len(content):
                content = content[j+1:]
                j = -1
        j += 1

    if len(content)> 1 and (content[:j] not in split_list):
        content_list.append(content[:j])

    return content_list


