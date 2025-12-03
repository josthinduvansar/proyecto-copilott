#!/usr/bin/env python3
"""
Servidor local simple para visualizar el blog de Tablas Hash
Uso: python server.py
Luego abre: http://localhost:8000
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Agregar headers para evitar problemas de caché
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    # Cambiar al directorio del script
    os.chdir(Path(__file__).parent)
    
    # Crear el servidor
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║                   SERVIDOR LOCAL ACTIVO                      ║
╚══════════════════════════════════════════════════════════════╝

📍 URL: http://localhost:{PORT}

📂 Directorio: {Path.cwd()}

📖 Abre tu navegador y ve a: http://localhost:{PORT}

⏹️  Para detener el servidor, presiona: Ctrl+C

╔══════════════════════════════════════════════════════════════╗
║              ¡Disfruta del blog de Tablas Hash!              ║
╚══════════════════════════════════════════════════════════════╝
        """)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Servidor detenido.")
            sys.exit(0)

if __name__ == "__main__":
    main()
