# Sistema de Teste Automático BOCA - Versão 2.0

🚀 **Sistema melhorado para testes automáticos de exercícios de programação**

## ✨ Principais Melhorias

- **Código completamente reescrito** com melhor estrutura e legibilidade
- **Interface visual aprimorada** com emojis e mensagens claras
- **Tratamento robusto de erros** com mensagens informativas
- **Documentação completa** com docstrings e comentários
- **Arquitetura orientada a objetos** para melhor manutenibilidade
- **Comparação detalhada de saídas** mostrando diferenças linha por linha
- **Suporte a pathlib** para melhor compatibilidade entre sistemas
- **Limpeza automática de cache** do Python

## 📁 Estrutura do Projeto

```
boca-trifasico/
├── main.py              # Script principal (MELHORADO)
├── programa/             # Coloque seus arquivos .py aqui
│   └── exemplo.py        # Arquivo de exemplo
├── exercise/             # Diretórios dos exercícios
│   ├── A_antenna/
│   │   ├── in/          # Arquivos de entrada
│   │   └── out/         # Arquivos de saída esperada
│   └── ...
└── README.MD            # Este arquivo
```

## 🎯 Como Usar

### 1. Preparar seu código
- Coloque seu arquivo Python na pasta `programa/`
- O nome do arquivo deve corresponder ao exercício (ex: `antenna.py` para exercício `A_antenna`)

### 2. Executar os testes
```bash
python main.py
```

### 3. Interpretar os resultados
- ✅ **PASSOU**: Teste executado com sucesso
- ❌ **FALHOU**: Saída diferente do esperado (mostra diferenças)
- 🎉 **CORRECT ANSWER**: Todos os testes passaram
- ❌ **WRONG ANSWER**: Alguns testes falharam

## 📊 Exemplo de Saída

```
🚀 Iniciando sistema de testes...

📁 Arquivo encontrado: antenna.py
📂 Exercício encontrado: A_antenna
🧪 Executando 5 testes...

Teste 1/5: 01... ✅ PASSOU
Teste 2/5: 02... ✅ PASSOU
Teste 3/5: 03... ❌ FALHOU

❌ ERRO no teste 03:
Saída obtida:
  1: '42'
Saída esperada:
  1: '24'
  Diferença na linha 1: '42' ≠ '24'

Teste 4/5: 04... ✅ PASSOU
Teste 5/5: 05... ✅ PASSOU

==================================================
📊 Resultado: 4/5 testes passaram
❌ WRONG ANSWER
```

## 🔧 Funcionalidades Técnicas

- **Detecção automática** de arquivos Python e exercícios
- **Ordenação inteligente** de arquivos de teste por número
- **Captura segura** de entrada/saída com restauração de streams
- **Limpeza de cache** automática entre execuções
- **Tratamento de exceções** robusto
- **Suporte a interrupção** via Ctrl+C

## 🐛 Solução de Problemas

### Erro: "Diretório 'programa' não encontrado"
- Crie a pasta `programa/` e coloque seu arquivo .py dentro

### Erro: "Nenhum arquivo .py encontrado"
- Verifique se há um arquivo Python na pasta `programa/`

### Erro: "Diretório do exercício não encontrado"
- Verifique se o nome do arquivo corresponde ao exercício
- Ex: `antenna.py` deve corresponder a `A_antenna/` ou `antenna/`

## 📝 Notas da Versão 2.0

- Código original de 199 linhas reduzido e reorganizado em 242 linhas mais legíveis
- Eliminadas variáveis desnecessárias e código comentado
- Implementada arquitetura de classes para melhor organização
- Adicionado sistema de logging visual com emojis
- Melhorado tratamento de erros e mensagens de debug
