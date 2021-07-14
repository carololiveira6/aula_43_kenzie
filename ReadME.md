## **Table of Contents**
- [Retake - Parte 5](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/codewars_retake5.html&ref=master#mcetoc_1f4uinjti1)
- [Introdução](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/codewars_retake5.html&ref=master#mcetoc_1f8b3af9p0)
- [Explicando rotas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/codewars_retake5.html&ref=master#mcetoc_1f8b3af9p1)
- [Rota GET - "/games"](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/codewars_retake5.html&ref=master#mcetoc_1f8b3af9p3)
- [Classe - CsvServices](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/codewars_retake5.html&ref=master#mcetoc_1f8b3af9p4) 

    - [Método de instância - validate_fields](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/codewars_retake5.html&ref=master#mcetoc_1f8b3af9p5)
    - [Método de instância - validate_column_filter](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/codewars_retake5.html&ref=master#mcetoc_1f8b3af9p6)
    - [Método de instância - found_by_filter](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/codewars_retake5.html&ref=master#mcetoc_1f8b3af9p7)
    - [Método estático - top_teen](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/codewars_retake5.html&ref=master#mcetoc_1f8b3af9p8)
- [Entregáveis ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/codewars_retake5.html&ref=master#mcetoc_1egvoav555j)


# **Retake - Parte 5**
**Atenção**: O acesso para o Retake, **só vai ser permitido** para os devs que realizarem a **Parte 1,** **Parte 2, Parte 3, Parte 4 e Parte 5** do conteúdo de estudos para o Retake.
# **Introdução**
Antes de começar, faça o fork e em seguida clone [**este repositório**](https://gitlab.com/kenzie-academy-brasil/se/back-end-web-development/q3/nivelamento/entrega-retake-parte-5-outubro-20).

Não esqueça de criar o venv e de rodar o comando **pip install -r requirements.txt** no seu terminal, para instalar todas as dependências.
# **Explicando rotas**

# **Rota GET - "/games"**
Conforme explicado no vídeo, a rota **GET "/games"** funciona das seguinte maneiras:

- **Com dois argumentos** (filtros), por exemplo "**http://127.0.0.1:5000/games?name=ps2&column=platform**"

**Observação**: Ao aplicar os filtros na URL, a pesquisa no arquivo CSV **NÃO DEVE** ser **case sensitive**.

Caso a rota **tenha um, ou nenhum argumento, deverá retornar os 10 primeiros registros** do arquivo **games.csv**.

Exemplos de rotas que retornam os 10 primeiros registros do arquivo csv:

1. ` `"**http://127.0.0.1:5000/games**"
1. ` `"**http://127.0.0.1:5000/games?name=kart**"

**Fique atento:** Nos arquivos do repositório existem comentários que podem te auxiliar no desenvolvimento da entrega.
# **Classe - CsvServices**
### **Método de instância - validate\_fields**
Esse método deve **verificar se existe os 2 argumentos na URL**:

- Caso exista um, ou nenhum argumento na URL, o método deve estourar **AttributeError** ou o **Custom Error MissingArg**.
### **Método de instância - validate\_column\_filter**
Esse método deve **verificar se o argumento column é valido**.

- O filtro **Column** aceita somente os valores de **VALID\_FILTERS**, caso o usuário passe um valor diferente, o método deve estourar **ValueError** ou o **Custom Error InvalidColumnFilter**.
### **Método de instância - found\_by\_filter**
Você irá chamar esse metódo na rota para aplicar os filtros, ele **deve retornar uma LISTA DE DICIONÁRIOS com os valores filtrados**.

- Certifique-se de que haja os 2 argumentos na rota e o **filtro por coluna seja válido**.
- Caso não encontre nenhum valor após aplicar o filtro deve estourar **ValueError** ou o **Custom Error NotFound**.
### **Método estático - top\_teen**
Esse método deve **retornar os 10 primeiros games (registros) do CSV**.



**Observação:** Dentro do repositório existe o arquivo **insomnia-retake5**, importe-o no insomnia para realizar os testes de rota.

-----
# **Entregáveis** 
- Envie o link do seu repositório, não esqueça de adicionar o grupo de correções.


