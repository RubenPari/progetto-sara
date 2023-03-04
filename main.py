import pandas as pd


def stampo_sup_pop_dens(df, provincia_regione):
    # chiedo all'utente di scegliere un'opzione
    scelta = input('''
            1. Stampa la superficie
            2. Stampa la popolazione
            3. Stampa la densità
        ''')

    match scelta:
        case '1':
            # stampo la superficie della regione
            print(df[df['Regione/Provincia'] == provincia_regione]['Superficie'])
        case '2':
            # stampo la popolazione della regione
            print(df[df['Regione/Provincia'] ==
                  provincia_regione]['Popolazione'])
        case '3':
            # stampo la densità della regione
            print(df[df['Regione/Provincia'] == provincia_regione]['Densità'])
        case _:
            # stampo un messaggio di errore
            print('Opzione non valida')


# importo i dati dal csv
df = pd.read_csv('dati_comunali_e_provinciali.csv', sep=';')

# stampa un menù di scielta per l'utente
print('''
    1. Stampa i dati di una provincia ( superficie, popolazione e densità)
    2. Stampa i dati di una regione ( superficie, popolazione e densità)
    3. Stampa la media della popolazione delle regioni
    4. Stampa il massimo della densità delle provincie
    5. Stampa il minimo della superficie di un comune
''')

scelta = input('Scegli un opzione: ')

match scelta:
    case '1':
        # chiedo all'utente di inserire il nome della provincia
        provincia = input('Inserisci il nome della provincia: ')

        # stampo uno dei dati della provincia
        stampo_sup_pop_dens(df, provincia)

    case '2':
        regione = input('Inserisci il nome della regione: ')

        # stampo uno dei dati della regione
        stampo_sup_pop_dens(df, regione)
    case '3':
        # TODO: fix
        # stampo la media della popolazione delle regioni
        print(df['Popolazione'].mean())

    case '4':
        # TODO: fix
        # stampo il massimo della densità delle provincie
        print(df['Densità'].max())

    case '5':
        # TODO: fix
        # stampo il minimo della superficie di un comune
        print(df['Superficie'].min())

    case _:
        # stampo un messaggio di errore
        print('Opzione non valida')
