-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 12, 2023 at 10:23 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotelmgmttkinter`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `Ref` int(100) DEFAULT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Mother` varchar(100) DEFAULT NULL,
  `Gender` varchar(100) DEFAULT NULL,
  `PostCode` varchar(100) DEFAULT NULL,
  `Mobile` varchar(15) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Nationality` varchar(100) DEFAULT NULL,
  `Idproof` varchar(100) DEFAULT NULL,
  `Idnumber` varchar(100) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`Ref`, `Name`, `Mother`, `Gender`, `PostCode`, `Mobile`, `Email`, `Nationality`, `Idproof`, `Idnumber`, `Address`) VALUES
(6353, 'Aman Bhadoriya', 'Alexendra ', 'Male', '1232', '21345676**', 'aman@123.com', 'Indian', 'AdharCard', '13213*****', 'Mumbai'),
(2856, 'Devid', 'alexa', 'Male', '453217', '73664563**', 'devid@abc.com', 'American', 'Passport', '21245665655**', 'New York');

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `Floor` varchar(100) DEFAULT NULL,
  `RoomNo` varchar(100) DEFAULT NULL,
  `RoomType` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`Floor`, `RoomNo`, `RoomType`) VALUES
('3', '1002', 'Luxury'),
('1', '1003', 'Laxary'),
('3', '1002', 'Luxury'),
('2', '1003', 'Laxary');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `contact` varchar(30) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `securityQ` varchar(100) DEFAULT NULL,
  `securityA` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`fname`, `lname`, `contact`, `email`, `securityQ`, `securityA`, `password`) VALUES
('Sanchu', 'Kumar', '4231415256', 'Sanchu@abc.com', 'Your Birth Place', 'NUPR', '1234'),
('Mayank', 'Kumar', '89324343**', 'mayank@abc.com', 'Your Birth Place', 'Ujjain', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `contact` varchar(30) DEFAULT NULL,
  `check_in` varchar(45) DEFAULT NULL,
  `check_out` varchar(45) DEFAULT NULL,
  `roomtype` varchar(45) DEFAULT NULL,
  `roomavailable` varchar(45) DEFAULT NULL,
  `meal` varchar(45) DEFAULT NULL,
  `noOfdays` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`contact`, `check_in`, `check_out`, `roomtype`, `roomavailable`, `meal`, `noOfdays`) VALUES
('7366456366', '10/06/2023', '15/06/2023', 'Laxary', '1003', 'BreakFast', '5'),
('2134567689', '17/05/2023', '20/05/2023', 'Single', '1001', 'Launch', '3');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
