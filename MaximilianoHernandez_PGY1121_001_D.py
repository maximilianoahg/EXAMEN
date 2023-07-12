import datetime 

cont_a, cont_b, cont_c, cont_d= 0,0,0,0
total_a, total_b, total_c, total_d= 0,0,0,0

run_cliente = []

total = total_a + total_b + total_c + total_d
total_cont = cont_a + cont_b + cont_c + cont_d


departamento = [['A10', 'B10', 'C10', '10D'],
               ['A9', 'B9', 'C9', 'D9'],
               ['A8', 'B8', 'C8', 'D8'],
               ['A7', 'B7', 'C7', 'D7'],
               ['A6', 'B6', 'C6', 'D6'],
               ['A5', 'B5', 'C5', 'D5'],
               ['A4', 'B4', 'C4', 'D4'],
               ['A3', 'B3', 'C3', 'D3'],
               ['A2', 'B2', 'C2', 'D2'],
               ['A1', 'B1', 'C1', 'D1']]


def menu():
  print('''  -------------------------------
    INMOBILIARIA CASA FELIZ
  -------------------------------
  Seleccione una opción:

  1.- Comprar Departamento

  2.- Mostrar Departamentos Disponibles

  3.- Ver listado de compradores

  4.- Mostrar ganancias totales

  5.- Salir
  -------------------------------
  ''')



def comprar_departamento(departamento_comprar):
  flag = True

  while flag:
    for fila in range(len(departamento)):
      for elemento_actual in range(len(departamento[fila])):
        if departamento[fila][elemento_actual] == 'X':
          print('\nNO ESTA DISPONIBLE')
          flag = False
          
    
    for fila in range(len(departamento)):
      for elemento_actual in range(len(departamento[fila])):
        if departamento[fila][elemento_actual] == departamento_comprar:
          departamento[fila][elemento_actual] = 'X'
          flag = False
        
def mostrar_departamentos():
  print('''\n  -------------------------------
  LISTADO DE DEPARTAMENTO
  -------------------------------
  ''')
  for fila in range(len(departamento)):
    for elemento_actual in range(len(departamento[fila])):
      print('  ',departamento[fila][elemento_actual], end=' ')
    print('\n')

def mostrar_compradores(run_cliente):
  print('''\n  -------------------------------
  MOSTRAR COMPRADORES
  -------------------------------
  ''')
  run_cliente.sort()
  for i in range(len(run_cliente)):
    print(run_cliente[i])
    print('\n')
  
  

def mostrar_ganancias():
  print('''\n  -------------------------------
  GANANCIAS TOTALES
  -------------------------------
  ''')
  for fila in range(len(venta_total)):
    for elemento_actual in range(len(venta_total[fila])):
      print('  ', venta_total[fila][elemento_actual], end=' ')
    print('\n')
  
def exit():
  now = datetime.date.today()
  print(f'''
  GRACIAS POR USAR EL PROGRAMA

  MAXIMILIANO HERNANDEZ
  
  {now}
  ''')

while True:
  menu()
  op=int(input('  Seleccione una opcion: '))
  
  while op < 1 or op > 5:
    print('\n  ERROR! SELECIONE UNA OPCIÓN ENTRE 1 A 5')
    op=int(input('\n  Seleccione una opcion: '))

  if op == 1:
    print('''\n  -------------------------------
    COMPRAR DEPARTAMENTO
    -------------------------------
    ''')
    mostrar_departamentos()
    
    
    piso = int(input('Ingrese el piso del departamento: '))
    
    while piso < 1 or piso > 10:
      print('\n  ERROR! SELECIONE UNA OPCIÓN ENTRE 1 A 10')
      piso = int(input('\nIngrese el piso del departamento: '))
    piso = str(piso)
    
    tipo_departamento = str(input('\nIngrese tipo de departamento: '))
    tipo_departamento = tipo_departamento.upper()
    
    while tipo_departamento != 'A' and tipo_departamento != 'B' and tipo_departamento != 'C' and tipo_departamento != 'D':
      print('\n  ERROR! SELECIONE UNA OPCIÓN ENTRE A, B, C y D')
      tipo_departamento = str(input('\nIngrese tipo de departamento: '))
      tipo_departamento = tipo_departamento.upper()

    rut = int(input('\nIngrese su rut: '))
    run_cliente.append(rut)

    departamento_comprar = tipo_departamento + piso
    
    comprar_departamento(departamento_comprar)

    if tipo_departamento == 'A':
      cont_a+= 1
      total_a+= 3800
    elif tipo_departamento == 'B':
      cont_b+= 1
      total_b+= 3000
    elif tipo_departamento == 'C':
      cont_c+= 1
      total_c+= 2800
    elif tipo_departamento == 'D':
      cont_d+= 1
      total_d+= 3500
  
  elif op == 2:
    mostrar_departamentos()
  elif op == 3:
    mostrar_compradores(run_cliente)
    
  elif op == 4:
    venta_total = [['Tipo A 3800UF', cont_a, total_a],
              ['Tipo B 3000UF', cont_b, total_b],
              ['Tipo C 2800UF', cont_c, total_c],
              ['Tipo D 3500UF', cont_d, total_d],
              ['TOTAL        ', total_cont, total]]
    
    mostrar_ganancias()

  elif op == 5:
    exit()
    break
