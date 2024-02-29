-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 29, 2024 at 10:48 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `asmitha`
--

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`) VALUES
('Admin', 'Admin123');

-- --------------------------------------------------------

--
-- Table structure for table `student_management`
--

CREATE TABLE `student_management` (
  `STUDENT_ID` int(11) NOT NULL,
  `NAME` text DEFAULT NULL,
  `EMAIL` text DEFAULT NULL,
  `PHONE_NO` text DEFAULT NULL,
  `GENDER` text DEFAULT NULL,
  `DOB` text DEFAULT NULL,
  `STREAM` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_management`
--

INSERT INTO `student_management` (`STUDENT_ID`, `NAME`, `EMAIL`, `PHONE_NO`, `GENDER`, `DOB`, `STREAM`) VALUES
(1, 'Rani', 'rani@gmail.com', '9566561500', 'Female', '2004-12-4', 'Lawyer'),
(5, 'Abishek', 'abishek123@gmail.com', '8012425695', 'Male', '1999-11-29', 'Engineer'),
(7, 'Bertha', 'bertha99@gmail.com', '9876543212', 'Female', '1990-11-29', 'IT'),
(8, 'Babloo', 'babloo22@gmail.com', '9873216545', 'Male', '1995-11-29', 'Distributor'),
(9, 'Aneesha', 'aneesha2008@gmail.com', '9638527412', 'Female', '2008-11-29', 'IT'),
(10, 'Krithick Mithun', 'mithun2010@gmail.com', '9512368745', 'Male', '2010-11-29', 'Doctor'),
(11, 'Yathvick vithun', 'yathvick12@gmail.com', '9514786325', 'Male', '2000-11-29', 'Computer Engineer'),
(12, 'Murugeshwari', 'murgeshwari89@gmail.com', '9524963265', 'Female', '1985-11-29', 'Receptionist'),
(13, 'Balamani', 'balamani11@gmail.com', '9865718488', 'Female', '1982-11-29', 'Teacher'),
(14, 'Ramu', 'ramu99@gmail.com', '9710972563', 'Male', '1970-11-29', 'Supervisor'),
(15, 'Mohammad Shahid', 'shaju98@gmail.com', '9710369852', 'Male', '1972-11-29', 'Professor'),
(16, 'Yashiv', 'yash88@gmail.com', '9632147852', 'Male', '1980-11-29', 'Business'),
(17, 'Yeshwanth', 'yesh34@gmail.com', '8523697412', 'Male', '2000-11-29', 'Income Tax'),
(18, 'Raji', 'raji77@gmail.com', '9042295563', 'Female', '1995-11-29', 'Zumba fitness'),
(19, 'Raja', 'rajaa01@gmail.com', '9042296637', 'Male', '1970-11-29', 'MLA'),
(20, 'Meena', 'meena98@gmail.com', '9566749865', 'Female', '1994-11-29', 'IT');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student_management`
--
ALTER TABLE `student_management`
  ADD PRIMARY KEY (`STUDENT_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student_management`
--
ALTER TABLE `student_management`
  MODIFY `STUDENT_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
