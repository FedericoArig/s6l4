from matplotlib import pyplot as plt 
import pandas as pd 

file_name = "election.csv"

dataset = pd.read_csv(file_name)

somma_voti_candidato1 = dataset["Coderre"].sum()
somma_voti_candidato2 = dataset["Bergeron"].sum()
somma_voti_candidato3 = dataset["Joly"].sum()

candidati = ["Coderre", "Bergeron", "Joly"]
voti_totali = [somma_voti_candidato1, somma_voti_candidato2, somma_voti_candidato3]

plt.bar(candidati, voti_totali, color=['blue', 'green', 'red'])
plt.xlabel('Candidati')
plt.ylabel('Voti totali')
plt.title('Confronto voti totali dei tre candidati')
plt.show()
