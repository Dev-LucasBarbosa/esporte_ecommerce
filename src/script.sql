-- Primeiro, limpar dados existentes para evitar conflitos
DELETE FROM carts_cartproduct;
DELETE FROM orders_order;
DELETE FROM carts_cart;
DELETE FROM products_productimage;
DELETE FROM products_product;
DELETE FROM categories_category;
DELETE FROM tags_tag_products;
DELETE FROM tags_tag;
DELETE FROM accounts_user;

-- Inserir categorias
INSERT INTO categories_category (id, name, slug, image, description, active, timestamp) VALUES
(1, 'Calçados', 'calcados', 'categories/calcados.jpg', 'Categoria de calçados', TRUE, (NOW())),
(2, 'Roupas', 'roupas', 'categories/roupas.jpg', 'Categoria de roupas', TRUE, (NOW())),
(3, 'Acessórios', 'acessorios', 'categories/acessorios.jpg', 'Categoria de acessórios', TRUE, (NOW())),
(4, 'Eletrônicos', 'eletronicos', 'categories/eletronicos.jpg', 'Categoria de eletrônicos', TRUE, (NOW()));

-- Inserir produtos
INSERT INTO products_product (id, title, slug, description, price, discount_price, stock, sku, featured, active, timestamp, updated, category_id) VALUES
(1, 'Tênis Esportivo', 'tenis-esportivo', 'Tênis confortável e durável.', 199.99, 149.99, 50, 'SKU001', TRUE, TRUE, (NOW()), (NOW()), 1),
(2, 'Camiseta Casual', 'camiseta-casual', 'Camiseta ideal para o dia a dia.', 79.99, 59.99, 100, 'SKU002', FALSE, TRUE, (NOW()), (NOW()), 2),
(3, 'Jaqueta de Couro', 'jaqueta-de-couro', 'Jaqueta de couro premium.', 499.99, 399.99, 20, 'SKU003', TRUE, TRUE, (NOW()), (NOW()), 2),
(4, 'Smartphone Android', 'smartphone-android', 'Smartphone de alta performance.', 2499.99, 2199.99, 80, 'SKU006', TRUE, TRUE, (NOW()), (NOW()), 4),
(5, 'Fone de Ouvido Bluetooth', 'fone-de-ouvido-bluetooth', 'Som de alta qualidade sem fio.', 399.99, 349.99, 40, 'SKU011', FALSE, TRUE, (NOW()), (NOW()), 4),
(6, 'Óculos de Sol', 'oculos-de-sol', 'Proteção UV com estilo.', 199.99, 179.99, 45, 'SKU012', FALSE, TRUE, (NOW()), (NOW()), 3),
(7, 'Smartwatch Fitness', 'smartwatch-fitness', 'Monitore suas atividades.', 599.99, 499.99, 35, 'SKU013', FALSE, TRUE, (NOW()), (NOW()), 4),
(8, 'Tênis de Corrida', 'tenis-de-corrida', 'Para corridas de alta performance.', 299.99, 259.99, 55, 'SKU014', FALSE, TRUE, (NOW()), (NOW()), 1);

-- Inserir imagens dos produtos
INSERT INTO products_productimage (id, product_id, image, alt_text, is_featured, "order", timestamp) VALUES
(1, 1, 'products/tenis-esportivo.jpg', 'Tênis esportivo', TRUE, 0, (NOW())),
(2, 2, 'products/camiseta-casual.jpg', 'Camiseta casual', TRUE, 0, (NOW())),
(3, 3, 'products/jaqueta-de-couro.jpg', 'Jaqueta de couro', TRUE, 0, (NOW())),
(4, 4, 'products/smartphone-android.jpg', 'Smartphone Android', TRUE, 0, (NOW())),
(5, 5, 'products/fone-de-ouvido-bluetooth.jpg', 'Fone de ouvido bluetooth', TRUE, 0, (NOW())),
(6, 6, 'products/oculos-de-sol.jpg', 'Óculos de sol', TRUE, 0, (NOW())),
(7, 7, 'products/smartwatch-fitness.jpg', 'Smartwatch fitness', TRUE, 0, (NOW())),
(8, 8, 'products/tenis-de-corrida.jpg', 'Tênis de corrida', TRUE, 0, (NOW()));

-- Inserir tags
INSERT INTO tags_tag (id, title, slug, active, timestamp) VALUES
(1, 'Esporte', 'esporte', TRUE, (NOW())),
(2, 'Casual', 'casual', TRUE, (NOW())),
(3, 'Tecnologia', 'tecnologia', TRUE, (NOW())),
(4, 'Conforto', 'conforto', TRUE, (NOW())),
(5, 'Moderno', 'moderno', TRUE, (NOW())),
(6, 'Premium', 'premium', TRUE, (NOW()));

-- Inserir usuários
INSERT INTO accounts_user (id, full_name, email, password, active, staff, admin, is_verified, timestamp) VALUES
(1, 'Admin User', 'admin@example.com', 'pbkdf2_sha256$320000$somehash', TRUE, TRUE, TRUE, TRUE, (NOW())),
(2, 'Guest User', 'guest@example.com', 'pbkdf2_sha256$320000$somehash', TRUE, FALSE, FALSE, FALSE, (NOW())),
(3, 'Test User', 'test@example.com', 'pbkdf2_sha256$320000$somehash', TRUE, FALSE, FALSE, TRUE, (NOW()));

-- Inserir carrinhos
INSERT INTO carts_cart (id, total, subtotal, timestamp, updated) VALUES
(1, 369.98, 349.98, (NOW()), (NOW())),
(2, 199.99, 189.99, (NOW()), (NOW())),
(3, 999.98, 949.98, (NOW()), (NOW()));

-- Inserir pedidos
INSERT INTO orders_order (id, order_id, status, shipping_total, total, active, billing_profile_id, cart_id, billing_address_id, shipping_address_id) VALUES
(1, 'ORD001', 'completed', 20.00, 369.98, TRUE, NULL, 1, NULL, NULL),
(2, 'ORD002', 'pending', 10.00, 199.99, TRUE, NULL, 2, NULL, NULL),
(3, 'ORD003', 'shipped', 50.00, 999.98, TRUE, NULL, 3, NULL, NULL);

-- Associar produtos aos carrinhos
INSERT INTO carts_cartproduct (id, cart_id, product_id, quantity) VALUES
(1, 1, 1, 2),
(2, 1, 2, 1),
(3, 2, 3, 1),
(4, 3, 4, 1),
(5, 3, 6, 1);

-- Associar tags aos produtos
INSERT INTO tags_tag_products (id, tag_id, product_id) VALUES
(1, 1, 1),  -- Tênis Esportivo - Esporte
(2, 2, 2),  -- Camiseta Casual - Casual
(3, 3, 4),  -- Jaqueta de Couro - Tecnologia
(4, 4, 6),  -- Smartphone - Conforto
(5, 5, 8),  -- Óculos de Sol - Moderno
(6, 6, 7);  -- Smartwatch Fitness - Premium

