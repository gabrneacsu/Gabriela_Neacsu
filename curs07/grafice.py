import matplotlib.pyplot as plot
import pandas as pd

# grafic de tip linie
# data = {'An': [2010, 2011, 2012, 2013, 2014],
#         'Vanzari': [500, 600, 750, 500, 800]}
#
# df = pd.DataFrame(data)
# df.plot(x='An', y='Vanzari', marker='o', linestyle='--', color='b', label='Vanzari')
# plot.xlabel('An')
# plot.ylabel('Vanzari')
# plot.title('Grafic linie - Vanzari in functie de An')
# plot.legend()
# plot.grid()
# plot.show()

# grafic de tip histograma - rol de analiza distributia datelor
# data = {'Varsta': [25, 30, 35, 40, 45, 50, 30, 55, 60]}
# df = pd.DataFrame(data)
# df['Varsta'].hist(bins=3, color='skyblue', edgecolor='black') #bins=5 este nr de valori pe care le vreau in histograma
# plot.xlabel('Varsta')
# plot.ylabel('Frecventa')
# plot.title('Distributia varstei')
# plot.show()
# # histograma utila cand trebuie sa vedem distributia valorilor pe intervale


data = {'An': [2010, 2011, 2012, 2013, 2014],
        'Vanzari': [500, 600, 750, 500, 800]}
df = pd.DataFrame(data)
fig, axs = plot.subplots(nrows=2, ncols=2, figsize=(10, 8))
df.plot(x='An', y='Vanzari', ax=axs[0, 0], marker='o', linestyle='-', color='r', label='Vanzari')
axs[0, 0].set_title('Grafic linie - Vanzari')
df.plot.bar(x='An', y='Vanzari',ax=axs[0, 1], color='g', alpha=0.7, label='Vanzari(bara') #alpha = dimensiunea liniutei
axs[0, 1].set_title('Grafic bara - Vanzari')
axs[1, 0].set_visible(False)
axs[1, 1].set_visible(False)
plot.show()

# fisierele tip pandas sunt DataFrames (mai util la filtrare si sortare)
# fisiere tip text: .xtx, .csv, .tsv

# virtual enviroment are rolul de a ne lasa sa instalam pachetele doar la nivelul la care lucram

# pip list in terminal pt a vedea ce avem instalat in venv