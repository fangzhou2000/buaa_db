-- MySQL dump 10.13  Distrib 8.0.26, for macos11 (x86_64)
--
-- Host: rm-2zeu3f7e1n5yt10v0co.mysql.rds.aliyuncs.com    Database: spoc
-- ------------------------------------------------------
-- Server version	8.0.18

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'a1bf3042-2109-11ec-bd72-00163e3259ee:1-430258';

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `admin_id` (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('admin','123456','管理员01');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_post`
--

DROP TABLE IF EXISTS `admin_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_post` (
  `admin_id` varchar(255) NOT NULL,
  `post_id` int(20) NOT NULL,
  PRIMARY KEY (`admin_id`,`post_id`) USING BTREE,
  KEY `ap` (`post_id`,`admin_id`) USING BTREE,
  CONSTRAINT `ap_admin_f` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ap_post_f` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_post`
--

LOCK TABLES `admin_post` WRITE;
/*!40000 ALTER TABLE `admin_post` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_posttheme`
--

DROP TABLE IF EXISTS `admin_posttheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_posttheme` (
  `admin_id` varchar(255) NOT NULL,
  `posttheme_id` int(20) NOT NULL,
  PRIMARY KEY (`admin_id`,`posttheme_id`) USING BTREE,
  KEY `apt` (`posttheme_id`,`admin_id`) USING BTREE,
  CONSTRAINT `apt_admin_f` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `apt_posttheme_f` FOREIGN KEY (`posttheme_id`) REFERENCES `posttheme` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_posttheme`
--

LOCK TABLES `admin_posttheme` WRITE;
/*!40000 ALTER TABLE `admin_posttheme` DISABLE KEYS */;
INSERT INTO `admin_posttheme` VALUES ('admin',42);
/*!40000 ALTER TABLE `admin_posttheme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `content` varchar(10000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `time` varchar(100) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `comment_id` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (11,'算法设计2感觉还不错哈','2021-11-21 20:49:15'),(18,'在此课程学习了递归、分治、动态规划和贪心','2021-11-22 02:36:03'),(21,'算法值得学习','2021-11-22 03:28:34'),(32,'这门课程是开卷考试，最终大作业是写一篇综述和Web Service小程序。','2021-11-23 01:39:00'),(34,'不孬','2021-11-23 18:08:12'),(46,'真的吗，我不信','2021-12-10 19:44:01'),(50,'信息前沿理论对于本科生的学习具有重要意义！','2021-12-11 10:17:58'),(120,'老师很友善','2021-12-12 21:17:21'),(122,'郭焱老师很棒\n','2021-12-12 21:18:54'),(123,'学习过太极拳，是中国传统文化遗产，很好！','2021-12-12 21:37:38'),(124,'太难了','2021-12-12 21:43:05'),(125,'作业和讲课内容严重分离','2021-12-12 21:43:36');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `comment_delete` BEFORE DELETE ON `comment` FOR EACH ROW BEGIN
		DECLARE sid VARCHAR(255);
		SET sid = (SELECT student_id FROM student_comment where comment_id=old.id);
		UPDATE student SET count_comment = count_comment - 1 
		where id=sid;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `comment_degree` BEFORE DELETE ON `comment` FOR EACH ROW BEGIN
	DECLARE cid int;
	DECLARE judge int;
	SET cid = (SELECT course_id from course_comment where comment_id=old.id);
	DELETE from course_comment where course_id=cid and comment_id=old.id;
	SET judge = (SELECT course_id from course_comment where comment_id=old.id);
-- 	if judge is null THEN
-- 		UPDATE course SET degree = 5 where id=cid;
-- 	ELSE
		UPDATE course SET degree = (SELECT AVG(degree) from course_comment 
			where course_id=cid GROUP BY course_id)
			where id=cid;
-- 	end if;	
SET judge = (SELECT degree FROM course where id=cid);
if judge is null THEN
		UPDATE course SET degree = 5 where id=cid;
end if;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `introduction` varchar(10000) DEFAULT NULL,
  `degree` float(10,1) DEFAULT '5.0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `course_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (26,'体育（5）','<p>体育必修课，包括太极拳、人体工程、羽毛球、乒乓球、游泳、篮球、足球等。</p>',4.5),(42,'线性代数','线性代数是数学的一个分支，它的研究对象是向量，向量空间（或称线性空间），线性变换和有限维的线性方程组。向量空间是现代数学的一个重要课题；因而，线性代数被广泛地应用于抽象代数和泛函分析中；通过解析几何，线性代数得以被具体表示。线性代数的理论已被泛化为算子理论。由于科学研究中的非线性模型通常可以被近似为线性模型，使得线性代数被广泛地应用于自然科学和社会科学中。\n\n',3.5),(68,'算法设计与分析','<p>《算法设计与分析》是计算机专业的一门重要专业基础课。计算机学科中，无论是软件设计，还是硬件设计都离不开算法，算法计算机科学的核心。本课程为学生打开算法之门，介绍常用的算法设计策略和技术、众多经典问题及其算法设计思想、算法证明和分析的方法和技术等。通过本课程的学习，使学生熟练掌握算法设计的基本理论、方法和技术，训练计算思维，提高分析问题和解决问题的实际能力。</p>',5.0),(75,'xml和Web Service','<p>课程针对近年来互联网软件发展过程中出现和得到广泛使用的XML信息处理和Web服务技术，主要讲述互联网环境下软件需求的变化和计算模式的发展，重点讲授XML信息处理和Web服务等相关软件新技术的基本概念、工作原理、技术规范、开发环境和典型应用。课程的主要目的是使得学生能够了解并掌握当前互联网相关软件新技术的知识体系，为学生进行应用实践和进行专业工作打好基础，提高计算机软件知识技术水平。 通过该课程的学习，使学生能够达到如下目标： 1) 了解并掌握互联网软件的应用需求特点、计算模式变化和技术发展趋势 2) 了解并掌握XML信息处理技术，如DTD、Schema、DOM、SAX、XSLT等，能够进行XML应用的简单分析和设计，能够进行XML文档处理程序的设计和实现。 3) 了解并掌握Web Services工作原理和技术规范，如SOA、SOAP、WSDL、UDDI、BPEL、WS-Security。 4) 了解并掌握典型的Web Services开发环境和工具，如.NET Framework、Visual Studio .NET、C#语言，及.NET和J2EE其比较。能够进行Web服务软件的分析与设计，能够使用常见的开发工具环境进行Web服务程序的设计和实现。 5) 了解并掌握典型的Web Services应用场景和案例，扩大计算机专业学生在互联网软件技术领域的视野，进一步提高计算机专业实践工作的能力。</p>',5.0),(76,'2021编译技术','<p>编译原理是计算机专业的一门重要专业课，旨在介绍编译程序构造的一般原理和基本方法。内容包括语言和文法、词法分析、语法分析、语法制导翻译、中间代码生成、存储管理、代码优化和目标代码生成。 编译原理是计算机专业设置的一门重要的专业课程。</p>',5.0),(79,'高等数学','高等数学是一门十分重要的基础理论课。它的主要研究对象为实变实值函数，尤其是连续的实变实值函数。本课程包括的主要内容有：一元函数的极限，连续、微分、积分，级数及多元函数的极限、连续、微分、积分（含参积分，线积分、重积分、面积分）、空间解析几何、微分方程等。\n\n',5.0),(83,'大学语文','大学选修课，《大学语文》课程致力于学生了解中国传统文化，继承发扬民族精神，从而增强学生人文精神，提升个人人格力量；从优秀文学作品中获得美感、陶冶性情，以提高文学鉴赏力和写作水平；并在此基础上达到突破学生思维定势，培养学生探索创新的能力。',5.0),(87,'法学原理','通过讲授法学基本原理相关知识，旨在引导学生通过独立思考、自主学习进入到法学体系的殿堂，以使学生在掌握法理学的基本知识理论的前提下，提高法律思辨能力，并使学生学会运用法学基础理论分析、解释和解决部门法与法律实践中的各种问题。',5.0),(102,'信息前沿理论','本课程的教学内容主要关于信息理论中概念、思想和历史，不涉及具体的理论知识。为增强理论教学、实践应用与研讨交流相结合，本课程设置课堂讲授、演讲和辩论三大教学环节。主要内容包含信息的起源，信息的本质，信息理论的兴起和信息理论的未来。',5.0),(103,'法律、科技与社会','本课程是专门为计算机学院本科生开始的通识核心课，主要研讨人工智能、大数据、基因编辑等新技术带来的法律和伦理问题，以及法律和伦理对于新技术的规制。具体包括：1. 人工智能的法律与伦理规制；2. 数据主权与安全；3. 个人数据保护；4. 基因编辑的法律与伦理规制。\n\n',5.0),(104,'证券投资学原理与应用	','本课程为投资学入门课程，介绍了投资学的基本原理，分析投资市场特别是中国证券投资市场的运行规律。引导学生利用投资学基本原理应用于投资实践分析。课程引用大量中国证券市场的典型案例和数据，介绍中国投资市场的运行机制，使得学生能够理论与实践得到很好的结合。',5.0),(105,'进化、行为与生态','进化是生物学的核心主题，而生物学对于生物与医学工程的大学生，甚至可能是所有大学生来说是必需拥有的知识。本课程分为8节课，每节课讲授进化的一个重要题目。本课程有8个功课作业，每个功课作业包含进化与医学、工程或其他学术领域相关的文章题目。本课程的主要目的是为学生提供对进化生物学的了解；其次是激发学生对本科学的兴趣。\n\n \n\nEvolution is the core theme of biology, and biology is essential for college students in biological science and medical engineering, if not for all college students in general. This course is divided into 8 lectures, and each lecture teaches an important topic of evolution. The course has 8 homework assignments, and each homework assignment consists of an essay topic that associates evolution with medicine, engineering, or other academic fields. The main objective of this course is to provide students with an understanding of evolutionary biology. A secondary objective is to let students to develop an interest in science.',5.0),(106,'舞蹈之美','   本课程以舞蹈理论为线，以舞蹈赏析为案展开对舞蹈之美的讨论，是一门集美学、舞蹈学及舞蹈实践为一体的交叉学科。舞蹈既是一门艺术，也是一种文化。感受舞蹈之美一方面需要从艺术的本质入手，同时，也要从人类的生命实践活动中来。课程以“美”作为引线，引导学生发现这样一种“有反省，有思维，有渴望，有向往，有对伤痛的悲悯，也有对喜悦的期待”的哲思。从而提高学生们感受美、表现美、鉴赏美、创造美的能力，促进德智体美全面和谐发展。\n\n  《舞蹈之美》课程全篇贯以对舞蹈艺术的审美体验，帮助学生提升艺术素养的同时体验不同的文化；在此基础上增强学生的审美自觉性，使学生能够更自觉地通过审美活动去追求一种更有意义、更有价值和更有趣味的人生。通过大量作品的讲解与分析从而实现提高审美素养，培养创新精神和实践能力，塑造健全人格的美育作用。课程涉及哲学、艺术学、舞蹈学、文化学的基础理论，内容精炼、重点突出。\n\n  通过美学理论以及舞蹈实践的学习，帮助学生树立正确的审美观念，培养高雅的审美品位，提高人文素养；了解、吸纳中外优秀艺术成果，理解并尊重多元文化；发展形象思维，培养创新精神和实践能力，提高感受美、表现美、鉴赏美、创造美的能力，促进德智体美全面和谐发展。总之，通过《舞蹈之美》的课程学习，有助于提高大学生的艺术修养，有利于提高对学生的多元思维的培养，更有利于学生综合素质的提升，使学生在理智、道德、情感等方面全面发展。',5.0),(108,'智能计算体系结构','<p>本课程是面向理工科三年级本科生开设的专业选修课程，为《计算机组成原理和实验》与《智能计算导论》等课程的后续延伸，尝试将智能计算硬件加速的最新研究前沿技术引入课堂。本课 程涉及到的理论基础较为广泛，包括智能计算领域（人工智能、机器学习、数据挖掘、图像处理、 计算机视觉等）与硬件加速领域（硬件描述语言、计算机组成原理、数字系统设计、集成电路设计等）的基本知识。</p>',2.0),(109,'职业规划讲座','<p>职业规划讲座是6系的必修课</p>',5.0),(118,'西方音乐史与名曲鉴赏','<p>	<span style=\"background-color: rgb(255, 255, 255); color: rgb(103, 103, 103);\">本课程以西方音乐历史的发展为脉络，重点讲授巴罗克时期、维也纳古典时期、浪漫派时期、民族乐派到德彪西印象派的音乐风格与特点，并结合各时期产生的音乐体裁，介绍每个历史时期最具有代表性的作曲家及其音乐作品。</span>	</p><p>	<span style=\"background-color: rgb(255, 255, 255); color: rgb(103, 103, 103);\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;本课程对音乐作品的分析主要以视频资料呈现（因新冠疫情原因，近期将分阶段向同学们提供声频MP3学习资料、学习提纲），以展示50年来世界著名的指挥家、演奏家、歌唱家对音乐作品的权威诠释。同时，还将对不同的演奏团体、演奏家、歌唱家演绎的作品风格进行比较。</span>	</p><p>	<span style=\"background-color: rgb(255, 255, 255); color: rgb(103, 103, 103);\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;开设本课程旨在培养大学生正确的审美理想、健康的审美情趣，提升对美的感受力、鉴赏力，激发研究型人才的创造力和全面素质的提高。</span></p>',5.0),(122,'太极拳（2）','<p><span style=\"background-color: rgb(255, 255, 255); color: rgb(247, 49, 49);\">太极拳</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(51, 51, 51);\">，国家级非物质文化遗产，是以中国传统儒、道哲学中的太极、阴阳辩证理念为核心思想，集颐养性情、强身健体、技击对抗等多种功能为一体。大家快来学习。</span></p>',4.0);
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `course_delete` BEFORE DELETE ON `course` FOR EACH ROW BEGIN
		DECLARE sid VARCHAR(255);
		SET sid = (SELECT teacher_id FROM teacher_course where course_id=old.id);
		UPDATE teacher SET count_course = count_course - 1 
		where id=sid;
