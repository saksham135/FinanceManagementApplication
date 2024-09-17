-- phpMyAdmin SQL Dump
-- version 5.3.0-dev+20220826.811789df3c
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 12, 2024 at 08:16 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `finance_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `budgets`
--

CREATE TABLE `budgets` (
  `user_id` int(11) NOT NULL,
  `category` enum('income','expense') NOT NULL,
  `monthly_limit` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `budgets`
--

INSERT INTO `budgets` (`user_id`, `category`, `monthly_limit`) VALUES
(1, 'income', '25000.00'),
(6, 'income', '1200.00'),
(11, 'income', '100.00');

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `user_id` int(11) NOT NULL,
  `type` enum('income','expense') NOT NULL,
  `category` varchar(255) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `description` text DEFAULT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`user_id`, `type`, `category`, `amount`, `description`, `date`) VALUES
(1, 'income', 'august salary', '25000.00', 'monthly salary', '2024-05-01'),
(1, 'expense', 'Food', '5000.00', 'shopping', '2024-05-04'),
(1, 'income', 'income', '20000.00', 'yearly salary', '2024-05-02'),
(1, 'income', 'october salary', '100.00', 'salary', '2024-10-02'),
(1, 'income', 'salary', '2500.00', 'updated salary', '2024-01-25'),
(6, 'income', 'august salary', '10000.00', 'monthly salary', '2024-02-01'),
(6, 'expense', 'income', '25000.00', 'shopping', '2024-02-09'),
(7, 'income', 'september salary', '100000.00', 'salary', '2024-09-12'),
(7, 'income', 'septmeber income', '120000.00', 'monthly salary', '2024-09-13'),
(11, 'expense', 'expense', '120000.00', 'Grocery', '2024-08-12'),
(11, 'income', 'September Salary', '10000.00', 'Monthly Salary', '2024-09-09');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password_hash`) VALUES
(1, 'admin', '$2b$12$sH9DEQb90Cgqzx6Lhtwi4enb2jl6wtUsT4GWKetZX5wxOHJzYl4Lm'),
(6, 'hitika', '$2b$12$dY7eF20VGLmwcJKybrAkFOV5COB2HxW4bEHWEBsnnspsCVQE.PWAO'),
(7, 'ashok', '$2b$12$S7rsH/FjIAjnNyKacQLkDOCI/BScEFg82ndji3DnVWmwm2Zty.rIa'),
(8, 'user12', '$2b$12$8il30DwZaJC0491xv9FG7uyFzayVi4W0e5knVsKBkj.r4qOSzvUcq'),
(11, 'new_user', '$2b$12$YXk2BILXBLW9vMoNsywhqONWaxjj8TQDrPtnMEXWJQsLCcq/aW7LK'),
(12, 'admin123', '$2b$12$4anFltD1sbIPhsGvrK7XpOTGnCska6NAAAhzDujvXw0GdKNN0ionW');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `budgets`
--
ALTER TABLE `budgets`
  ADD PRIMARY KEY (`user_id`,`category`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`user_id`,`category`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `budgets`
--
ALTER TABLE `budgets`
  ADD CONSTRAINT `budgets_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `transactions`
--
ALTER TABLE `transactions`
  ADD CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
