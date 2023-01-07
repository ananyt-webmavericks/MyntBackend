/*GENERATED QUERIES*/
create database `livewell_myinvest_db`;
use `livewell_myinvest_db`;
/*SIGN UP */
CREATE TABLE `mt_user_signupmodel` (
  `id` int NOT NULL AUTO_INCREMENT,
  `FIRSTNAME` varchar(150) NOT NULL,
  `LASTNAME` varchar(150) NOT NULL,
  `EMAIL` varchar(250) NOT NULL,
  `SCHOOL` varchar(500) NOT NULL,
  `PASSWORD` varchar(6) NOT NULL,
  `CONPASSWORD` varchar(6) NOT NULL,
  `ROLE` varchar(50) NOT NULL,
  `MODULE` varchar(50) NOT NULL,
  `AGREECHK` varchar(1) NOT NULL,
  `STATUS` varchar(50) NOT NULL,
  `COMMENTS` varchar(250) NOT NULL,
  `DESCRIPTION` varchar(250) NOT NULL,
  `CREATED_USER` varchar(150) NOT NULL,
  `CREATED_DATE` date NOT NULL,
  `MODIFIED_USER` varchar(150) NOT NULL,
  `MODIFIED_DATE` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
/***********************************************************************
    MODULE : STARTUP 
************************************************************************/
/*COMPANY INFORMATION*/
CREATE TABLE `mt_startup_companyinfo_companyinfomodel` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `MTUSER_ID` varchar(250) NOT NULL,
  `EMAIL` varchar(250) NOT NULL,
  `MODULE` varchar(50) NOT NULL,
  `COUNTRY` varchar(150) NOT NULL,
  `STATE` varchar(150) NOT NULL,
  `CITY` varchar(75) NOT NULL,
  `PINCODE` varchar(50) NOT NULL,
  `ADDRESS` varchar(500) NOT NULL,
  `COMPANY_WEBSITE` varchar(250) NOT NULL,
  `FB_LINK` varchar(500) NOT NULL,
  `INSTA_LINK` varchar(500) NOT NULL,
  `LINKEDIN_LINK` varchar(500) NOT NULL,
  `LEGAL_NAME` varchar(250) NOT NULL,
  `CIN_NUMBER` varchar(250) NOT NULL,
  `DATE_OF_INCORPORATATION` date NOT NULL,
  `INCORPORATION_TYPE` varchar(500) NOT NULL,
  `ABOUT_COMPANY` varchar(500) NOT NULL,
  `AMOUNT_INVESTED` varchar(500) NOT NULL,
  `NO_OF_EMPLOYEES` varchar(150) NOT NULL,
  `STATUS` varchar(50) NOT NULL,
  `COMMENTS` varchar(250) NOT NULL,
  `DESCRIPTION` varchar(250) NOT NULL,
  `CREATED_USER` varchar(150) NOT NULL,
  `CREATED_DATE` date NOT NULL,
  `MODIFIED_USER` varchar(150) NOT NULL,
  `MODIFIED_DATE` date NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
/*TEAM INFORMATION*/
CREATE TABLE `mt_startup_teaminfo_teaminfomodel` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `MTUSER_ID` varchar(250) NOT NULL,
  `EMAIL` varchar(250) NOT NULL,
  `MODULE` varchar(50) NOT NULL,
  `TEAM_SNO` varchar(50) NOT NULL,
  `TEAM_MEMBER_NAME` varchar(150) NOT NULL,
  `TEAM_MEMBER_POSITION` varchar(150) NOT NULL,
  `FB_LINK` varchar(500) NOT NULL,
  `INSTA_LINK` varchar(500) NOT NULL,
  `LINKEDIN_LINK` varchar(500) NOT NULL,
  `TEAM_BIO` varchar(500) NOT NULL,
  `PROFILE_PIC` blob,
  `STATUS` varchar(50) NOT NULL,
  `COMMENTS` varchar(250) NOT NULL,
  `DESCRIPTION` varchar(250) NOT NULL,
  `CREATED_USER` varchar(150) NOT NULL,
  `CREATED_DATE` date NOT NULL,
  `MODIFIED_USER` varchar(150) NOT NULL,
  `MODIFIED_DATE` date NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci