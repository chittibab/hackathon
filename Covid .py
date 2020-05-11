import pandas as pd
import sys
import matplotlib.pyplot as plt
a=[]
b=[]
Death_growing_rate=[]
df=pd.read_excelr('C:\User\lenovo\Desktop\hackthon\times_series_covid_19_deaths.xlsx')
country_deaths=[list(row) for row in df.values]
for i in range(0,245):
    t1=0
    for j in range(1,76):
        t1=t1+country_deaths[i][j]
    a.append(t1)
#code death in different countries as a list
            
cr=pd.read_excel('C:\Users\lenovo\Desktop\hackthon\times_series_covid_19_recovered.xlsx')
country_recovered=[list(row) for row in cr.values]
for i in range(0,245):
    t2=0
    for j in range(3,76):
        t2=t2+country_recovered[i][j]
    b.append(t2)


#converting the whole csv data into a lists in list
df=pd.read_excel('C:\Users\lenovo\Desktop\hackthon\high_risk_countries_deaths.xlsx')
high_risk_countries_deaths=[list(row) for row in df.values]       
df=pd.read_excel('C:\Users\lenovo\Desktop\hackthon\high_risk_countries_recovered')
high_risk_countries_recovered=[list(row) for row in df.values]



#code recovered in different cases as  a list
print("1.Death_growing_rates of all countries \n2.death_growing_rate of countries more than 4% \n3.Death growing rate countries with 100% \n4.high_risk_countries_for which indian students go for study,internship etc.,")
m=int(input())

for i in range(0,245):
    if a[i]+b[i]==0:
        t=0
        Death_growing_rate.append(t)
    else:
        c=0
        c=(a[i]/(a[i]+b[i]))*100
        Death_growing_rate.append(c)



if m==1:
    for i in range(0,245):
        print(i+1,country_deaths[i][0],"\t",Death_growing_rate[i])  #prints death growing rate of all countries
       
elif m==2:
    for i in range(0,245):
        if Death_growing_rate[i]>=4 and Death_growing_rate[i]!=100: 
            print(country_recovered[i][0],' ',Death_growing_rate[i])

elif m==3:
    print('There are countries with 100%death growing rate in which there are 0 recovered patients')
    for i in range(0,245):
        if Death_growing_rate[i]==100:
            print(country_recovered[i][0],' ',Death_growing_rate[i])
    
elif m==4:
    print('press a number to know its corresponding graphical plot deaths vs recovered')
    print('press 0 to exit')
    for i in range(0,15):
        print(i+1,high_risk_countries_deaths[i][0])
    for i in range(0,15):
        g=int(input())
        if(g==1 or g==2 or g==3 or g==4 or g==5 or g==6 or g==7 or g==8 or g==9 or g==10 or g==11 or g==12 or g==13 or g==14 or g==15):
            popped_element1=high_risk_countries_deaths[g-1].pop(0)
            popped_element2=high_risk_countries_recovered[g-1].pop(0)
            plt.plot(high_risk_countries_deaths[g-1],high_risk_countries_recovered[g-1])
            plt.xlabel("high_risk_countries_deaths")
            plt.ylabel("high_risk_countries_recovered)")
            plt.show()
        
        elif g==0:
            sys.exit(g)
