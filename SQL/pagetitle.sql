CREATE TABLE `pagetitle` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `pagetitle` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `date_added` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;