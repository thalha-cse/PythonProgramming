# This project is about colored text using python
# This project contains a module named as colorama and it has function Fore, Back, Style in it.

# This is module name as colorame
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Fore, Back, Style are the function of colorama
print(Fore.CYAN+Back.BLACK+"My self Elon Musk"+Fore.CYAN+Back.BLACK+" I'm Owner of Tesla, SpaceX")
print(Style.BRIGHT+"Hello! Users, How are you? ")
