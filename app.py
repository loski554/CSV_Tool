import ttkbootstrap as ttk
import logging

#Class qui permet l'initialisation et la configuration de la fenêtre.
class Application(ttk.Window):
    def __init__(self, data):

        #Configuration fenêtre
        super().__init__(themename = 'cosmo')
        self.title('Tableau utilisateurs')
        self.geometry('800x400')

        #Text titre
        label = ttk.Label(self, text = 'Utilisateurs valides:', font = 'Poppins 16 bold')
        label.pack(pady=10)

        #Création du tableau utilisateurs valide
        table = ttk.Treeview(self, columns = ('id', 'user', 'age', 'email'), show = 'headings', height=10)
        table.column('#1', anchor='center', width=100)
        table.column('#2', anchor='center')
        table.column('#3', anchor='center', width=100)
        table.column('#4', anchor='center')
        table.heading('id', text = 'ID')
        table.heading('user', text = 'User')
        table.heading('age', text = 'Age')
        table.heading('email', text = 'Email')
        table.pack(pady=20, padx=20)

        #Inserer les données dans le tableau
        for i in range(len(data)):
            table.insert(
                parent='',
                index=i,
                values=(i+1, data[i]['name'], data[i]['age'], data[i]['email'])
            )

        logging.info("Interface graphique lancée")