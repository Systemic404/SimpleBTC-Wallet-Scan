import requests
from tqdm import tqdm


# Function to check balance
# Função para verificar saldo
def check_balance(address):

    url = f'https://blockchain.info/rawaddr/{address}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        balance = data['final_balance'] / 100000000  # Converting from satoshis to BTC
        return balance
    else:
        return None


# Function to generate addresses
# Função para gerar endereços
def generate_addresses(start, end):

    addresses = []
    # f'1MaiDwS5HvNTnGq6snz4VQz5v1zX3brfi is prefix change for more best result :D
    # f'1MaiDwS5HvNTnGq6snz4VQz5v1zX3brfi é o prefixo altere para talvez obter melhores resultados :D
    for i in range(start, end + 1):
        address = f'1MaiDwS5HvNTnGq6snz4VQz5v1zX3brfi{str(i).zfill(8)}'
        addresses.append(address)

    return addresses


# Function to create a ranking
# Função para criar ranking
def create_ranking(addresses):

    ranking = []

    for address in tqdm(addresses, desc="Checking balances"):
        balance = check_balance(address)
        ranking.append({'address': address, 'balance': balance if balance is not None else 0})

    ranking = sorted(ranking, key=lambda x: x['balance'], reverse=True)
    return ranking



ascii_art = """
    ____ ____________                     
   / __ )_  __/ ____/                     
  / __  |/ / / /                          
 / /_/ // / / /___                        
/_____//_/__\____/__    __    ____________
| |     / /   |  / /   / /   / ____/_  __/
| | /| / / /| | / /   / /   / __/   / /   
| |/ |/ / ___ |/ /___/ /___/ /___  / /    
|__/|__/_/__|_/_____/_____/_____/ /_/     
  / ___// ____/   |  / | / /              
  \__ \/ /   / /| | /  |/ /               
 ___/ / /___/ ___ |/ /|  /                
/____/\____/_/  |_/_/ |_/                 

BY: SYSTEMIC404
https://github.com/Systemic404/
"""

# Replace 'START' and 'END' with the desired values for the address range
# Substitua 'START' e 'END'  pelos valores desejados para o intervalo de endereços
START = 1
END = 10  # Increase the number of addresses as needed / Aumente o número de endereços conforme necessário
address_list = generate_addresses(START, END)

# Create a ranking of addresses based on balances
# Criar ranking de endereços com base nos saldos
ranking = create_ranking(address_list)


print(ascii_art)

# Display ranking results
# Exibir resultados do ranking
for position, result in enumerate(ranking, start=1):
    print(f"Position {position}: Address: {result['address']}, Balance: {result['balance']} BTC")
