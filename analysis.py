import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/eduardacarolline27/Amazon_Sales_Analise/refs/heads/main/Amazon.csv"
df = pd.read_csv(url)
df.head()

df.info()

sales_by_state_category = df.groupby(['State', 'Category'])['TotalAmount'].sum()
print("Total sales by State and Category:\n", sales_by_state_category.head())

sales_df = sales_by_state_category.unstack(level='Category')
best_selling_category_per_state = sales_df.idxmax(axis=1)
print("Best-selling category per state:\n", best_selling_category_per_state.head())

best_selling_category_counts = best_selling_category_per_state.value_counts()

plt.figure(figsize=(10, 6))
best_selling_category_counts.plot(kind='bar', color='lightcoral')
plt.title('Contagem de Categorias Mais Vendidas por Estado')
plt.xlabel('Categoria de Produto')
plt.ylabel('Número de Estados')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Selecionar um único estado, por exemplo, 'CA' (Califórnia)
state_to_analyze = 'CA'
best_category_for_state = best_selling_category_per_state[state_to_analyze]
print("A categoria mais vendida em {state_to_analyze} é: {best_category_for_state}")

# Obter os dados de vendas para o estado selecionado em todas as categorias
sales_for_selected_state = sales_by_state_category.loc[state_to_analyze]

plt.figure(figsize=(10, 6))
sales_for_selected_state.plot(kind='bar')
plt.title('Total de Vendas por Categoria no Estado de {state_to_analyze}')
plt.xlabel('Categoria de Produto')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
