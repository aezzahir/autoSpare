-- Create database + user if doesn't exist
CREATE DATABASE IF NOT EXISTS spear_dev_db;
CREATE USER IF NOT EXISTS 'spear_dev'@'localhost';
SET PASSWORD FOR 'spear_dev'@'localhost' = 'spear_dev_pwd';
GRANT ALL ON spear_dev_db.* TO 'spear_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'spear_dev'@'localhost';
FLUSH PRIVILEGES;

USE spear_dev_db;

-- Table structure for table `suppliers`
DROP TABLE IF EXISTS `suppliers`;
CREATE TABLE `suppliers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `name` varchar(128) NOT NULL,
  `cage_code` int(11) NOT NULL,
  `address` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Table structure for table `products`
DROP TABLE IF EXISTS `products`;
CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `designation` varchar(128) NOT NULL,
  `NSN` int(11) NOT NULL,
  `description` varchar(128) NOT NULL,
  `supplier_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `products_supplier_fk` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table `suppliers`
LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES (1,'2024-02-26 12:00:00','2024-02-26 12:00:00','ABC Corporation',123456,'123 Main St'),(2,'2024-02-26 12:00:00','2024-02-26 12:00:00','XYZ Inc.',654321,'456 Elm St'),(3,'2024-02-26 12:00:00','2024-02-26 12:00:00','LMN Enterprises',789012,'789 Oak St'),(4,'2024-02-26 12:00:00','2024-02-26 12:00:00','PQR Limited',987654,'987 Pine St');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

-- Dumping data for table `products`
LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'2024-02-26 12:00:00','2024-02-26 12:00:00','Sharp Spear',123456,'Description A',1),(2,'2024-02-26 12:00:00','2024-02-26 12:00:00','Sturdy Spear',654321,'Description B',2),(3,'2024-02-26 12:00:00','2024-02-26 12:00:00','Swift Spear',789012,'Description C',3),(4,'2024-02-26 12:00:00','2024-02-26 12:00:00','Powerful Spear',987654,'Description D',4);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

