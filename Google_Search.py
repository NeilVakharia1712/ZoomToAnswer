from serpapi import GoogleSearch
import requests
import pyperclip
from Zoom_Control import openChat
def searchQuery(q):
    params = {
      "q": q,
      'location':'Evanston,Illinois',
      "hl": "en",
      "gl": "us",
      "device": "desktop",
      "api_key": "6c8dcdb60b2416c130acea4c86a035763e5869fe9e5eb44db66077985f512697"
    }

    client = GoogleSearch(params)
    results = client.get_dict()
    if 'answer_box' in results:
        res = results['answer_box']
        if 'result' in res:
            output = res['result']
        elif 'snippet' in res:
            output = res['snippet']
        elif 'definition' in res:
            output = res['definition']
        else:
            output = results['answer_box']
        pyperclip.copy(str(output))
        pyperclip.paste()
    elif 'knowledge_graph' in results:
        res = results['knowledge_graph']
        if 'title' in res:
            output = res['title']
        elif 'snippet' in res:
            output = res['snippet']
        else:
            output = results['knowledge_graph']
        pyperclip.copy(str(output))
        pyperclip.paste()
    else:
        found = False
        for i in results:
            if type(results[i]) == list:
                for k in range(len(results[i])):
                    if 'snippet' in results[i][k]:
                        output = results[i][k]['snippet'] + '  LINK AT:' + results[i][k]['link']
                        found = True
                        break
                if found:
                    break
        if not found:
            output = "NO VALID ANSWERS"
        pyperclip.copy(str(output))
        pyperclip.paste()

    openChat()


#searchQuery("what is the integral of sinx")