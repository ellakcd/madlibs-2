import webbrowser
from sys import argv

search_term = " ".join(argv[1:])
webbrowser.open_new_tab("https://www.google.com/search?q="+search_term)
