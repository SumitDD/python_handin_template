import numpy as np
import matplotlib.pyplot as plt
import json

# Exercise 1.1 and 1.2

bef_stats_df = np.genfromtxt(
    "/home/jovyan/data/befkbhalderstatkode.csv", delimiter=",", dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave',
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst',
          10: 'Amager Vest', 99: 'Udenfor'}


def file_to_numpy():

    print(type(bef_stats_df), ' of size: ', bef_stats_df.size)
    print('The skip_header=1 means that we have only the data\n\nfirst line:\n',
          bef_stats_df[0], '\nlast line\n', bef_stats_df[len(bef_stats_df)-1])


# Exercise 1.3
newDict = {}


def count_people_city():

    for n in neighb:

        mask = (bef_stats_df[:, 1] == n) & (bef_stats_df[:, 0] == 2015)
        sum = np.sum(bef_stats_df[mask][:, 4])
        print(neighb.get(n))
        print(sum)
        newDict.update({n: sum})


# Exercise 1.4

def getBarWithPubInCity():
    sortedDict = {k: v for k, v in sorted(
        newDict.items(), key=lambda item: item[1])}
    for n in sortedDict:
        plt.bar([neighb.get(n)], [sortedDict.get(n)],
                width=0.5, align="center")
        plt.xticks(rotation=45, horizontalalignment="right",
                   fontweight="light")

# Exercise 1.5


def above65years():
    mask = (bef_stats_df[:, 0] == 2015) & (
        bef_stats_df[:, 2] > 65) & (bef_stats_df[:, 1] != 99)
    print('sum of all the pople above 65 years old\n',
          np.sum(bef_stats_df[mask][:, 4]))

# Exercise 1.6


def above65years_notfromnordicCountries():
    mask = (bef_stats_df[:, 0] == 2015) & (
        bef_stats_df[:, 2] > 65) & (bef_stats_df[:, 3] == 5101) & (bef_stats_df[:, 3] == 5104) & (bef_stats_df[:, 3] == 5110) & (bef_stats_df[:, 3] == 5120) & (bef_stats_df[:, 3] == 5106)
    print('sum of all the pople above 65 years old and not from nordic countries\n',
          np.sum(bef_stats_df[mask][:, 4]))

# Exercise 1.7


def line_plot_østerbro_and_vesterbro():
    vesterbro_dict = {}
    østerbro_dict = {}
    listOfYears = list(np.unique(bef_stats_df[:, 0]))

    for y in listOfYears:
        mask = (bef_stats_df[:, 0] == y) & (bef_stats_df[:, 1] == 4)
        sum = np.sum(bef_stats_df[mask][:, 4])
        vesterbro_dict.update({y: sum})

    for y in listOfYears:
        mask = (bef_stats_df[:, 0] == y) & (bef_stats_df[:, 1] == 2)
        sum = np.sum(bef_stats_df[mask][:, 4])
        østerbro_dict.update({y: sum})

    values_vesterbro = list(vesterbro_dict.values())
    values_østerbro = list(østerbro_dict.values())

    plt.title('Udviklingen i Østerbro og Vesterbro gennem årene')
    plt.xlabel("Årstal")
    plt.ylabel('Befolkningstal')
    plt.plot(listOfYears, values_vesterbro, label='Vesterbro')
    plt.plot(listOfYears, values_østerbro, label='Østerbro')
    plt.legend()
    plt.show()
