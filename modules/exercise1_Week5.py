import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Exercise 5.A


def pctChange_divorcedDanes():

    url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&Tid=2008K1%2C2008K2%2C2008K3%2C2008K4%2C2020K1%2C2020K2%2C2020K3%2C2020K4&CIVILSTAND=F'
    dst = pd.read_csv(url, sep=";")

    list2008 = list(dst.iloc[0:4]['INDHOLD'])
    list2020 = list(dst.iloc[4:8]['INDHOLD'])

    pct_dif = (sum(list2020)/sum(list2008))/sum(list2008)*100
    print(pct_dif)


# Exercise 5.B

def biggestCities_NeverMarried():

    neverMarriedUrl = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=U&OMR%C3%85DE=*&Tid=2020K1'
    allStatusUrl = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&CIVILSTAND=*&Tid=2020K1'

    neverMarriedDst = pd.read_csv(neverMarriedUrl, sep=";")
    allStatusDst = pd.read_csv(allStatusUrl, sep=";")

    sorted_neverMarriedDst = neverMarriedDst.sort_values(
        by=["INDHOLD"], ascending=False)
    sorted_allStatus = allStatusDst.sort_values(
        by=["INDHOLD"], ascending=False)

    ugift_lst = list(sorted_neverMarriedDst.iloc[1:6]['INDHOLD'])
    alle_lst = list(allStatusDst.iloc[1:6]['INDHOLD'])

    pct_array = []

    for element in range(5):
        pct_diff = ugift_lst[element]/alle_lst[element]*100
        pct_array.append(pct_diff)

    area_lst = list(sorted_neverMarriedDst.iloc[1:6]['OMRÅDE'])
    myDict = dict(zip(area_lst, pct_array))

    sortedDict = {k: v for k, v in sorted(
        myDict.items(), key=lambda item: item[1], reverse=True)}

    print(sortedDict)

# Exercise 5.C


def barChart_NeverMarried():

    url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=G&ALDER=*&Tid=2020K1'
    dst = pd.read_csv(url, sep=";")
    dst.plot.bar(figsize=(30, 5), x='CIVILSTAND', y='INDHOLD')
    dst.plot.bar(figsize=(30, 5), x='TID', y='INDHOLD')

# Exercise 5.D


def barChart_MarriedAndNeverMarried():

    # Ex 5 D. Show 2 plots in same figure: 'Married' and 'Never Married' for all ages in DK in 2020
    # (Hint: x axis is age from 0-125, y axis is how many people in the 2 categories). Add lengend to show names on graphs
    url5 = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=G&Tid=2020K1&ALDER=*"
    dst4 = pd.read_csv(url5, sep=";")
    url6 = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&Tid=2020K1&ALDER=*&CIVILSTAND=U"
    dst5 = pd.read_csv(url6, sep=";")

    age_list = []
    for x in range(126):
        age_list.append(x)

    gift_list = list(dst4.iloc[1:]['INDHOLD'])
    ugift_list = list(dst5.iloc[1:]['INDHOLD'])

    plt.plot(age_list, gift_list, label="Gift")
    plt.plot(age_list, ugift_list, label="Ugift")
    plt.legend()
