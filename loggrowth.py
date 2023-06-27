import math

def main():
    print("This program calculates the log growth of a quantity.")
    print()

    val_euler = Euler()
    val_taylor = taylor()
    val_runge_kutta = runge_kutta(0.05, 10.0)
    print("val_taylor = " , val_taylor, " |\nval_euler", val_euler, "| \nval_runge_kutta", val_runge_kutta)
 
 

def runge_kutta(h, t_final):
    # Valor inicial
    t = 0
    P = 10

    # Lista para armazenar os valores de t e P(t)
    t_values = [t]
    P_values = [P]

    while t < t_final:
        # Cálculo dos coeficientes k1, k2, k3 e k4
        k1 = h * (100 * math.exp(t) * (9 + math.exp(t)) - 100 * math.exp(t) * math.exp(t)) / (9 + math.exp(t)) ** 2
        k2 = h * (100 * math.exp(t + h/2) * (9 + math.exp(t + h/2)) - 100 * math.exp(t + h/2) * math.exp(t + h/2)) / (9 + math.exp(t + h/2)) ** 2
        k3 = h * (100 * math.exp(t + h/2) * (9 + math.exp(t + h/2)) - 100 * math.exp(t + h/2) * math.exp(t + h/2)) / (9 + math.exp(t + h/2)) ** 2
        k4 = h * (100 * math.exp(t + h) * (9 + math.exp(t + h)) - 100 * math.exp(t + h) * math.exp(t + h)) / (9 + math.exp(t + h)) ** 2

        # Atualização de t e P(t)
        t += h
        P += (k1 + 2*k2 + 2*k3 + k4) / 6

        # Armazenamento dos valores de t e P(t)
        t_values.append(t)
        P_values.append(P)

    return P

   
def taylor():
    r = 1.0
    h = 0.00001
    t = 1.0
    tf = 10.0
    i = 1.0
    valor = 0.0
    e = math.exp(1)
    while t <= tf:
        valor = 100*math.exp(t)/(9 + math.exp(t)) + (900-99*math.exp(t))/(81+19*math.exp(t)) +((-8019*e**(t) - 1881*e**(2*t) - 17100*e**(t) + 1881*e**(2*t))/(6561+3078*e**t + 361*e**(2*t)))/2
        #i+= 1
        #print("t = ", t, "valor = ", valor)
        
        t = t+h
    return valor 

    ## Get the initial and final quantities
    #initial = float(input("Enter the initial quantity: "))
    #final = float(input("Enter the final quantity: "))

    # Calculate the log growth
    #growth = math.log(final / initial)

    # Print the result
    #print("The log growth is", growth)

def Euler():
    r = 1.0
    h = 0.00001
    t = 1.0
    tf = 10.0
    i = 1.0
    valor = 0.0
    #vf = 0
    while t <= tf:
        valor = (100*math.exp(t)/(9 + math.exp(t))) + (900-99*math.exp(t))/(81+19*math.exp(t))
        #i+= 1
        #print("t = ", t, "valor = ", valor)
        
        t = t+h
    return valor

    ## Get the initial and final quantities
    #initial = float(input("Enter the initial quantity: "))
    #final = float(input("Enter the final quantity: "))

    # Calculate the log growth
    #growth = math.log(final / initial)

    # Print the result
    #print("The log growth is", growth)
    
    
main()