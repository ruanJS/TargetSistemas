import json

# Suponha que o JSON esteja em um arquivo chamado "faturamento.json"
with open('faturamento.json') as f:
    dados = json.load(f)

faturamentos = dados['faturamento_diario']
dias_com_faturamento = [valor for valor in faturamentos if valor > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento) if dias_com_faturamento else 0

menor_faturamento = min(dias_com_faturamento, default=0)
maior_faturamento = max(dias_com_faturamento, default=0)
dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
