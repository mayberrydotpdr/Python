 


SHOW CREATE TABLE all_finesse_tools;

SHOW CREATE DATABASE scrapy;

https://dba.stackexchange.com/questions/24371/how-to-import-a-sql-file-in-mysql
mysqldump --no-data --skip-comments --host=your_database_hostname_or_ip.com -u your_username --password=your_password your_database_name penguins > penguins.sql
mysqldump scrapy all_finesse_tools.sql


CREATE TABLE `all_finesse_tools` (
  `product_title` varchar(255) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `description` text,
  `product_code` varchar(50) DEFAULT NULL,
  `image_urls` text,
  `url` varchar(255) DEFAULT NULL,
  `project` varchar(50) DEFAULT NULL,
  `spider` varchar(50) DEFAULT NULL,
  `server` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  UNIQUE (product_title)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


Could not get this to work:
https://stackoverflow.com/questions/11407349/mysql-how-to-export-and-import-a-sql-file-from-command-line
https://stackoverflow.com/questions/32737478/how-should-i-tackle-secure-file-priv-in-mysql
cd to:  secure-file-priv="C:/ProgramData/MySQL/MySQL Server 5.7/Uploads"
Then Run One of the Fallowing:
mysql -u username -p -h localhost DATA-BASE-NAME < data.sql
mysqlimport scrapy all_finesse_tools.sql
mysql -u root -p -h localhost scrapy < all_finesse_tools.sql

Example INSERT INTO `all_finesse_tools` Statement:
INSERT INTO `all_finesse_tools` (`product_title`,`price`,`description`,`product_code`,`image_urls`,`url`,`project`,`spider`,`server`,`date`) VALUES ('John Highley Basic Tactical 22 Piece Set','$1,875.00','John Highley Basic Tactical 22 piece Set This all new 22 Piece Basic Tactical Set Was assembled by John Highley, Ike Rhoades, and Jason Mayberry at John\'s shop in Ohio. The intention behind this set is to provide a new tech in training an essential set of professional grade tools that is well-rounded for door ding or hail repair. We believe that you will save time and money by purchasing this strategically assembled set, because purchasing the right tools for the job the first time is always the shortest route to success. Let’s have some fun and make some money! 270 JH MT Sharp Rod Set of 5 113 04 53 W 32 Tip Set 54 - $75 232 MR 36-24 Door Tool 57W 52w \xad Wooden knock down paddle Black Knockdown Plastic Window Guard','Product Code: John Highley Tactical Set',"'http://pdrfinessetools.com/image/cache/catalog/jason_added/Finesse_Starter-250x250.jpg'",'http://pdrfinessetools.com/By%20Design/Tools%20Sets/Complete%20Tool%20Sets/John%20Highley%20Basic%20Tactical%2022%20piece%20Set','properties','manual2','DESKTOP-U4HKUI7','2018-07-14 12:58:25');

Practice SELECT Statements:
select product_code from all_finesse_tools where product_code = 'Product Code: 99';
select product_title, product_code, price, url from all_finesse_tools;

Create HTML Tables Like This:
mysql -H -e "select product_title, product_code, price, url from all_finesse_tools" -u root -p scrapy
mysql -H -e "select image_urls from all_finesse_tools" -u root -p scrapy

From:  https://stackoverflow.com/questions/4685173/delete-all-duplicate-rows-except-for-one-in-mysql
INSERT INTO finesse_tools(product_title, price, description, product_code, image_urls, url, project, spider, server, date)
    SELECT DISTINCT product_title, price, description, product_code, image_urls, url, project, spider, server, date
    FROM all_finesse_tools;

select image_urls from all_finesse_tools where price = '$20.00' limit 0,2;

Nice Ordered List:
SELECT product_title, product_code, price FROM all_finesse_tools ORDER BY product_title;

SELECT product_title, product_code, price
FROM all_finesse_tools
ORDER BY product_title;





SELECT SUBSTRING_INDEX(image_urls,',',1), product_title, product_code, price
FROM all_finesse_tools
WHERE price = '$20.00'
# GROUP BY c1
# HAVING COUNT(c2)=4;
ORDER BY product_title;
+------------------------------------------------------------------------------------------------------------------------+----------------------------------+--------------------------+--------+
| SUBSTRING_INDEX(image_urls,',',1)                                                                                      | product_title                    | product_code             | price  |
+------------------------------------------------------------------------------------------------------------------------+----------------------------------+--------------------------+--------+
| 'http://pdrfinessetools.com/image/cache/catalog/trash%20tools/jan%202012%20images/new%20images/97-500x500-250x250.jpg' | #97- Sharp Tip Hand Ball Pusher  | Product Code: 97         | $20.00 |
| 'http://pdrfinessetools.com/image/cache/catalog/trash%20tools/jan%202012%20images/new%20images/98-500x500-250x250.jpg' | #98- Medium Tip Hand Ball Pusher | Product Code: 98         | $20.00 |
| 'http://pdrfinessetools.com/image/cache/catalog/trash%20tools/jan%202012%20images/new%20images/99-500x500-250x250.jpg' | #99- Round Tip Hand Ball Pusher  | Product Code: 99         | $20.00 |
| 'http://pdrfinessetools.com/image/cache/catalog/new%20tools/big%20hammer%20tip-250x250.JPG'                            | 1 Inch Polished Flat Tip         | Product Code: ft         | $20.00 |
| 'http://pdrfinessetools.com/image/cache/catalog/new%20tools/hammer%20tip-250x250.JPG'                                  | 1/2 Inch Polished Flat Tip       | Product Code: 1/2ft      | $20.00 |
| 'http://pdrfinessetools.com/image/cache/catalog/new%20tools/doorstrap-500x500-250x250.jpg'                             | Door Strap                       | Product Code: Door Strap | $20.00 |
| 'http://pdrfinessetools.com/image/cache/catalog/new%20tools/hood%20prop%20large-250x250.JPG'                           | Hood Prop                        | Product Code: PB22       | $20.00 |
| 'http://pdrfinessetools.com/image/cache/catalog/new%20tools/swivel-500x500-250x250.jpg'                                | S Hook With A Swivel             | Product Code: PB31       | $20.00 |
+------------------------------------------------------------------------------------------------------------------------+----------------------------------+--------------------------+--------+




SELECT CONCAT("<img src=", SUBSTRING_INDEX(image_urls,',',1), "></img>"), product_title, product_code, price
FROM all_finesse_tools
WHERE price = '$20.00'
ORDER BY product_title;
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+--------------------------+--------+
| CONCAT("<img src=", SUBSTRING_INDEX(image_urls,',',1), "></img>")                                                                      | product_title                    | product_code             | price  |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+--------------------------+--------+
| <img src='http://pdrfinessetools.com/image/cache/catalog/trash%20tools/jan%202012%20images/new%20images/97-500x500-250x250.jpg'></img> | #97- Sharp Tip Hand Ball Pusher  | Product Code: 97         | $20.00 |
| <img src='http://pdrfinessetools.com/image/cache/catalog/trash%20tools/jan%202012%20images/new%20images/98-500x500-250x250.jpg'></img> | #98- Medium Tip Hand Ball Pusher | Product Code: 98         | $20.00 |
| <img src='http://pdrfinessetools.com/image/cache/catalog/trash%20tools/jan%202012%20images/new%20images/99-500x500-250x250.jpg'></img> | #99- Round Tip Hand Ball Pusher  | Product Code: 99         | $20.00 |
| <img src='http://pdrfinessetools.com/image/cache/catalog/new%20tools/big%20hammer%20tip-250x250.JPG'></img>                            | 1 Inch Polished Flat Tip         | Product Code: ft         | $20.00 |
| <img src='http://pdrfinessetools.com/image/cache/catalog/new%20tools/hammer%20tip-250x250.JPG'></img>                                  | 1/2 Inch Polished Flat Tip       | Product Code: 1/2ft      | $20.00 |
| <img src='http://pdrfinessetools.com/image/cache/catalog/new%20tools/doorstrap-500x500-250x250.jpg'></img>                             | Door Strap                       | Product Code: Door Strap | $20.00 |
| <img src='http://pdrfinessetools.com/image/cache/catalog/new%20tools/hood%20prop%20large-250x250.JPG'></img>                           | Hood Prop                        | Product Code: PB22       | $20.00 |
| <img src='http://pdrfinessetools.com/image/cache/catalog/new%20tools/swivel-500x500-250x250.jpg'></img>                                | S Hook With A Swivel             | Product Code: PB31       | $20.00 |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+--------------------------+--------+






CREATE TABLE `finesse_tools_printable` (
  `img` varchar(255) DEFAULT NULL,
  `product_title` varchar(255) DEFAULT NULL,
  `product_code` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  UNIQUE (product_title)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

INSERT INTO finesse_tools_printable(img, product_title, product_code, price)
SELECT CONCAT("<img src=", SUBSTRING_INDEX(image_urls,',',1), " class=\"thumbnails\"></img>"), product_title, product_code, price
FROM all_finesse_tools
ORDER BY product_title;

mysql -H -e "SELECT img, product_title, product_code, price FROM finesse_tools_printable ORDER BY product_title" -u root -p scrapy





#### I had good luck with this!
CREATE TABLE `finesse_booklet` (
  `img` varchar(255) DEFAULT NULL,
  `product_title` varchar(255) DEFAULT NULL,
  `product_code` varchar(255) DEFAULT NULL,
  UNIQUE (product_title)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

INSERT INTO finesse_booklet(img, product_title, product_code)
SELECT CONCAT("<img src=", SUBSTRING_INDEX(image_urls,',',1), " class=\"thumbnails\"></img>"), 
CONCAT("<h1>", product_title, "</h1><pre>      </pre><span class=\"price\">", price, "</span>"), 
CONCAT("<a href=\"", url, "\" target=\"_blank\">", product_code, "</a>")
FROM all_finesse_tools
ORDER BY product_title;

mysql -H -e "SELECT img, product_title, product_code FROM finesse_booklet ORDER BY product_title" -u root -p scrapy











#####################################
#### Last Booklet Made 7-17-2018 ####
####   with finesse_booklet_v2   ####
#####################################
####    Try this new style!      ####
#####################################
CREATE TABLE `finesse_booklet_v2` (
  `img` varchar(255) DEFAULT NULL,
  `product_title` varchar(255) DEFAULT NULL,
  `product_code` varchar(255) DEFAULT NULL,
  UNIQUE (product_title)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

INSERT INTO finesse_booklet_v2(img, product_title, product_code)
SELECT CONCAT("<img src=", SUBSTRING_INDEX(image_urls,',',1), " class=\"thumbnails\"></img>"), 
CONCAT("<div class=\"spacer\"></div><h1> ", product_title, " <span class=\"price\"><span class=\"tilda\"> ~ </span> ", price, "</span></h1>"), 
CONCAT("<a href=\"", url, "\" target=\"_blank\">", product_code, "</a>")
FROM all_finesse_tools
ORDER BY product_title LIMIT 10;

mysql -H -e "SELECT img, product_title, product_code FROM finesse_booklet_v2 ORDER BY product_title" -u root -p scrapy

<html>
<head>
    <style>
        .thumbnails {
            width: 200px;
            height: auto;
        }
        .price {
            color: red;
            font-weight: bolder;
        }
        .tilda {
            color: transparent;
        }
        a {
            text-decoration: navy;
            text-decoration-line: none;
            font-size: 18pt;
            font-weight: bolder;
        }
    </style>
</head>    
<body>

###################################
####    End of new style!      ####
###################################









# While this looks like it shouuld work it will not!
mysql -H -e "
SELECT CONCAT("<img src=", SUBSTRING_INDEX(image_urls,',',1), " class=\"thumbnails\"></img>"), product_title, product_code, price FROM all_finesse_tools ORDER BY product_title
" -u root -p scrapy










SELECT image_urls, product_title, product_code, price

SELECT c1 
FROM table
WHERE c2 IN (1,2,3,4)
GROUP BY c1
HAVING COUNT(c2)=4;

SELECT SUBSTRING_INDEX(value,',',1) As value FROM ...
or
substring(str,1,instr(str,',')-1)

SELECT CONCAT(Address, " ", PostalCode, " ", City) AS Address
FROM Customers;