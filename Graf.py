import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

front = pd.read_csv('fronteras.csv')
front["Date"] = pd.to_datetime(front["Date"], format="%m/%d/%Y")
is_usa = front["Border"] == "US-Canada Border"
is_2019 = front["Date"].dt.strftime("%Y") == "2019"
frame1 = front[is_2019 & is_usa]
frame2 = frame1[["Port Name","State","Date","Measure","Value"]]
is_per = frame1["Measure"] == "Personal Vehicles"
is_perve = frame1["Measure"] == "Personal Vehicles"
is_ped = frame1["Measure"] == "Pedestrians"
is_bus = frame1["Measure"] == "Bus Passengers"
st1 = frame1["State"] == "MN"
st2 = frame1["State"] == "NY"
st3 = frame1["State"] == "ME"
st4 = frame1["State"] == "AK"
st5 = frame1["State"] == "VT"
st6 = frame1["State"] == "ID"
st7 = frame1["State"] == "WA"
st8 = frame1["State"] == "ND"
st9 = frame1["State"] == "MI"
st10 = frame1["State"] == "MT"

###################EJERCICIO 1######################
ejer1_est1 = front[is_usa & is_2019 & is_per & st1]
ejer1_est2 = front[is_usa & is_2019 & is_per & st2]
ejer1_est3 = front[is_usa & is_2019 & is_per & st3]
ejer1_est4 = front[is_usa & is_2019 & is_per & st4]
ejer1_est5 = front[is_usa & is_2019 & is_per & st5]
ejer1_est6 = front[is_usa & is_2019 & is_per & st6]
ejer1_est7 = front[is_usa & is_2019 & is_per & st7]
ejer1_est8 = front[is_usa & is_2019 & is_per & st8]
ejer1_est9 = front[is_usa & is_2019 & is_per & st9]
ejer1_est10 = front[is_usa & is_2019 & is_per & st10]

#####SOLO CAMBIAMOS EL ESTADO######
##x1 = ejer1_est1["Date"]
##y1 = ejer1_est1["Value"]
##plt.plot(x1,y1)
##plt.show()

###################EJERCICIO 2######################

ejer2_est1 = front[is_usa & is_2019 & is_ped & st1]
ejer2_est2 = front[is_usa & is_2019 & is_ped & st2]
ejer2_est3 = front[is_usa & is_2019 & is_ped & st3]
ejer2_est4 = front[is_usa & is_2019 & is_ped & st4]
ejer2_est5 = front[is_usa & is_2019 & is_ped & st5]
ejer2_est6 = front[is_usa & is_2019 & is_ped & st6]
ejer2_est7 = front[is_usa & is_2019 & is_ped & st7]
ejer2_est8 = front[is_usa & is_2019 & is_ped & st8]
ejer2_est9 = front[is_usa & is_2019 & is_ped & st9]
ejer2_est10 = front[is_usa & is_2019 & is_ped & st10]

#####SOLO CAMBIAMOS ESTADO#####
x = ejer2_est10["Port Name"]
y = ejer2_est10["Value"]
##plt.scatter(x,y)
##plt.show()

###################EJERCICIO 3######################

ejer3_est1 = front[is_usa & is_2019 & is_perve & st1]
ejer3_est2 = front[is_usa & is_2019 & is_perve & st2]
ejer3_est3 = front[is_usa & is_2019 & is_perve & st3]
ejer3_est4 = front[is_usa & is_2019 & is_perve & st4]
ejer3_est5 = front[is_usa & is_2019 & is_perve & st5]
ejer3_est6 = front[is_usa & is_2019 & is_perve & st6]
ejer3_est7 = front[is_usa & is_2019 & is_perve & st7]
ejer3_est8 = front[is_usa & is_2019 & is_perve & st8]
ejer3_est9 = front[is_usa & is_2019 & is_perve & st9]
ejer3_est10 = front[is_usa & is_2019 & is_perve & st10]

#####SOLO CAMBIAMOS ESTADO#####
pv = pd.DataFrame(ejer1_est10)
pvp = pd.DataFrame(ejer3_est10)
sumapv = pv.groupby("Port Name")["Value"].sum()
sumapvp = pv.groupby("Port Name")["Value"].sum()
dfsumapv = pd.DataFrame(sumapv)
dfsumapvp = pd.DataFrame(sumapvp)

juntos_est = pd.merge(dfsumapv,dfsumapvp,on = "Port Name")
dfjuntos = pd.DataFrame(juntos_est)
dfjuntox = dfjuntos[["Value_x", "Value_y"]]
##dfjuntox.plot.bar()
##plt.show()


###################EJERCICIO 4######################

##ejer4 = front[is_usa & is_2019 & is_bus]
##ejer4["Value"].plot.hist()
##plt.show()