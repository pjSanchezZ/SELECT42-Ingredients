CREATE PROCEDURE Fuckcxt (IN Recipe_Id VARCHAR(50))
    BEGIN
        DECLARE done int default 0;
        DECLARE tid INT(11);
        DECLARE pid VARCHAR(25);
        DECLARE pri DOUBLE;

        DECLARE procur CURSOR FOR (SELECT a.Type_Id, a.Product_Id, a.Price
                                   FROM (pages_recipe NATURAL JOIN pages_recipe_ingredients NATURAL JOIN pages_product_info) a
                                   WHERE a.Recipe_Id = Recipe_Id);
        DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
        
        DROP TABLE IF EXISTS FinalTable;
        
        CREATE TABLE FinalTable(
            Type_Id INT(11);
            Product_Id VARCHAR(25);
            Price DOUBLE
        );

        DROP TABLE IF EXISTS MaxTable;
        
        CREATE TABLE MaxTable(
            Type_Id INT(11);
            MaxPrice DOUBLE
        );
        
        OPEN procur;
        
        REPEAT
            FETCH procur INTO tid, pid, pri;
            INSERT INTO FinalTable VALUES (pro);
        UNTIL done
        END REPEAT;
        
        close procur;
        
        INSERT INTO MaxTable(Type_Id, MaxPrice) SELECT Type_Id, MAX(Price)
        FROM FinalTable
        GROUP BY Type_Id

        SELECT Product_Id
        FROM FinalTable a
        WHERE Price IN (
            SELECT MaxPrice
            FROM MaxTable
            WHERE a.Type_Id = Type_Id
        )

    END;