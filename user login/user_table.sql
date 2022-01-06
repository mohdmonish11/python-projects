-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 31, 2020 at 09:38 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user_table`
--

-- --------------------------------------------------------

--
-- Table structure for table `courseinsertion`
--

CREATE TABLE `courseinsertion` (
  `sno` int(11) NOT NULL,
  `course_name` varchar(200) NOT NULL,
  `course_category` varchar(200) NOT NULL,
  `course_duration` varchar(3) NOT NULL,
  `fees` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `courseinsertion`
--

INSERT INTO `courseinsertion` (`sno`, `course_name`, `course_category`, `course_duration`, `fees`) VALUES
(1, 'autocad', 'Technical', '1', 5000),
(2, 'python', 'Mechanical', '2', 6500),
(3, 'C', 'Non-Technical', '3', 6787),
(4, 'C++', 'Management', '1', 8520),
(5, 'python', 'Technical', '1', 8888);

-- --------------------------------------------------------

--
-- Table structure for table `studentinsertion`
--

CREATE TABLE `studentinsertion` (
  `sno` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `course` int(5) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `address` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentinsertion`
--

INSERT INTO `studentinsertion` (`sno`, `name`, `course`, `phone`, `address`) VALUES
(1, 'Monish', 1, '8858047609', 'Lakshmi Nagar'),
(2, 'Abdul', 4, '8090780606', 'Badarpur'),
(3, 'Shyam', 3, '4545454545', 'NOhar'),
(4, 'Roshan', 2, '885252525', 'Uttam Nagar'),
(5, 'Mahi', 1, '85858588', 'hjth'),
(6, 'Sohani', 5, '25242563', 'ghthh');

-- --------------------------------------------------------

--
-- Table structure for table `user_table`
--

CREATE TABLE `user_table` (
  `sno` int(11) NOT NULL,
  `name` varchar(120) NOT NULL,
  `email` varchar(250) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_table`
--

INSERT INTO `user_table` (`sno`, `name`, `email`, `password`) VALUES
(2, 'Monish', 'md.monish123ee@gmail.com', '124523%$'),
(3, 'shyam', 'shyan123e@gmail.com', '2525204'),
(5, 'rohan1234', 'rohan@gmail.com', 'rohan12345');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `courseinsertion`
--
ALTER TABLE `courseinsertion`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `studentinsertion`
--
ALTER TABLE `studentinsertion`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `user_table`
--
ALTER TABLE `user_table`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `courseinsertion`
--
ALTER TABLE `courseinsertion`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `studentinsertion`
--
ALTER TABLE `studentinsertion`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user_table`
--
ALTER TABLE `user_table`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
