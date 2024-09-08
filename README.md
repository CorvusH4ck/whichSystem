# whichSystem

# Sistema Operativo por TTL :mag:

Este script intenta identificar el sistema operativo de un dispositivo remoto utilizando el valor TTL (Time-to-Live) de una solicitud de `ping`. Basado en el valor TTL, se determina si el sistema operativo es **Linux**, **Windows**, o si no se puede identificar (**Not Found**). Además, el script muestra el resultado con iconos y colores utilizando **Nerd Fonts**.

## Características

- **Identificación del sistema operativo** basado en el TTL del `ping`.
- **Soporte de iconos** utilizando Nerd Fonts.
- **Colores** personalizados para los sistemas operativos:
  - **Linux**: Amarillo :yellow_heart:
  - **Windows**: Azul :blue_heart:
  - **No encontrado**: Rojo :heart:
- **Opción de ayuda** `-h` o `--help` que explica cómo utilizar el script.

## Requisitos

- **Python 3.x**
- **Nerd Fonts** instaladas y configuradas en la terminal para visualizar los iconos correctamente.
- **Terminal con soporte para secuencias ANSI** para mostrar los colores.

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```

2. Entra en el directorio del proyecto:

   ```bash
   cd tu-repositorio
   ```

3. Mueve el archivo del script a `/usr/bin/` para que pueda ser ejecutado desde cualquier lugar:

   ```bash
   sudo mv wichSystem.py /usr/bin/wichSystem
   ```

4. Dale permisos de ejecución al archivo:

   ```bash
   sudo chmod +x /usr/bin/wichSystem
   ```

5. Ahora puedes ejecutar el script desde cualquier ubicación en tu terminal:

   ```bash
   wichSystem <direccion-ip>
   ```

## Uso

### Mostrar la ayuda

Puedes ejecutar el siguiente comando para mostrar una breve explicación de cómo usar el script:

```bash
wichSystem -h
```

Salida esperada:

```
Uso:
    wichSystem <direccion-ip>

Descripción:
    Este script intenta identificar el sistema operativo de un dispositivo remoto
    basado en el valor TTL de una solicitud de ping.

Opciones:
    -h, --help    Muestra esta ayuda y sale.

Ejemplo:
    wichSystem 192.168.1.1
```

### Ejemplo de uso

Para identificar el sistema operativo de una IP específica:

```bash
wichSystem 192.168.1.1
```

El script devolverá algo como:

```
192.168.1.1 (ttl -> 64): Linux 🐧
```

