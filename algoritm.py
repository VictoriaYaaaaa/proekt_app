def str_count(s):
    for simvol in set(s):
        count = 0
        for subsimvol in s:
            if simvol == subsimvol:
                count +=1
        print(simvol,count)
#str_count('hello word! abcda')

def str_count_2(s):
    simvols={}
    for simvol in s:
        simvols[simvol] = simvols.get(simvol,0) + 1
    for sim,count in simvols.items():
        print(sim,count)
str_count_2('hello word! abcda')
