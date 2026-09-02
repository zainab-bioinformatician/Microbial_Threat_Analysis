import os
import numpy as np
import matplotlib.pyplot as plt
labels=['Poison Speed','Hiding Power','Soil Survival','Medicine Failure']
# poison speed= How quickly the provided microbe affect 
# Hiding Power= immunity or avoidness from interferance
# soil survival= Wether the microbe can persist outside a host, especially in soil 
# Medicine failure= How strongly Antimicrobial resistance reduce effectiveness of treatment
a= float(input("Enter poison speed (0-100):"))
b= float(input("Enter Hiding Power (0-100):"))
c= float(input("Enter Soil Survival (0-100):"))
d= float(input("Enter Medicine failure (0-100):"))
num_vars= len(labels)
x= np.linspace(0,2* np.pi, num_vars,endpoint=False).tolist()

y=[a,b,c,d]
x +=x[:1]
y += y[:1]
# for round lines/circle figure
fig,ax=plt.subplots(figsize=(6,6),subplot_kw={'polar':True})
# for labels and directions
ax.set_theta_offset(np.pi/2)
ax.set_theta_direction(-1)
plt.xticks(x[:-1], labels,color='#2D2D2D',fontweight='bold',fontsize=10)
color='#FF6B6B'
ax.plot(x,y,color=color, linewidth=3, linestyle='solid')
for i, value in enumerate(y[:-1]):
    ax.text(x[i], value + 5, str(int(value)),
            ha='center', fontweight='bold')
ax.fill(x,y, color=color, alpha=0.3)
# for ring lables
ax.set_rlabel_position(0)
plt.yticks([25,50,75,100],['25','50','75',"100"],color='#A0A0A0',fontsize=8)
plt.ylim(0,100)
# giving name to the project
ax.set_title('MICROBIAL THREAT ANALYSIS',fontsize=12, fontweight='bold',pad=25)
os.makedirs('bio_data', exist_ok= True)
plt.savefig('bio_data/Microbial_Threat_chart.png', dpi=300)
print("zainab: congratulations your project is done!")