class Article:
    def __init__(self, reference, designation, prix_ht, stock):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    def ajouter_stock(self, quantite: int):
        if quantite < 0:
            raise ValueError("La quantité ajoutée ne peut pas être négative.")
        self.stock += quantite

    def __str__(self):
        return f"[{self.reference}] {self.designation} - Stock: {self.stock} - Prix HT: {self.prix_ht:.2f}€"


a1 = Article("REF-001", "Clavier Mécanique", 89.99, 10)
print(a1)
a1.ajouter_stock(5)
print(a1)