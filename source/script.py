import langchain
from random import choice
import main
from langchain import OpenAI

from langchain.prompts import PromptTemplate

def aaa(x):
    prompt = PromptTemplate.from_template('хочу борщ , {product}')
    templ = prompt.format(product=choice(x))
    return templ

    # llm = OpenAI(temperature=0.0)
    # return llm(templ)