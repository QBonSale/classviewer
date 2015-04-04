-- MySQL dump 10.13  Distrib 5.5.41, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: classviewer
-- ------------------------------------------------------
-- Server version	5.5.41-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `class` (
  `year` int(11) NOT NULL DEFAULT '0',
  `quarter` char(1) NOT NULL DEFAULT '',
  `major` varchar(10) DEFAULT NULL,
  `course_number` varchar(10) NOT NULL DEFAULT '',
  `professor` varchar(100) DEFAULT NULL,
  `type` varchar(5) DEFAULT NULL,
  `building` varchar(100) DEFAULT NULL,
  `room` varchar(10) DEFAULT NULL,
  `days` varchar(7) DEFAULT NULL,
  `start` time DEFAULT NULL,
  `stop` time DEFAULT NULL,
  `rest` tinyint(1) DEFAULT NULL,
  `lecture_number` int(11) NOT NULL DEFAULT '0',
  `course_title` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`year`,`quarter`,`course_number`,`lecture_number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `class_over_time`
--

DROP TABLE IF EXISTS `class_over_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `class_over_time` (
  `snapshot_time` datetime DEFAULT NULL,
  `num_en` int(11) DEFAULT NULL,
  `en_cap` int(11) DEFAULT NULL,
  `num_wl` int(11) DEFAULT NULL,
  `wl_cap` int(11) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `quarter` char(1) DEFAULT NULL,
  `course_number` varchar(10) DEFAULT NULL,
  `lecture_number` int(11) DEFAULT NULL,
  KEY `year` (`year`,`quarter`,`course_number`,`lecture_number`),
  CONSTRAINT `class_over_time_ibfk_1` FOREIGN KEY (`year`, `quarter`, `course_number`, `lecture_number`) REFERENCES `class` (`year`, `quarter`, `course_number`, `lecture_number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `section`
--

DROP TABLE IF EXISTS `section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `section` (
  `section_id_number` int(11) DEFAULT NULL,
  `type` varchar(5) DEFAULT NULL,
  `building` varchar(100) DEFAULT NULL,
  `room` varchar(10) DEFAULT NULL,
  `sec` char(1) DEFAULT NULL,
  `days` varchar(7) DEFAULT NULL,
  `start` time DEFAULT NULL,
  `stop` time DEFAULT NULL,
  `quarter` char(1) DEFAULT NULL,
  `course_number` varchar(10) DEFAULT NULL,
  `lecture_number` int(11) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  KEY `year` (`year`,`quarter`,`course_number`,`lecture_number`),
  KEY `year_2` (`year`,`lecture_number`,`course_number`,`quarter`,`sec`),
  CONSTRAINT `section_ibfk_1` FOREIGN KEY (`year`, `quarter`, `course_number`, `lecture_number`) REFERENCES `class` (`year`, `quarter`, `course_number`, `lecture_number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `section_over_time`
--

DROP TABLE IF EXISTS `section_over_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `section_over_time` (
  `snapshot_time` datetime DEFAULT NULL,
  `num_en` int(11) DEFAULT NULL,
  `en_cap` int(11) DEFAULT NULL,
  `num_wl` int(11) DEFAULT NULL,
  `wl_cap` int(11) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `quarter` char(1) DEFAULT NULL,
  `course_number` varchar(10) DEFAULT NULL,
  `lecture_number` int(11) DEFAULT NULL,
  `sec` char(1) DEFAULT NULL,
  KEY `year` (`year`,`lecture_number`,`course_number`,`quarter`,`sec`),
  CONSTRAINT `section_over_time_ibfk_1` FOREIGN KEY (`year`, `lecture_number`, `course_number`, `quarter`, `sec`) REFERENCES `section` (`year`, `lecture_number`, `course_number`, `quarter`, `sec`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-04-04 19:16:38