-- 		SET sid = (SELECT student_id FROM student_course where course_id=old.id);
-- 		UPDATE student SET count_course = count_course - 1
-- 		where id=sid;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `course_comment_delete` BEFORE DELETE ON `course` FOR EACH ROW BEGIN
-- 	DELETE FROM comment where id IN
-- 	(SELECT comment_id from course_comment WHERE course_id=old.id);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `course_comment`
--

DROP TABLE IF EXISTS `course_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course_comment` (
  `comment_id` int(20) NOT NULL,
  `course_id` int(20) NOT NULL,
  `degree` int(11) DEFAULT '5',
  PRIMARY KEY (`comment_id`,`course_id`),
  KEY `cc` (`course_id`,`comment_id`) USING BTREE,
  CONSTRAINT `cc_comment_f` FOREIGN KEY (`comment_id`) REFERENCES `comment` (`id`),
  CONSTRAINT `cc_course_f` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_comment`
--

LOCK TABLES `course_comment` WRITE;
/*!40000 ALTER TABLE `course_comment` DISABLE KEYS */;
INSERT INTO `course_comment` VALUES (11,68,5),(18,68,5),(21,68,5),(32,75,5),(34,76,5),(46,26,5),(50,102,5),(120,42,4),(122,26,4),(123,122,4),(124,42,3),(125,108,2);
/*!40000 ALTER TABLE `course_comment` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `course_comment_insert` AFTER INSERT ON `course_comment` FOR EACH ROW begin 
UPDATE course SET degree = 
	(SELECT AVG(degree) FROM course_comment 
		WHERE course_id = new.course_id GROUP by course_id)
	WHERE id=new.course_id;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `course_material`
--

DROP TABLE IF EXISTS `course_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course_material` (
  `material_id` int(20) NOT NULL,
  `course_id` int(20) NOT NULL,
  PRIMARY KEY (`material_id`,`course_id`),
  KEY `cm` (`course_id`,`material_id`) USING BTREE,
  CONSTRAINT `cm_course_f` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `cm_material_f` FOREIGN KEY (`material_id`) REFERENCES `material` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_material`
--

LOCK TABLES `course_material` WRITE;
/*!40000 ALTER TABLE `course_material` DISABLE KEYS */;
INSERT INTO `course_material` VALUES (1,26),(48,42),(48,109),(82,76),(84,76),(84,83),(84,109),(97,75),(98,75),(98,83),(104,26),(104,87),(105,68),(106,102),(107,26),(107,102),(108,104),(110,108),(112,118),(113,122);
/*!40000 ALTER TABLE `course_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material`
--

DROP TABLE IF EXISTS `material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `material` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `material_id` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material`
--

LOCK TABLES `material` WRITE;
/*!40000 ALTER TABLE `material` DISABLE KEYS */;
INSERT INTO `material` VALUES (1,'经济管理课件'),(48,'线性代数课件'),(82,'编译技术实验⽂法定义及相关说明'),(84,'编译器课程设计MARS仿真器使用说明'),(97,'xml教程'),(98,'WebService课程'),(101,'证据法学'),(102,'证据法学2'),(103,'数据库习题解析'),(104,'《法学原理》（中国铁道出版社）'),(105,'《算法设计与分析》第四版'),(106,'《信息论基础》（机械工业出版社）'),(107,'《信息简史》（人民邮电出版社）'),(108,'《投资学原理及应用》（机械工业出版社）'),(110,'《智能计算体系结构》（第二版）'),(112,'《西方音乐史与名作赏析》'),(113,'太极拳教学视频');
/*!40000 ALTER TABLE `material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `content` varchar(10000) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `isTeacher` int(5) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `post_id` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=120 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (1,'我来跟帖','2021-11-22 03:24:51',0),(11,'放在‘查看个人主题帖’那行不\n','2021-11-22 10:44:18',0),(12,'等会，我需要再改下数据库，稍等在拉取一个版本哈','2021-11-22 10:44:55',0),(22,'前端写了一部分，看看有没有影响后端','2021-11-22 17:01:04',0),(25,'新版本IDEA不支持WebService，需要使用2018版本的IDEA','2021-11-23 01:41:30',0),(26,'1. 侧边栏可以一直展开吗？不要点击后就缩回去。\n2. 主题帖的标题点进去没有显示。\n3. 能否侧边栏和右侧内容栏不同步滑动。让侧边栏固定。','2021-11-23 01:43:57',0),(27,'可不可以增加删除确认弹窗？（学生的主题帖删除、跟帖删除、课程评价的删除、选课、退课， 老师的停课和删除学习材料）','2021-11-23 01:50:17',0),(34,'已解决','2021-11-24 16:24:19',0),(37,'课程选课没有确认弹窗','2021-11-29 15:22:02',0),(41,'？','2021-12-01 22:52:28',1),(57,'测试','2021-12-02 00:47:19',0),(69,'辛苦了','2021-12-07 19:39:36',0),(74,'辛苦了，前端很好看！','2021-12-10 20:39:24',0),(75,'面壁十年图破壁，难酬蹈海亦英雄！','2021-12-10 20:41:11',0),(77,'今天进行修改的一些重点：1、表单验证，一方面需要对密码进行检测；另一方面需要在个人主页中增加一些新的内容（选）；2、对于图片的处理和后端的响应；3、对于课程信息的修改；4、复用','2021-12-11 10:04:46',0),(78,'试试效果？','2021-12-11 10:16:33',0),(82,'大作业请及时提交','2021-12-11 15:44:05',1),(118,'面壁十年图破壁，难酬蹈海亦英雄！\n','2021-12-12 20:55:16',0),(119,'好嘞，老师','2021-12-12 21:19:24',0);
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `post_delete` BEFORE DELETE ON `post` FOR EACH ROW BEGIN
		DECLARE type int;
		DECLARE sid VARCHAR(255);
		SET type = old.isTeacher;
		if type = 0 THEN
			SET sid = (SELECT student_id FROM student_post where post_id=old.id);
			UPDATE student SET count_discuss = count_discuss - 1 where id=sid;
		ELSEIF type = 1 THEN
			SET sid = (SELECT teacher_id FROM teacher_post where post_id=old.id);
			UPDATE teacher SET count_discuss = count_discuss - 1 where id=sid;
		END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `post_posttheme`
--

DROP TABLE IF EXISTS `post_posttheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post_posttheme` (
  `post_id` int(20) NOT NULL,
  `posttheme_id` int(20) NOT NULL,
  PRIMARY KEY (`post_id`,`posttheme_id`),
  KEY `pp` (`posttheme_id`,`post_id`) USING BTREE,
  CONSTRAINT `pp_post_f` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `pp_posttheme_f` FOREIGN KEY (`posttheme_id`) REFERENCES `posttheme` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_posttheme`
--

LOCK TABLES `post_posttheme` WRITE;
/*!40000 ALTER TABLE `post_posttheme` DISABLE KEYS */;
INSERT INTO `post_posttheme` VALUES (1,11),(11,13),(12,13),(22,11),(25,18),(26,19),(27,19),(34,19),(37,19),(69,42),(74,11),(75,47),(77,11),(78,11),(82,18),(118,47),(119,87);
/*!40000 ALTER TABLE `post_posttheme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posttheme`
--

DROP TABLE IF EXISTS `posttheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posttheme` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(10000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `content` varchar(10000) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `isTeacher` int(5) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `posttheme_id` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posttheme`
--

LOCK TABLES `posttheme` WRITE;
/*!40000 ALTER TABLE `posttheme` DISABLE KEYS */;
INSERT INTO `posttheme` VALUES (11,'我是第二个主题帖，大家快来','这是帖子的内容','2021-11-22 03:24:31',0),(13,'楼主区分以及贴子删除问题待解决','啦啦啦','2021-11-22 10:10:15',0),(18,'关于课程Web Service的大作业','参考：https://blog.csdn.net/xjzjyx_/article/details/104259718','2021-11-23 01:40:28',0),(19,'目前的问题 总结','rt','2021-11-23 01:43:26',0),(32,'测试','','2021-12-02 00:47:31',0),(33,'测试','','2021-12-02 00:48:58',0),(35,'关于放假的通知','学校将于1月16日放假，2月28日开学','2021-12-02 00:56:24',1),(37,'admin','admin','2021-12-07 12:12:05',1),(42,'关于系统维护的通知','本站将于2021年12月07日至2021年12月08日维护，敬请谅解！','2021-12-07 12:48:06',2),(46,'学期已经即将结束，请同学们及时复习，完成任务。','','2021-12-09 15:47:07',1),(47,'新的页面','<h1>	<strong>	生如夏花之绚烂，死如秋叶之静美</strong></h1>','2021-12-10 19:39:05',0),(49,'关于富文本导入的问题','<p><strong>这里html会显示&lt;strong&gt;</strong></p><p><em>这里会显示斜体</em></p><p><u>这里会显示下划线</u></p>','2021-12-11 10:40:39',0),(87,'数据库考试在即','<h1>希望大家认真复习！</h1><h2><br></h2><h2><br></h2><h2>数据库的基本知识</h2>','2021-12-12 21:09:11',1),(88,'大家注意在第15周上交体育书面作业','<p>如题</p>','2021-12-12 21:34:00',1),(89,'求推荐大三下学期的课程','<p>如题，不知道大三下都有什么课</p>','2021-12-12 21:58:49',0);
/*!40000 ALTER TABLE `posttheme` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `posttheme_delete` BEFORE DELETE ON `posttheme` FOR EACH ROW BEGIN
		DECLARE type int;
		DECLARE sid VARCHAR(255);
		SET type = old.isTeacher;
		if type = 0 THEN
			SET sid = (SELECT student_id FROM student_posttheme where posttheme_id=old.id);
			UPDATE student SET count_discuss = count_discuss - 1 where id=sid;
		ELSEIF type = 1 THEN
			SET sid = (SELECT teacher_id FROM teacher_posttheme where posttheme_id=old.id);
			UPDATE teacher SET count_discuss = count_discuss - 1 where id=sid;
		END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `post_posttheme_delete` BEFORE DELETE ON `posttheme` FOR EACH ROW BEGIN
	DELETE FROM post where id IN
	(SELECT post_id from post_posttheme WHERE posttheme_id=old.id);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `count_course` int(10) DEFAULT '0',
  `count_comment` int(10) DEFAULT '0',
  `count_discuss` int(10) DEFAULT '0',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `student_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('123','123456','王五',0,0,0),('19373135','123456','田旗舰',6,3,2),('19373136','123456','郭明明',6,7,14),('19373686','12345678','欧阳奎',5,2,5),('19373889','123456','白也歌',3,0,1),('stu0','123456','张三',0,0,0),('stu1','123','李四',0,0,0);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_comment`
--

DROP TABLE IF EXISTS `student_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_comment` (
  `student_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `comment_id` int(20) NOT NULL,
  PRIMARY KEY (`student_id`,`comment_id`),
  KEY `sco` (`comment_id`,`student_id`) USING BTREE,
  CONSTRAINT `sco_comment_f` FOREIGN KEY (`comment_id`) REFERENCES `comment` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sco_student_f` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_comment`
--

LOCK TABLES `student_comment` WRITE;
/*!40000 ALTER TABLE `student_comment` DISABLE KEYS */;
INSERT INTO `student_comment` VALUES ('19373135',21),('19373135',124),('19373135',125),('19373136',11),('19373136',18),('19373136',32),('19373136',34),('19373136',120),('19373136',122),('19373136',123),('19373686',46),('19373686',50);
/*!40000 ALTER TABLE `student_comment` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `stu_commentNum_insert` AFTER INSERT ON `student_comment` FOR EACH ROW BEGIN
	UPDATE student SET count_comment = count_comment + 1 
	where id=new.student_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `stu_commentNum_delete` BEFORE DELETE ON `student_comment` FOR EACH ROW BEGIN
	UPDATE student SET count_comment = count_comment - 1 
	where id=old.student_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `student_course`
--

DROP TABLE IF EXISTS `student_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_course` (
  `student_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `course_id` int(20) NOT NULL,
  PRIMARY KEY (`student_id`,`course_id`) USING BTREE,
  KEY `sc` (`course_id`,`student_id`) USING BTREE,
  CONSTRAINT `sc_course_f` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sc_student_f` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_course`
--

LOCK TABLES `student_course` WRITE;
/*!40000 ALTER TABLE `student_course` DISABLE KEYS */;
INSERT INTO `student_course` VALUES ('19373135',26),('19373135',42),('19373135',68),('19373135',75),('19373135',76),('19373135',106),('19373136',26),('19373136',42),('19373136',83),('19373136',104),('19373136',105),('19373136',118),('19373686',26),('19373686',42),('19373686',76),('19373686',103),('19373686',104),('19373889',42),('19373889',68),('19373889',76);
/*!40000 ALTER TABLE `student_course` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `stu_courseNum_insert` AFTER INSERT ON `student_course` FOR EACH ROW BEGIN
	UPDATE student SET count_course = count_course + 1  
	where id=new.student_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `stu_courseNum_delete` BEFORE DELETE ON `student_course` FOR EACH ROW BEGIN
	UPDATE student SET count_course = count_course - 1 
	where id=old.student_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `student_post`
--

DROP TABLE IF EXISTS `student_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_post` (
  `student_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `post_id` int(20) NOT NULL,
  PRIMARY KEY (`student_id`,`post_id`),
  KEY `sp` (`post_id`,`student_id`) USING BTREE,
  CONSTRAINT `sp_post_f` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sp_student_f` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_post`
--

LOCK TABLES `student_post` WRITE;
/*!40000 ALTER TABLE `student_post` DISABLE KEYS */;
INSERT INTO `student_post` VALUES ('19373136',11),('19373136',12),('19373136',25),('19373136',26),('19373136',27),('19373136',34),('19373136',37),('19373136',69),('19373136',74),('19373136',75),('19373136',119),('19373686',22),('19373686',77),('19373686',78),('19373889',118);
/*!40000 ALTER TABLE `student_post` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `student_post_insert` AFTER INSERT ON `student_post` FOR EACH ROW BEGIN
	UPDATE student SET count_discuss = count_discuss + 1 
	where id=new.student_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `student_posttheme`
--

DROP TABLE IF EXISTS `student_posttheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_posttheme` (
  `student_id` varchar(255) NOT NULL,
  `posttheme_id` int(20) NOT NULL,
  PRIMARY KEY (`student_id`,`posttheme_id`),
  KEY `spt` (`posttheme_id`,`student_id`) USING BTREE,
  CONSTRAINT `spt_posttheme_f` FOREIGN KEY (`posttheme_id`) REFERENCES `posttheme` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `spt_student_f` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_posttheme`
--

LOCK TABLES `student_posttheme` WRITE;
/*!40000 ALTER TABLE `student_posttheme` DISABLE KEYS */;
INSERT INTO `student_posttheme` VALUES ('19373135',13),('19373135',89),('19373136',11),('19373136',18),('19373136',19),('19373686',47),('19373686',49);
/*!40000 ALTER TABLE `student_posttheme` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `student_posttheme` AFTER INSERT ON `student_posttheme` FOR EACH ROW BEGIN
	UPDATE student SET count_discuss = count_discuss + 1 
	where id=new.student_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `count_discuss` int(10) DEFAULT '0',
  `count_course` int(10) DEFAULT '0',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `teacher_id` (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES ('123','123456','王老师',0,1),('Anchor','12345','Anchor',0,0),('t19373135','123456','田老师',0,4),('t19373136','123456','郭老师',2,1),('t19373686','123456','欧老师',2,3),('t19375211','123456','赵老师',0,1),('t19379888','123456','王翔老师',0,4),('tea0','123','李老师',0,0),('teacher01','123456','欧阳老师',0,2),('wang123','123456','体育王老师',1,1);
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_course`
--

DROP TABLE IF EXISTS `teacher_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher_course` (
  `teacher_id` varchar(255) NOT NULL,
  `course_id` int(20) NOT NULL,
  PRIMARY KEY (`teacher_id`,`course_id`),
  KEY `tc` (`course_id`,`teacher_id`) USING BTREE,
  CONSTRAINT `tc_course_f` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tc_teacher_f` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_course`
--

LOCK TABLES `teacher_course` WRITE;
/*!40000 ALTER TABLE `teacher_course` DISABLE KEYS */;
INSERT INTO `teacher_course` VALUES ('123',106),('t19373135',68),('t19373135',75),('t19373135',87),('t19373135',108),('t19373136',76),('t19373686',26),('t19373686',83),('t19373686',109),('t19375211',118),('t19379888',102),('t19379888',103),('t19379888',104),('t19379888',105),('teacher01',42),('teacher01',79),('wang123',122);
/*!40000 ALTER TABLE `teacher_course` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `teacher_course_insert` AFTER INSERT ON `teacher_course` FOR EACH ROW BEGIN
	UPDATE teacher set count_course = count_course + 1 
	where id=new.teacher_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `teacher_material`
--

DROP TABLE IF EXISTS `teacher_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher_material` (
  `teacher_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `material_id` int(20) NOT NULL,
  PRIMARY KEY (`material_id`,`teacher_id`),
  KEY `tm` (`teacher_id`,`material_id`) USING BTREE,
  CONSTRAINT `tm_material_f` FOREIGN KEY (`material_id`) REFERENCES `material` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tm_teacher_f` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_material`
--

LOCK TABLES `teacher_material` WRITE;
/*!40000 ALTER TABLE `teacher_material` DISABLE KEYS */;
INSERT INTO `teacher_material` VALUES ('t19373135',1),('teacher01',48),('t19373136',82),('t19373136',84),('t19373135',97),('t19373135',98),('t19373135',101),('t19373136',102),('t19373136',103),('t19373135',104),('t19373135',105),('t19379888',106),('t19379888',107),('t19379888',108),('t19373135',110),('t19375211',112),('wang123',113);
/*!40000 ALTER TABLE `teacher_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_post`
--

DROP TABLE IF EXISTS `teacher_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher_post` (
  `teacher_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `post_id` int(20) NOT NULL,
  PRIMARY KEY (`teacher_id`,`post_id`) USING BTREE,
  KEY `tp` (`post_id`,`teacher_id`) USING BTREE,
  CONSTRAINT `tp_post_f` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tp_teacher_f` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_post`
--

LOCK TABLES `teacher_post` WRITE;
/*!40000 ALTER TABLE `teacher_post` DISABLE KEYS */;
INSERT INTO `teacher_post` VALUES ('t19373686',82);
/*!40000 ALTER TABLE `teacher_post` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `teacher_post_insert` AFTER INSERT ON `teacher_post` FOR EACH ROW BEGIN
	UPDATE teacher SET count_discuss = count_discuss + 1 
	where id=new.teacher_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `teacher_posttheme`
--

DROP TABLE IF EXISTS `teacher_posttheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher_posttheme` (
  `teacher_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `posttheme_id` int(20) NOT NULL,
  PRIMARY KEY (`teacher_id`,`posttheme_id`) USING BTREE,
  KEY `tpt` (`posttheme_id`,`teacher_id`) USING BTREE,
  CONSTRAINT `tpt_posttheme_f` FOREIGN KEY (`posttheme_id`) REFERENCES `posttheme` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tpt_teacher_f` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_posttheme`
--

LOCK TABLES `teacher_posttheme` WRITE;
/*!40000 ALTER TABLE `teacher_posttheme` DISABLE KEYS */;
INSERT INTO `teacher_posttheme` VALUES ('t19373136',35),('t19373136',46),('t19373686',87),('wang123',88);
/*!40000 ALTER TABLE `teacher_posttheme` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `teacher_posttheme_insert` AFTER INSERT ON `teacher_posttheme` FOR EACH ROW BEGIN
	UPDATE teacher SET count_discuss = count_discuss + 1 
	where id=new.teacher_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test` (
  `a` int(255) NOT NULL,
  PRIMARY KEY (`a`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
INSERT INTO `test` VALUES (2),(22);
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-12 22:01:24
