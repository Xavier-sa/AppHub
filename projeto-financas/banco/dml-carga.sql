INSERT INTO `cadastro` (`id`, `user_id`, `salario`, `despesa`, `investimentos`, `rendaextra`, `veiculos`, `gasolina`, `cursos`) VALUES
(1, 1, 3000, 2000, 1000, 500, 2, 300, 1000),
(2, 2, 4500, 1500, 2500, 600, 1, 400, 2000),
(3, 3, 3200, 1800, 1500, 700, 3, 350, 1500),
(4, 4, 5000, 2200, 3000, 900, 2, 450, 1200),
(5, 5, 2800, 2100, 1200, 400, 2, 280, 1300),
(6, 6, 4000, 1800, 2200, 600, 4, 500, 1100),
(7, 7, 3500, 1700, 1700, 800, 1, 450, 1800),
(8, 8, 2800, 1600, 1300, 500, 3, 350, 900),
(9, 9, 4900, 2500, 3500, 1000, 2, 600, 2000),
(10, 10, 6000, 3000, 4000, 1100, 1, 700, 2500);

INSERT INTO `metas` (`id`, `user_id`, `nome_meta`, `valor_total`, `valor_atual`, `status`) VALUES
(1, 1, 'Comprar um carro', 20000.00, 5000.00, 'Em andamento'),
(2, 2, 'Viajar para Europa', 15000.00, 3000.00, 'Em andamento'),
(3, 3, 'Comprar uma casa', 100000.00, 20000.00, 'Em andamento'),
(4, 4, 'Abrir um negócio', 30000.00, 8000.00, 'Em andamento'),
(5, 5, 'Estudar no exterior', 20000.00, 5000.00, 'Em andamento'),
(6, 6, 'Comprar um apartamento', 80000.00, 15000.00, 'Em andamento'),
(7, 7, 'Investir em ações', 10000.00, 2000.00, 'Em andamento'),
(8, 8, 'Viajar para o Japão', 25000.00, 7000.00, 'Em andamento'),
(9, 9, 'Concluir curso de pós-graduação', 5000.00, 1000.00, 'Em andamento'),
(10, 10, 'Comprar um terreno', 60000.00, 12000.00, 'Em andamento');

INSERT INTO `progresso` (`id`, `meta_id`, `valor_adicionado`, `data`) VALUES
(1, 1, 1000.00, '2025-01-10'),
(2, 1, 1500.00, '2025-02-15'),
(3, 2, 500.00, '2025-01-20'),
(4, 2, 800.00, '2025-02-18'),
(5, 3, 4000.00, '2025-01-12'),
(6, 3, 5000.00, '2025-02-10'),
(7, 4, 2000.00, '2025-01-05'),
(8, 4, 3000.00, '2025-02-25'),
(9, 5, 1500.00, '2025-01-15'),
(10, 5, 2500.00, '2025-02-10');

INSERT INTO `status_info` (`id`, `life`, `ki`, `forca`, `user_id`) VALUES
(1, 100, 10, 50, 1),
(2, 200, 20, 60, 2),
(3, 150, 15, 55, 3),
(4, 180, 18, 70, 4),
(5, 120, 12, 65, 5),
(6, 220, 22, 80, 6),
(7, 250, 25, 90, 7),
(8, 160, 16, 75, 8),
(9, 130, 13, 45, 9),
(10, 210, 21, 85, 10);

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'xavier', '1234'),
(2, 'wellington', 'abcd'),
(3, 'santos', 'password'),
(4, 'ana', 'mypassword'),
(5, 'bruno', 'qwerty'),
(6, 'clara', '123456'),
(7, 'daniel', 'senha123'),
(8, 'eduardo', 'letmein'),
(9, 'fernanda', 'iloveu'),
(10, 'guilherme', 'admin123');
