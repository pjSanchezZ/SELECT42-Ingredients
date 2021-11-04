CREATE TABLE `user`(
​	`User_Id` VARCHAR(25) PRIMARY KEY NOT NULL,
​	`First_Name` VARCHAR(25),
​	`Last_Name` VARCHAR(25),
​	`State` VARCHAR(25), 
​	`City` VARCHAR(25), 
​	`Address` VARCHAR(50), 
​	`Zip_Code` INT, 
​	`Phone_Number` INT, 
​	`Email` VARCHAR(50), 
​	`Daily_Calories` INT, 
​	`Daily_Protein` INT
);

/* this is a compromise version */
CREATE TABLE `wanted_item`(
​	`Product_Id` VARCHAR(25) NOT NULL, 
​	`User_Id` VARCHAR(25) NOT NULL, 
​	`Date` VARCHAR(25), 
​	`Price` REAL, 
​	`Quantity` INT
);

/* this is the original version that comes with unsettled error */
CREATE TABLE wanted_item(
​	Product_Id INT NOT NULL, 
​	User_Id INT NOT NULL, 
​	Date VARCHAR(25), 
​	Price REAL, 
​	Quantity INT, 
​	PRIMARY KEY (Product_Id, User_Id), 
​	FOREIGN KEY (Product_Id) REFERENCES product_info(Product_Id), 
​	FOREIGN KEY (User_Id) REFERENCES user(User_Id)
);

CREATE TABLE `product_info`(
​	`Product_Id` VARCHAR(25) PRIMARY KEY NOT NULL, 
​	`Product_Name` VARCHAR(50) REFERENCES nutrition_table(Product_Name),
​	`Price` REAL,  
​	`Product_Type` VARCHAR(50) REFERENCES product_type(Product_Type), 
​	`Seller_Id` VARCHAR(25)REFERENCES seller (Seller_Id), 
​	`Availability` BOOLEAN, 
​	`Image_Address` VARCHAR(100), 
​	`Description` VARCHAR(1024), 
​	`Discount` REAL, 
​	`Rating` REAL
);

CREATE TABLE `nutrition_table`(
​	`Product_Name` VARCHAR(50) PRIMARY KEY, 
​	`Calories` INT, 
​	`Protein` INT, 
​	`Carbohydrate` INT, 
​	`Fat` INT
);

CREATE TABLE `seller`(
​	`Seller_Id` VARCHAR(25) PRIMARY KEY, 
​	`Brand_Id` VARCHAR(25) REFERENCES brand(Brand_Id), 
​	`State` VARCHAR(25), 
​	`City` VARCHAR(25),
​	`Address` VARCHAR(50), 
​	`Zip_Code` INT, 
​	`Phone_Number` INT, 
​	`Email` VARCHAR(50), 
​	`Website_Address` VARCHAR(250)
);

CREATE TABLE `brand`(
​	`Brand_Id` VARCHAR(25) PRIMARY KEY,
​	`Brand_Name` VARCHAR(50),
​	`Rating` REAL
);

CREATE TABLE `product_type`(
​	`Product_Type_Id` INT PRIMARY KEY, 
​	`Product_Type` VARCHAR(50) REFERENCES product_info(Product_Type), 
​	`Classification` VARCHAR(50)
);

CREATE TABLE `recipe`(
​	`Dish_Id` INT PRIMARY KEY,
​	`Dish_Name` VARCHAR(50), 
​	`Calories` INT,
​	`Protein` INT,
​	`Carbohydrate` INT, 
​	`Fat` INT
);

CREATE TABLE `ingredient`(
​	`Record_Id` INT PRIMARY KEY,
​	`Dish_Id` INT REFERENCES recipe(Dish_Id),
​	`Ingred` VARCHAR(50) REFERENCES product_type(Product_Type)
);