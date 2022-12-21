-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: localhost    Database: carDataBase
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car` (
  `id` int NOT NULL AUTO_INCREMENT,
  `make` varchar(64) NOT NULL,
  `model` varchar(64) NOT NULL,
  `colour` varchar(64) NOT NULL,
  `year` int DEFAULT NULL,
  `mileage` int DEFAULT NULL,
  `type` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,'Volkswagen','Polo','Purple',1999,186679,'Hatchback'),(2,'Mercedes','S-Class','Grey',2001,54325,'Sedan'),(3,'BMW','3 Series','Orange',1992,53853,'Sedan'),(4,'Ford','Mondeo','Green',2003,155045,'Sedan'),(5,'Mercedes','E-Class','Purple',1985,150817,'Sedan'),(6,'Audi','TT','White',2010,90361,'Coupe'),(7,'Renault','Express','Grey',1990,141531,'Van'),(8,'Mercedes','C-Class','Grey',1996,19537,'Sedan'),(9,'Nissan','Juke','Red',2009,98157,'SUV'),(10,'Volkswagen','Arteon','Red',1988,16066,'Fastback'),(11,'Mercedes','E-Class','Black',1988,7955,'Sedan'),(12,'Nissan','GTR','Green',1991,137884,'Sport Car'),(13,'Toyota','Auris','Blue',1985,53099,'Hatchback'),(14,'Nissan','Leaf','Black',1986,5657,'Hatchback'),(15,'Renault','Clio','Purple',1989,29618,'Hatchback'),(16,'BMW','5 Series','Red',2010,147377,'Sedan'),(17,'Mercedes','C-Class','Purple',2015,36931,'Sedan'),(18,'Audi','E-tron','Red',1992,85086,'SUV'),(19,'Fiat','Punto','Purple',1997,173392,'Hatchback'),(20,'Audi','A2','Green',1993,195684,'Hatchback'),(21,'BMW','1 Series','Grey',2010,72125,'Hatchback'),(22,'Audi','A3','Red',2008,192379,'Sedan'),(23,'Mercedes','C-Class','Grey',1981,43546,'Sedan'),(24,'Ford','Mondeo','Purple',1992,61220,'Sedan'),(25,'Fiat','Panda','White',1984,133032,'Hatchback'),(26,'BMW','3 Series','Purple',2007,112571,'Sedan'),(27,'BMW','3 Series','Red',1980,88071,'Sedan'),(28,'Ford','Focus','Green',2017,133808,'Hatchback'),(29,'Audi','Q3','White',1986,91389,'SUV'),(30,'Audi','A1','Purple',1996,161693,'Hatchback'),(31,'BMW','5 Series','Green',1994,48716,'Sedan'),(32,'Audi','Q3','Orange',1988,114183,'SUV'),(33,'Fiat','Punto','Black',2007,7444,'Hatchback'),(34,'Nissan','Juke','Blue',1996,56752,'SUV'),(35,'Audi','Q7','Red',2017,108585,'SUV'),(36,'Audi','A3','Grey',1992,18078,'Sedan'),(37,'Fiat','Panda','Green',1989,186346,'Hatchback'),(38,'Audi','A2','Red',1992,29557,'Hatchback'),(39,'BMW','3 Series','White',1992,172501,'Sedan'),(40,'Ford','Fiesta','White',1999,123454,'Hatchback'),(41,'BMW','1 Series','Grey',1987,162120,'Hatchback'),(42,'Mercedes','C-Class','Purple',1982,51512,'Sedan'),(43,'Audi','A1','White',1989,5888,'Hatchback'),(44,'Mercedes','S-Class','Black',1999,17640,'Sedan'),(45,'Toyota','Corolla','Black',2013,33533,'Sedan'),(46,'Nissan','Navara','Green',1995,11957,'Pickup Truck'),(47,'Audi','Q5','Orange',1992,99684,'SUV'),(48,'Nissan','Quasqai','White',2002,6781,'SUV'),(49,'BMW','5 Series','Green',2010,164580,'Sedan'),(50,'Volkswagen','Touran','Blue',2009,102630,'Minivan'),(51,'Nissan','Juke','Purple',1980,149193,'SUV'),(52,'Fiat','Panda','Green',2001,125852,'Hatchback'),(53,'Audi','TT','Blue',1987,189077,'Coupe'),(54,'Toyota','Yaris','Red',2017,47801,'Hatchback'),(55,'Nissan','Juke','White',2016,37640,'SUV'),(56,'Ford','Mondeo','Red',1996,177614,'Sedan'),(57,'Volkswagen','Passat','Grey',1986,58452,'Sedan'),(58,'BMW','5 Series','Black',2003,100636,'Sedan'),(59,'Renault','Captur','Orange',1995,126550,'SUV'),(60,'Audi','A1','White',1990,154436,'Hatchback'),(61,'Nissan','Navara','Green',2009,137051,'Pickup Truck'),(62,'Mercedes','C-Class','Grey',2003,139246,'Sedan'),(63,'Ford','Focus','Red',2011,109430,'Hatchback'),(64,'Renault','Clio','Grey',1988,193294,'Hatchback'),(65,'Audi','R8','Green',2000,568,'Sport Car'),(66,'Ford','Mondeo','Purple',2002,187953,'Sedan'),(67,'Renault','Clio','Black',2002,51745,'Hatchback'),(68,'Fiat','Punto','Blue',2010,175013,'Hatchback'),(69,'Toyota','Corolla','White',1987,11053,'Sedan'),(70,'Nissan','Leaf','Black',2002,36894,'Hatchback'),(71,'BMW','1 Series','Green',2014,143335,'Hatchback'),(72,'Ford','Mondeo','Orange',2015,178070,'Sedan'),(73,'Volkswagen','Golf','Red',2020,190301,'Hatchback'),(74,'BMW','3 Series','Grey',2013,127682,'Sedan'),(75,'Mercedes','C-Class','Black',1981,127120,'Sedan'),(76,'Ford','Mondeo','Blue',2020,52629,'Sedan'),(77,'BMW','5 Series','Red',2017,108343,'Sedan'),(78,'BMW','1 Series','Grey',1983,105621,'Hatchback'),(79,'Audi','Q7','Red',1992,86114,'SUV'),(80,'Renault','Kadjar','Red',1984,198651,'SUV'),(81,'Mercedes','S-Class','Grey',2014,198904,'Sedan'),(82,'BMW','3 Series','Black',2009,30213,'Sedan'),(83,'Toyota','Auris','Red',2015,139543,'Hatchback'),(84,'Fiat','500','Purple',1994,170173,'Hatchback'),(85,'Ford','Mondeo','Orange',2018,34714,'Sedan'),(86,'Volkswagen','Up','Green',1987,47275,'Hatchback'),(87,'Toyota','Auris','Purple',1982,102571,'Hatchback'),(88,'Nissan','Leaf','Blue',2014,187159,'Hatchback'),(89,'Fiat','500','Black',1988,104301,'Hatchback'),(90,'Audi','R8','Grey',1981,32827,'Sport Car'),(91,'Nissan','Quasqai','Purple',2018,111208,'SUV'),(92,'Nissan','X-trail','Red',1999,171561,'SUV'),(93,'Audi','E-tron','Green',2000,103066,'SUV'),(94,'Nissan','Leaf','Black',1996,142285,'Hatchback'),(95,'Nissan','GTR','White',2003,80922,'Sport Car'),(96,'Mercedes','E-Class','Black',2005,24862,'Sedan'),(97,'Volkswagen','Tiguan','Purple',1982,54397,'SUV'),(98,'BMW','3 Series','Green',2000,34975,'Sedan'),(99,'Fiat','Punto','Orange',1985,151341,'Hatchback'),(100,'Ford','Fiesta','Green',1999,176168,'Hatchback');
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-21 16:35:07
