import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
def get_list():
    return [1, 2, 3, 4]


@app.get("/contact", response_class=HTMLResponse)
def get_list():
    return """
    <html>
        <head>
            <title>Web FastAPI</title>
        </head>
        <body>
            <h1>¡Hola a todos!</h1>
            <p>Este es un texto de prueba para mi página</p>
            <p>Todos las mañanas al salir el sol, mamá me prepara chocolate "El Sol"</p>
            <p>ñdlfldfljdklfjds"</p>

        </body>
    </html>
    """


def run():
    store.get_categories()


if __name__ == "__main__":
    run()
