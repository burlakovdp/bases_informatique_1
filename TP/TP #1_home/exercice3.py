def reduction(n):
    if n >= 10 and n < 50:
        return 10
    elif n >= 50:
        return 20
    else:
        return 0
    
def prix_livraison(prix):
    if prix * 0.1 <= 5:
        return 5
    elif prix * 0.1 >= 100:
        return 100
    else:
        return prix * 0.1
    
def facture(n, p):
    prix = n*p
    print('Prix : ', prix, '€')
    print('Reduction : -', reduction(prix), '%')
    print('Cout livraison : ', prix_livraison(prix), '€')
    print('----------------------')
    print('Prix total (dont livraison) :', prix - (prix * (reduction(prix) / 100)) + prix_livraison(prix), '€'
        )
    
assert reduction(10) == 10
assert reduction(9) == 0
assert reduction(50) == 20
assert reduction(1) == 0
assert reduction(111) == 20

assert prix_livraison(5) == 5
assert prix_livraison(100) == 10
assert prix_livraison(10) == 5
assert prix_livraison(2000) == 100
assert prix_livraison(60) == 6

