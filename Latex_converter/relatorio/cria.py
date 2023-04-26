import os

class Relatorio:
    template_dir = "../dados"
    def __init__(self, titulo, autor, template='cabeçalho.tex') -> None:
        self.cabeçalho=None
        self.titulo = titulo
        self.autor = autor
        self.inicializa()

    def inicializa(self):
        with open(os.path.join('..dados/cabeçalho.tex')) as f:
            self.cabeçalho = f.read()
