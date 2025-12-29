# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 11:35:04 2023

@author: yyyyyyyyyyyyyyyyyyyy
"""



listtt= [['This', 'Ġthey', 0.732122004032135], ['Ġrisk', 'Ġseverity', 0.6583743095397949], ['Ġconcept', 'Ġseverity', 0.7150330543518066], ['Ġfee', 'Ġlandlord', 0.604739248752594]]
listt= [['This', 'Ġthey', 667.1293334960938], ['Ġrisk', 'Ġseverity', 497.2007141113281], ['Ġconcept', 'Ġseverity', 544.39794921875], ['Ġfee', 'Ġchance', 438.0860290527344]]

def trye(listt):
    new_list=[]
    new_list2=[]
    final=[]

    for item in listt:
        new_list.append(item[2])
        new_list2.append([listt[0],listt[1]])

    dog=sorted(new_list)
    for d in dog:
        for i in listt:
            if d==i[2]:
                final.append(i)
    return final


doggy=trye(listtt)   
doggy2=trye(listt)

print(doggy)
#700:66
print(doggy2)


    