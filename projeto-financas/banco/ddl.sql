CREATE database if not mau_mau;

-- Criação das tabelas
CREATE TABLE `cadastro` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `salario` int(11) DEFAULT NULL,
  `despesa` int(11) DEFAULT NULL,
  `investimentos` int(11) DEFAULT NULL,
  `rendaextra` int(11) DEFAULT NULL,
  `veiculos` int(11) DEFAULT NULL,
  `gasolina` int(11) DEFAULT NULL,
  `cursos` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `metas` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `nome_meta` varchar(255) NOT NULL,
  `valor_total` decimal(10,2) NOT NULL,
  `valor_atual` decimal(10,2) DEFAULT 0.00,
  `status` varchar(50) DEFAULT 'Em andamento'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `progresso` (
  `id` int(11) NOT NULL,
  `meta_id` int(11) NOT NULL,
  `valor_adicionado` decimal(10,2) NOT NULL,
  `data` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `status_info` (
  `id` int(11) NOT NULL,
  `life` int(11) NOT NULL,
  `ki` int(11) NOT NULL,
  `forca` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Índices
ALTER TABLE `cadastro`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

ALTER TABLE `metas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

ALTER TABLE `progresso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `meta_id` (`meta_id`);

ALTER TABLE `status_info`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

-- AUTO_INCREMENT
ALTER TABLE `cadastro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

ALTER TABLE `metas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `progresso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `status_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

-- Restrições (chaves estrangeiras)
ALTER TABLE `cadastro`
  ADD CONSTRAINT `cadastro_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

ALTER TABLE `metas`
  ADD CONSTRAINT `metas_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `progresso`
  ADD CONSTRAINT `progresso_ibfk_1` FOREIGN KEY (`meta_id`) REFERENCES `metas` (`id`);

ALTER TABLE `status_info`
  ADD CONSTRAINT `status_info_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
