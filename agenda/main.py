from ttkbootstrap import Window
from agenda_app import AgendaApp
import db

if __name__ == "__main__":
    db.criar_tabelas()
    db.cadastrar_medicos()
    root = Window(themename="superhero")
    app = AgendaApp(root)
    root.mainloop()
