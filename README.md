# CRUD de Compras - Python y MySQL

## Descripción

Aplicación de consola desarrollada en Python que permite gestionar compras mediante operaciones CRUD (Crear, Consultar, Actualizar y Eliminar).

Se implementó con programación orientada a objetos (POO) y utiliza MySQL como sistema gestor de bases de datos para almacenar la información.

## Tecnologías utilizadas

- **Python:** lenguaje de programación utilizado para desarrollar la aplicación.
- **MySQL:** sistema gestor de bases de datos.
- **XAMPP:** entorno local para gestionar el servicio MySQL.
- **MySQL Connector:** librería para conectar Python con MySQL.
- **Git y GitHub:** herramientas para el control de versiones y almacenamiento del código fuente.

## Funcionalidades

El sistema permite realizar las siguientes operaciones:

1. **Registrar compras:** permite ingresar el nombre del producto, la cantidad y el precio unitario.
2. **Consultar compras:** muestra todas las compras registradas, incluyendo el valor total de cada una.
3. **Actualizar compras:** permite modificar la información de una compra mediante su identificador.
4. **Eliminar compras:** permite eliminar una compra utilizando su identificador.

## Estructura del proyecto

```text
crud-compras-python/
│
├── main.py
├── database.py
├── compra.py
├── compra_crud.py
├── database.sql
├── requirements.txt
├── .gitignore
└── README.md
```

## Base de datos

El proyecto utiliza una base de datos llamada `crud_compras`, que contiene la tabla `compra`.

### Estructura de la tabla

| Campo | Tipo | Descripción |
|---|---|---|
| id | INT | Identificador único y autoincremental |
| producto | VARCHAR(100) | Nombre del producto |
| cantidad | INT | Cantidad de unidades compradas |
| precio | DECIMAL(10,2) | Precio unitario del producto |

## Instalación y configuración

### 1. Requisitos previos

- Tener Python instalado.
- Tener XAMPP instalado.
- Tener MySQL iniciado desde el panel de control de XAMPP.

### 2. Clonar el repositorio

```bash
git clone https://github.com/luka-ferr/crud-compras-python.git
```

Ingresar a la carpeta:

```bash
cd crud-compras-python
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

1. Iniciar MySQL desde XAMPP.
2. Abrir phpMyAdmin.
3. Importar el archivo `database.sql`.
4. Verificar que se haya creado la base de datos `crud_compras` y la tabla `compra`.

### 5. Configurar la conexión

Verificar los parámetros de conexión en `database.py`:

```python
host="localhost"
user="root"
password=""
database="crud_compras"
```

Estos valores deben ajustarse según la configuración local de MySQL.

### 6. Ejecutar la aplicación

Desde la terminal, ejecutar:

```bash
python main.py
```

## Arquitectura del proyecto

El proyecto está organizado en módulos con responsabilidades específicas:

- **main.py:** contiene la clase principal de la aplicación, administra el menú y gestiona la interacción con el usuario.
- **database.py:** administra la conexión con la base de datos MySQL.
- **compra.py:** define el modelo de datos de una compra y el método para calcular su valor total.
- **compra_crud.py:** implementa las operaciones CRUD mediante consultas SQL.
