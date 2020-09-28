from wit import Wit

AI = Wit('DR7A5NXCWLHMYX6BIJ2XIFJWQRODTOHM')

def question(message):
    ans = AI.message(message)
    return ans['entities']['intent'][0]['value']