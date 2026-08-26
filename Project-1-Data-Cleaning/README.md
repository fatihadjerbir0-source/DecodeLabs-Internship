 Dataset chargé : 1200 lignes, 14 colonnes
 Colonnes : ['OrderID', 'Date', 'CustomerID', 'Product', 'Quantity', 'UnitPrice', 'ShippingAddress', 'PaymentMethod', 'OrderStatus', 'TrackingNumber', 'ItemsInCart', 'CouponCode', 'ReferralSource', 'TotalPrice']

 Valeurs manquantes par colonne :
    - CouponCode : 309 valeurs manquantes (25.8%)
    -> CouponCode manquant interprété comme 'pas de coupon' : 309 valeurs remplacées par 'No Coupon'

Vérification des doublons :
    - Lignes 100% identiques supprimées : 0
    - Doublons sur la clé OrderID supprimés : 0

 Vérification du format des dates :
    - Dates non convertibles en date valide : 0
    - Lignes supprimées car date invalide : 0
    - Dates dans le futur détectées : 0
    - Plage de dates finale : 2023-01-01 -> 2025-06-30

 Nettoyage des espaces dans les colonnes texte :
    - Colonnes texte traitées : ['OrderID', 'CustomerID', 'Product', 'ShippingAddress', 'PaymentMethod', 'OrderStatus', 'TrackingNumber', 'CouponCode', 'ReferralSource']
    - Valeurs modifiées (espaces superflus retirés) : 0

 Vérification des types numériques (Quantity, UnitPrice) :
    - Quantity : 0 valeurs non numériques converties en NaN
    - UnitPrice : 0 valeurs non numériques converties en NaN
    - Lignes supprimées (Quantity/UnitPrice invalides) : 0
    - Quantity <= 0 détectées : 0
    - UnitPrice <= 0 détectées : 0
    - Lignes restantes après filtrage : 1200

 Vérification de TotalPrice = Quantity x UnitPrice :
    - Incohérences détectées entre TotalPrice existant et le calcul : 0
    - TotalPrice recalculé pour toutes les lignes (garantit la cohérence)

============================================================
RÉSUMÉ : 1200 lignes au départ -> 1200 lignes après nettoyage
Fichier sauvegardé : Cleaned_Dataset.xlsx
============================================================
