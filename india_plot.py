import matplotlib.pyplot as mt
import solve


# this section is plotting bar graph of india's population Vs year.
def indiapopulation():
    mt.title("India's Population Over Years")
    mt.bar(solve.india.keys(), solve.india.values(), width=0.4)
    mt.xlabel("Year")
    mt.ylabel("Population in 10 lacks")
