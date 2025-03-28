from datetime import datetime

def formatar_data(data_str):
    
    # Tenta converter a data no formato 'DD/MM/AAAA'
    try:
        return datetime.strptime(data_str, '%d/%m/%Y')
    except ValueError:
        pass
    
    # Tenta converter a data no formato 'DDMMYYYY'
    try:
        return datetime.strptime(data_str, '%d%m%Y')
    except ValueError:
        raise ValueError("Formato de data inválido. Use 'DD/MM/AAAA' ou 'DDMMYYYY'.")

def validar_data(data_validade, data_compra):
    
    try:
        
        data_validade = formatar_data(data_validade)
        data_compra = formatar_data(data_compra)
        data_atual = datetime.now()
        
        
        limite_data = datetime(2027, 12, 31)
        if data_validade > limite_data:
            print("\nO produto está vencido porque ultrapassou a data limite de 31/12/2027.")
        
        # Verifica se o produto está vencido em relação à data atual
        if data_validade < data_atual:
            dias_vencido = (data_atual - data_validade).days
            print(f"Este produto passou da data de validade neste período: {dias_vencido} dias.")
            return "O produto está vencido."
        else:
            # Calcula quanto tempo ainda pode ser consumido
            tempo_uso = (data_validade - data_atual).days
            print(f"Este produto pode ser consumido por mais {tempo_uso} dias.")
            return "O produto está dentro do prazo de validade."
    except ValueError as e:
        return str(e)

# Programa principal
if __name__ == "__main__":
    print("Bem-vindo ao Validador de Datas de Produtos!")
    
    while True:
        print("Esta consulta é para um alimento ou um produto?")
        
        # Pergunta inicial sobre o tipo de item
        tipo_item = input("Digite 'alimento' ou 'produto': ").strip().lower()
        
        if not tipo_item:
            print("\nPor favor, informe se é um alimento ou um produto.")
            continue
        
        if tipo_item == "higiene pessoal":
            print("\nNão foi possível fazer a consulta.")
            print("Encerrando o programa...")
            break
        
        # Solicita ao usuário que insira uma data de validade
        print("\n--- Entrada ---")
        data_validade_input = input("Digite a data de validade do produto (DD/MM/AAAA ou DDMMYYYY) ou 'sair' para encerrar: ")
        
        if data_validade_input.lower() == 'sair':
            print("\nEncerrando o programa. Até mais!")
            break
        
        # Solicita ao usuário que insira a data da compra
        data_compra_input = input("Digite a data da compra do produto (DD/MM/AAAA ou DDMMYYYY): ")
        
        #  função para validar a data 
        resultado = validar_data(data_validade_input, data_compra_input)
        
        
        print("\n--- Informações Gerais ---")
        print(f"Tipo do Item: {tipo_item.capitalize()}")
        print(f"Data da Compra: {data_compra_input}")
        print(f"Data de Validade: {data_validade_input}")
        
        print("\n--- Resultado ---")
        print(resultado)

        
        if resultado == "O produto está dentro do prazo de validade.":
            tempo_uso = (datetime.strptime(data_validade_input, '%d/%m/%Y') - datetime.now()).days
            print(f"\nVocê pode consumir este produto por mais {tempo_uso} dias.")

    
    print("\nObrigado pela consulta, tenha um ótimo dia!")
