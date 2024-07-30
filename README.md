# Gerenciamento de Projetos e Desenvolvedores

## Descrição

Este sistema de gerenciamento permite cadastrar, atualizar, listar e excluir projetos de software e desenvolvedores associados a esses projetos. Cada desenvolvedor é associado a um único projeto e o sistema gerencia a relação entre projetos e desenvolvedores.

## Funcionalidades

1. **Cadastrar Projeto de Software**:
   - Adiciona um novo projeto ao sistema com um ID e nome.
   
2. **Cadastrar Desenvolvedor**:
   - Adiciona um novo desenvolvedor ao sistema com um ID, nome e o projeto ao qual está associado.
   
3. **Listar Projetos**:
   - Exibe todos os projetos cadastrados com seus desenvolvedores associados.

4. **Listar Desenvolvedores**:
   - Exibe todos os desenvolvedores cadastrados e o projeto ao qual estão associados.
   
5. **Atualizar Projeto**:
   - Permite atualizar o nome de um projeto existente.

6. **Atualizar Desenvolvedor**:
   - Permite atualizar o nome de um desenvolvedor e reflete a mudança em todos os projetos associados.

7. **Excluir Projeto de Software**:
   - Remove um projeto do sistema e desassocia todos os desenvolvedores associados a ele.

8. **Excluir Desenvolvedor**:
   - Remove um desenvolvedor do sistema e atualiza todos os projetos para refletir a remoção.

## Estrutura do Código

- **`projects`**: Lista que armazena todos os projetos. Cada projeto é um dicionário com o formato:
  ```python
  {"id": "ID do Projeto", "nome": "Nome do Projeto", "desenvolvedores": [lista de desenvolvedores]}
