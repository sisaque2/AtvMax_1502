from controller.usuario_controler import UsuarioController
from view.usuario_view import UsuarioViewWeb 

def main():

    controller = UsuarioController(None) 

    view = UsuarioViewWeb(controller)

    controller.view = view

    view.run()

if __name__ == "__main__":
    main()