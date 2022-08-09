import pandas as pd
df = pd.read_csv('final_data.csv')

df.head()
df.columns()
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
radius_star = df['Radius'].to_list()
mass_star = df['Mass'].to_list()
gravity =[]

#converting solar mass and radius into km & kg
def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius_star[i] = radius[i]*6.957e+8
        mass_star[i] = mass[i]*1.989e+30
        
convert_to_si(radius_star,mass_star)

def gravity_calc(radius_star,mass_star):
    G = 6.674e-11
    for index in range(0,len(mass_star)):
        g= (mass_star[index]*G)/((radius_star[index])**2)
        gravity.append(g)
        
gravity_calc(radius_star,mass_star)

df["Gravity"] = gravity
df.dtypes
print(gravity_calc)