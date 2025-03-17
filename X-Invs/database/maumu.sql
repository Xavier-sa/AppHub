-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 17/03/2025 às 17:54
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `mau_mau`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cadastro`
--

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

--
-- Despejando dados para a tabela `cadastro`
--

INSERT INTO `cadastro` (`id`, `user_id`, `salario`, `despesa`, `investimentos`, `rendaextra`, `veiculos`, `gasolina`, `cursos`) VALUES
(6, 14, 3000, 7000, 10, 2500, 47500, 1100, 5000),
(7, 15, 1000, 1000, 10000, 100, 2500, 500, 1000),
(8, 16, 4000, 4000, 40, 40, 40, 105, 10),
(9, 17, 10000, 1, 1, 1, 1, 1, 1),
(10, 18, 54, 1, 1, 1, 1, 1, 1),
(11, 19, 1, 1, 1, 1, 1, 1, 1),
(12, 20, 1, 1, 1, 1, 1, 1, 1),
(13, 21, 4500, 7000, 200, 1500, 20000, 600, 150),
(14, 23, 4500, 7000, 200, 2500, 20000, 700, 150),
(15, 24, 4500, 20000, 1, 1, 10000, 700, 30000),
(16, 25, 42000, 10000, 10000, 10000, 10000, 10000, 100000),
(17, 27, 1, 1, 1, 1, 1, 1, 1),
(18, 28, 1, 1, 1, 1, 1, 1, 1),
(19, 29, 1, 1, 1, 1, 1, 1, 1),
(20, 30, 1, 1, 1, 1, 1, 1, 1),
(21, 31, 1, 1, 1, 1, 1, 1, 1),
(22, 32, 12, 11, 1, 1, 1, 11, 1),
(23, 33, 1, 1, 1, 1, 1, 1, 1),
(24, 34, 1, 1, 11, 1, 1, 11, 1),
(25, 35, 1, 11, 1, 1, 11, 11, 1),
(26, 36, 12, 1, 11, 1, 1, 1, 1),
(27, 37, 1, 1, 1, 1, 11, 1, 1),
(28, 38, 11, 1, 1, 1, 1, 1, 1),
(29, 39, 1, 1, 1, 1, 1, 1, 1),
(30, 40, 123, 1, 3, 3, 32, 2, 2),
(31, 41, 2, 1, 1, 1, 1, 1, 1),
(32, 1, 11, 1, 1, 11, 1, 10, 11);

-- --------------------------------------------------------

--
-- Estrutura para tabela `metas`
--

CREATE TABLE `metas` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `nome_meta` varchar(255) NOT NULL,
  `valor_total` decimal(10,2) NOT NULL,
  `valor_atual` decimal(10,2) DEFAULT 0.00,
  `status` varchar(50) DEFAULT 'Em andamento'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `progresso`
--

CREATE TABLE `progresso` (
  `id` int(11) NOT NULL,
  `meta_id` int(11) NOT NULL,
  `valor_adicionado` decimal(10,2) NOT NULL,
  `data` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `status_info`
--

CREATE TABLE `status_info` (
  `id` int(11) NOT NULL,
  `life` int(11) NOT NULL,
  `ki` int(11) NOT NULL,
  `forca` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `status_info`
--

INSERT INTO `status_info` (`id`, `life`, `ki`, `forca`, `user_id`) VALUES
(2, 100, 1, 99, 2),
(3, 41, 9, 50, 3),
(5, 1400, 1300, 1260, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'xavier', '1234'),
(2, 'wellington', '1234'),
(3, 'santos', '1234'),
(14, 'Sonic', 'wellington'),
(15, 'Trunks', 'trunks'),
(16, 'Dim1', '1234'),
(17, '4000', '12000'),
(18, 'santoss', '12231324'),
(19, 'xarfgsa', 'çkdsfa'),
(20, 'hul', 'kkkkk'),
(21, 'wellington teste', '1234'),
(23, 'wellingtonx', '123456789'),
(24, 'Dara Desiane', '123456789'),
(25, 'dark', '123456789'),
(27, 'dark1', '1234'),
(28, 'darkt', '1234'),
(29, 'daark', '1234'),
(30, 'none', '1234'),
(31, 'none1', '1234'),
(32, 'none2', '1234'),
(33, 'non3', '1234'),
(34, 'nonee', '1'),
(35, 'none12', '1234'),
(36, 'non1e', '1234'),
(37, 'darke', '1234'),
(38, 'dark12', '1234'),
(39, 'dark15', '1234'),
(40, 'reicaveira ', '1234'),
(41, 'asdfg', '1');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cadastro`
--
ALTER TABLE `cadastro`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Índices de tabela `metas`
--
ALTER TABLE `metas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Índices de tabela `progresso`
--
ALTER TABLE `progresso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `meta_id` (`meta_id`);

--
-- Índices de tabela `status_info`
--
ALTER TABLE `status_info`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Índices de tabela `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cadastro`
--
ALTER TABLE `cadastro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de tabela `metas`
--
ALTER TABLE `metas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `progresso`
--
ALTER TABLE `progresso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `status_info`
--
ALTER TABLE `status_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de tabela `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `cadastro`
--
ALTER TABLE `cadastro`
  ADD CONSTRAINT `cadastro_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Restrições para tabelas `metas`
--
ALTER TABLE `metas`
  ADD CONSTRAINT `metas_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Restrições para tabelas `progresso`
--
ALTER TABLE `progresso`
  ADD CONSTRAINT `progresso_ibfk_1` FOREIGN KEY (`meta_id`) REFERENCES `metas` (`id`);

--
-- Restrições para tabelas `status_info`
--
ALTER TABLE `status_info`
  ADD CONSTRAINT `status_info_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
