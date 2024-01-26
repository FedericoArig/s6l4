from matplotlib import pyplot as plt 
import pandas as pd 

file_name = "stockdata.csv"

dataset = pd.read_csv(file_name)#,names=["MSFT"])

index_values= dataset.index

#print(index_values)

#df = pd.DataFrame(index="MSFT")

print(dataset.loc[:,"MSFT"])

#qui ho creato un sottoinsieme del dataset iniziale.
#ho creato una serie con le due colonne interessate. 
#e inserite dentro una funzione .loc
subset = dataset.loc[:,["MSFT","Date"]]

rows = subset.head()

print(rows)

#ho selezionato le prime 5 righe del dataset tramite la funzione .head()
x_values = subset["Date"].head()
y_values = subset["MSFT"].head()

plt.plot(x_values,y_values)
plt.xlabel("Date")
plt.ylabel("MSFT")
plt.title("prime 5 righe")
plt.show()
#ho selezionato le ultime 5 righe del data set tramite la funzione .tail()
x_values = subset["Date"].tail()
y_values = subset["MSFT"].tail()

plt.plot(x_values,y_values)
plt.xlabel("Date")
plt.ylabel("MSFT")
plt.title("ultime 5 righe")
plt.show()

dataset2= dataset.loc[:,["AAPL","Date"]]
rows_20= dataset2.iloc[:20]
x_values2= rows_20["Date"]
y_values2= rows_20["AAPL"]
plt.plot(x_values2,y_values2,linestyle="--",marker="o",color="#FF0000", linewidth = 2)
plt.xlabel("Data")
plt.ylabel("Valore")
plt.show()

dataset3 = dataset.iloc[:, :-1]
date3 = dataset.iloc[:,-1:]
#prendo tutte le colonne e le righe tranne l'ultima

#definisco la y con la colonna date

#metto su grafico

x_values3 = date3["Date"]
y_values3 = dataset3
plt.plot(x_values3,y_values3,linestyle="-",color="#FF0000", linewidth = 1)
plt.xlabel("Data")
plt.ylabel("Azioni")
plt.show()

colori = ['blue', 'red', 'green', 'orange', 'purple']  # Aggiungi altri colori se necessario

# Traccia ogni azione separatamente con un colore diverso
for i, colonna in enumerate(dataset3.columns):
    plt.plot(date3["Date"], dataset3[colonna], linestyle="-", color=colori[i], linewidth=1, label=colonna)

plt.xlabel("Data")
plt.ylabel("Azioni")
plt.title("Andamento delle Azioni")
plt.legend()  # Aggiungi la legenda
plt.show()


