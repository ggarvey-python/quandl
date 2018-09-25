import quandl
import pandas as pd

df = quandl.get("FMAC/HPI_TX")

states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

abrev_states = []

for abreviation in states[0][1]:
    abrev_states.append(abreviation)
    
abrev_states.remove('Abbreviations')

for state in abrev_states:
    
    print("FMAC/HPI_{}".format(str(state)))

#print(states)
#print(df)
