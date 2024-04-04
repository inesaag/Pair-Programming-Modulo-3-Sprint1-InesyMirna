
query_creacion_bbdd = "CREATE SCHEMA IF NOT EXISTS `pair`;"

query_tabla_clientes = """
                    CREATE TABLE IF NOT EXISTS `pair`.`clientes` (
                    `id_cliente` INT NOT NULL,
                    `first_name` VARCHAR(45) NULL,
                    `last_name` VARCHAR(45) NULL,
                    `email` VARCHAR(45) NULL,
                    `gender` VARCHAR(45) NULL,
                    `city` VARCHAR(45) NULL,
                    `address` VARCHAR(45) NULL,
                    PRIMARY KEY (`id_cliente`));
                    """
                    
query_tabla_productos = """
                        CREATE TABLE IF NOT EXISTS `pair`.`productos` (
                        `id_producto` VARCHAR(45) NOT NULL,
                        `nombre_producto` VARCHAR(45) NULL,
                        `categoria` VARCHAR(45) NULL,
                        `precio` FLOAT NULL,
                        `origen` VARCHAR(45) NULL,
                        `descripcion` VARCHAR(500) NULL,
                        PRIMARY KEY (`id_producto`));

                        """
query_tabla_ventas = """
                        CREATE TABLE IF NOT EXISTS `pair`.`ventas` (
                        `id_cliente` INT NOT NULL,
                        `id_producto` VARCHAR(45) NULL,
                        `fecha_venta` DATE NULL,
                        `cantidad` INT NULL,
                        `total` VARCHAR(45) NULL);
                        """


                            
query_insertar_clientes = "INSERT INTO clientes (id_cliente, first_name, last_name, email, gender, city, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
query_insertar_productos = "INSERT INTO productos (id_producto, nombre_producto, categoria, precio, origen, descripcion) VALUES (%s, %s, %s, %s, %s, %s)"
query_insertar_ventas = "INSERT INTO ventas (id_cliente, id_producto, fecha_venta, cantidad, total) VALUES (%s, %s, %s, %s, %s)"




