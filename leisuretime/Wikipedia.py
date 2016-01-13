from pattern.web import Wikipedia, plaintext, WikipediaArticle
from pattern.web import SEARCH




def descarga(titulo):
    engine = Wikipedia(language="en")
    result= engine.search(titulo, type=SEARCH)
    return repr(plaintext(result.string))

        
from pattern.web import Wikipedia, WikipediaArticle
def wiki(titulo):
    article = Wikipedia(language="en").search(query=titulo)
    result=[]
    if article:
        for section in article.sections:
            result.append(section.title+"\n"+section.string+"\n")
            for link in section.links:
                result.append(link+"\n")

    return result
        
    