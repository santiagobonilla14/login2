instructions = [
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS hechos;',
    'DROP TABLE IF EXISTS usuario;',
    'SET FOREIGN_KEY_CHECKS=1;',

    """
        CREATE TABLE usuario (
            id INT PRIMARY KEY AUTO_INCREMENT,
            username  VARCHAR(50) NOT NULL,
            password VARCHAR(102) NOT NULL
        )
    """
    ,
    """
        CREATE TABLE hechos (
            id INT PRIMARY KEY AUTO_INCREMENT,
            hecho  VARCHAR(100) NOT NULL,
            estado VARCHAR(45) NOT NULL,
            created_by INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            completed BOOLEAN NOT NULL,
            FOREIGN KEY (created_by) REFERENCES usuario (id)
           
            )
"""
]
