-- ============================================================================
-- Project 3 -- SQL Data Analysis (DecodeLabs Internship, Batch 2026)
-- Table analysee : orders  (chargee depuis Cleaned_Dataset.xlsx dans ecommerce.db)
-- ============================================================================


-- ============================================================
-- SECTION 1 : SELECT + WHERE + ORDER BY
-- ============================================================

-- TITLE: Toutes les commandes annulees, les plus recentes en premier
SELECT OrderID, Date, Product, TotalPrice, OrderStatus
FROM orders
WHERE OrderStatus = 'Cancelled'
ORDER BY Date DESC;

-- TITLE: Top 10 des commandes les plus cheres
SELECT OrderID, CustomerID, Product, Quantity, UnitPrice, TotalPrice
FROM orders
ORDER BY TotalPrice DESC
LIMIT 10;

-- TITLE: Commandes payees en Credit Card avec plus de 3 articles dans le panier
SELECT OrderID, Date, Product, ItemsInCart, PaymentMethod
FROM orders
WHERE PaymentMethod = 'Credit Card' AND ItemsInCart > 3
ORDER BY ItemsInCart DESC;


-- ============================================================
-- SECTION 2 : GROUP BY + Agregations (COUNT, SUM, AVG)
-- ============================================================

-- TITLE: Chiffre d'affaires, nombre de commandes et panier moyen par produit
SELECT
    Product,
    COUNT(*) AS nb_orders,
    SUM(TotalPrice) AS total_revenue,
    ROUND(AVG(TotalPrice), 2) AS avg_order_value
FROM orders
GROUP BY Product
ORDER BY total_revenue DESC;

-- TITLE: Nombre de commandes et CA par mode de paiement
SELECT
    PaymentMethod,
    COUNT(*) AS nb_orders,
    SUM(TotalPrice) AS total_revenue
FROM orders
GROUP BY PaymentMethod
ORDER BY nb_orders DESC;

-- TITLE: Repartition des commandes par statut
SELECT
    OrderStatus,
    COUNT(*) AS nb_orders,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM orders), 2) AS pct_of_orders
FROM orders
GROUP BY OrderStatus
ORDER BY nb_orders DESC;

-- TITLE: Panier moyen (ItemsInCart) et CA moyen par source de trafic
SELECT
    ReferralSource,
    COUNT(*) AS nb_orders,
    ROUND(AVG(ItemsInCart), 2) AS avg_items_in_cart,
    ROUND(AVG(TotalPrice), 2) AS avg_order_value
FROM orders
GROUP BY ReferralSource
ORDER BY avg_order_value DESC;


-- ============================================================
-- SECTION 3 : HAVING (filtrer des groupes deja agreges)
-- ============================================================

-- TITLE: Produits dont le CA total depasse 100 000
SELECT
    Product,
    COUNT(*) AS nb_orders,
    SUM(TotalPrice) AS total_revenue
FROM orders
GROUP BY Product
HAVING SUM(TotalPrice) > 100000
ORDER BY total_revenue DESC;

-- TITLE: Modes de paiement utilises dans plus de 200 commandes
SELECT
    PaymentMethod,
    COUNT(*) AS nb_orders
FROM orders
GROUP BY PaymentMethod
HAVING COUNT(*) > 200
ORDER BY nb_orders DESC;


-- ============================================================
-- SECTION 4 : L'ALIAS TRAP (comprendre l'ordre d'execution)
-- ============================================================

-- TITLE: [FAUX] Alias utilise dans WHERE -> erreur attendue
SELECT PaymentMethod, SUM(TotalPrice) AS total_revenue
FROM orders
WHERE total_revenue > 100000
GROUP BY PaymentMethod;

-- TITLE: [CORRECT] Meme filtre ecrit avec HAVING
SELECT PaymentMethod, SUM(TotalPrice) AS total_revenue
FROM orders
GROUP BY PaymentMethod
HAVING total_revenue > 100000;


-- ============================================================
-- SECTION 5 : Contribution en pourcentage
-- ============================================================

-- TITLE: Part en % de chaque produit dans le CA total
SELECT
    Product,
    SUM(TotalPrice) AS product_revenue,
    ROUND(100.0 * SUM(TotalPrice) / (SELECT SUM(TotalPrice) FROM orders), 2) AS pct_of_total_revenue
FROM orders
GROUP BY Product
ORDER BY pct_of_total_revenue DESC;


-- ============================================================
-- SECTION 6 : Tendance temporelle (bonus)
-- ============================================================

-- TITLE: CA total et nombre de commandes par annee
SELECT
    strftime('%Y', Date) AS year,
    COUNT(*) AS nb_orders,
    SUM(TotalPrice) AS total_revenue
FROM orders
GROUP BY year
ORDER BY year;