instructions = [
  instructions = [
    'DROP TABLE IF EXISTS hecho;',
    """
        CREATE TABLE hecho (
            id INT PRIMARY KEY AUTO_INCREMENT,
            hecho  VARCHAR(100) NOT NULL,
            estado VARCHAR(45) NOT NULL
             );

        """
        'DROP TABLE IF EXISTS usuario;',
    """
        CREATE TABLE usuario (
            id INT PRIMARY KEY AUTO_INCREMENT,
            user  VARCHAR(50) NOT NULL,
            password VARCHAR(102) NOT NULL
        )
        """
    
]
    
 
