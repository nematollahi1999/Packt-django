--
-- Database: `samplevideo_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--
PRAGMA foreign_key = off;
BEGIN TRANSACTION;

-- Table: Products_list

CREATE TABLE IF NOT EXISTS product_details (
  id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
  pname varchar(255) DEFAULT NULL,
  sellername varchar(50) DEFAULT NULL,
  gender varchar(10) DEFAULT NULL,
  situation varchar(50) DEFAULT NULL,
);

--
-- Dumping data for table `product_details`
--

INSERT INTO product_details (id, pname, sellername, gender, situation) VALUES
(1, 'Rose', 'Tehran', 'Female', 'Available');
INSERT INTO product_details (id, pname, sellername, gender, situation) VALUES
(2, 'Lavender', 'Tehran', 'Female', 'Available');
INSERT INTO product_details (id, pname, sellername, gender, situation) VALUES
(3, 'Daisy', 'Tabriz', 'Female', 'Available');
INSERT INTO product_details (id, pname, sellername, gender, situation) VALUES
(4, 'Lily', 'Tehran', 'Female', 'Unavailable');
INSERT INTO product_details (id, pname, sellername, gender, situation) VALUES
(5, 'Dahila', 'Tehran', 'Female', 'Unavailable');
INSERT INTO product_details (id, pname, sellername, gender, situation) VALUES
(6, 'Iris', 'Tehran', 'Female', 'Available');

