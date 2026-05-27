
# Curso: Fundamentos de Programación (213022)
# Evaluación Final POA - Fase 5
# Problema 3 - Auditoría de Inventario
# Enfoque: Estructurado con funciones y arreglos



def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    
    if stock_actual < stock_minimo:
        cantidad_final = stock_minimo - stock_actual
    else:
        cantidad_final = 0
        
    return cantidad_final


def generar_reporte_inventario():

    inventario = [
        ["ART01", "Teclado Mecánico", 12, 15],
        ["ART02", "Mouse Óptico", 25, 20],
        ["ART03", "Monitor 24''", 4, 8],
        ["ART04", "Cable HDMI 2m", 50, 30],
        ["ART05", "Diadema Gamer", 3, 10]
    ]
    
    print("-" * 55)
    print("        INFORME DE AUDITORÍA Y REABASTECIMIENTO")
    print("-" * 55)
    print(f"{'PRODUCTO':<25} | {'CANTIDAD A PEDIR':<15}")
    print("-" * 55)
    

    for fila in inventario:
        nombre_producto = fila[1]
        stock_actual = fila[2]
        stock_minimo = fila[3]
        
    
        pedido_requerido = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
     
        print(f"{nombre_producto:<25} | {pedido_requerido:<15}")
        
    print("-" * 55)


if __name__ == "__main__":
    generar_reporte_inventario()