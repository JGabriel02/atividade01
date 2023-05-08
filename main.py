from desktop import Desktop
from notebook import Notebook

desktop = Desktop("Dell Inspiron", "Preto", 3500.0, 500)
notebook = Notebook("Lenovo Ideapad", "Prata", 2500.0, 8)

print(desktop.getInformacoes()) 
print(notebook.getInformacoes())