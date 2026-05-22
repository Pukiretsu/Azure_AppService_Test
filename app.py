import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Diseño responsivo y moderno con Tailwind CSS
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es" class="h-full bg-slate-50 text-slate-800 dark:bg-slate-900 dark:text-slate-100">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Azure App Service - Hello World</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="flex h-full flex-col items-center justify-center p-4 sm:p-6 lg:p-8">

    <main class="w-full max-w-md transform rounded-2xl bg-white p-8 shadow-xl transition-all hover:scale-[1.01] dark:bg-slate-800 dark:shadow-2xl border border-slate-100 dark:border-slate-700/50">
        <!-- Badge de Estado -->
        <div class="flex items-center gap-2 mb-6">
            <span class="relative flex h-3 w-3">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
            </span>
            <span class="text-xs font-semibold tracking-wider uppercase text-emerald-600 dark:text-emerald-400">
                Desplegado en Azure
            </span>
        </div>

        <!-- Título Principal -->
        <h1 class="text-4xl font-extrabold tracking-tight bg-gradient-to-r from-blue-600 to-indigo-500 bg-clip-text text-transparent dark:from-blue-400 dark:to-indigo-300 mb-2">
            Hello World!
        </h1>

        <!-- Contenido dinámico -->
        <p class="text-base text-slate-600 dark:text-slate-300 mb-6 leading-relaxed">
            Esta aplicación web de Python se está ejecutando de forma nativa dentro de un contenedor Linux en Azure App Service.
        </p>

        <!-- Divisor decorativo -->
        <div class="h-px w-full bg-slate-100 dark:bg-slate-700 mb-6"></div>

        <!-- Firma del Desarrollador -->
        <div class="flex items-center justify-between">
            <div>
                <p class="text-xs font-medium text-slate-400 uppercase tracking-wider">Desarrollador</p>
                <p class="text-lg font-bold text-slate-700 dark:text-slate-200">{{ nombre }}</p>
            </div>
            <!-- Botón interactivo de ejemplo -->
            <button onclick="saludar()" class="inline-flex items-center justify-center rounded-xl bg-blue-600 px-4 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 transition-colors duration-200">
                ¡Hola! 👋
            </button>
        </div>
    </main>

    <!-- Footer minimalista -->
    <footer class="mt-8 text-center text-xs text-slate-400 dark:text-slate-500">
        Integración Continua con GitHub Actions &bull; 2026
    </footer>

    <!-- Script simple para interactividad -->
    <script>
        function saludar() {
            alert("¡Saludos desde los servidores de Azure! El despliegue automático está funcionando a la perfección.");
        }
    </script>
</body>
</html>
"""

@app.route('/')
def hello_world():
    # Tu nombre se inyecta dinámicamente en la plantilla
    nombre_usuario = "Angel Leonardo"
    return render_template_string(HTML_TEMPLATE, nombre=nombre_usuario)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
