#Une fonction prenant trois notes et renvoyant la moyenne
def ft_moyenne(a, b, c):
    return (a + b + c)//3

#Une fonction prenant trois notes et renvoyant True si la moyenne est supérieure à 10.
def ft_check_moyenne(a, b, c):
    return ft_moyenne(a, b, c) > 10
    
#Une fonction prenant deux flottants et renvoyant True s’ils sont presques égaux (à 10−2 près)s
def ft_moyenne_float(a, b):
    return a >= 0.01 and a <= 0.02 and b >= 0.01 and b <= 0.02 
    