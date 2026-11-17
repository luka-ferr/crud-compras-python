-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS crud_compras;

-- Seleccionar la base de datos
USE crud_compras;

-- Crear tabla de compras
CREATE TABLE IF NOT EXISTS compra (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(10,2) NOT NULL
);