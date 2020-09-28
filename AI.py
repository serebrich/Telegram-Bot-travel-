from wit import Wit

AI = Wit(TOKEN)

def question(message):
    ans = AI.message(message)
    return ans['entities']['intent'][0]['value']
