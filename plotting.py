import matplotlib.pyplot as mt
import india_plot
import saarc
import grouped_plot
import south_asia


def plotting():
    """
     - import all the files and plot it.
    """
    while(1):
        print("Enter your choice : ")
        print("1. India's population Vs years")
        print("2. South Asian Counties Population of 2014")
        print("3. SAARC Countries Population Vs year")
        print("4. Grouped bar graph of Asian Countries between year 2004-2014")
        print("5. Exit")
        choice = int(input())
        if(choice == 1):
            india_plot.indiapopulation()
            print("Loading...")
            mt.tight_layout()
            mt.show()
        if(choice == 2):
            south_asia.south()
            print("Loading...")
            mt.tight_layout()
            mt.show()
        if(choice == 3):
            saarc.saarc()
            print("Loading...")
            mt.tight_layout()
            mt.show()
        if(choice == 4):
            grouped_plot.grouped()
            print("Loading...")
            mt.tight_layout()
            mt.show()
        if(choice == 5):
            break
