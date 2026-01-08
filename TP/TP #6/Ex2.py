stock = [('Pommes', 10), ('Carottes', 5), ('Radis', 23), ('Lentilles', 534), ('Poivrons', 12)]

def maj_inventaire(stock,produit,n):
    for i in range(len(stock)):
        if stock[i][0] == produit:
            tmp = stock[i][1]
            if tmp - n < 0:
                raise ValueError
            stock[i] = (produit, tmp - n)
            return 
    raise IndexError

def achat(stock,produit,n):
    try:
        maj_inventaire(stock, produit, n)
        print('Merci pour votre achat.')
    except ValueError:
        print('Produit en quantité insuffisante.')
    except IndexError:
        print('Produit inexistant.')

achat(stock,'Carottes',1)
print(stock)

