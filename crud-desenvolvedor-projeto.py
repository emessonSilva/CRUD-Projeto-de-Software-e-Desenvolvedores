'''
Projeto de Software e Desenvolvedores
- Descrição: Um projeto de software envolve vários
desenvolvedores. Cada desenvolvedor contribui para um único
projeto de software.
- Relação: Um projeto de software -> Muitos desenvolvedores
'''

projects = []
developers = []

def registerProject():
    projectId = input("Digite o ID do projeto: ")
    name = input("Digite o nome do projeto: ")
    projects.append({"id": projectId, "nome": name, "desenvolvedores": []})
    print(f"Projeto '{name}' cadastrado com sucesso! ID do projeto: {projectId}")

def registerDeveloper():
    developerId = input("Digite o ID do desenvolvedor: ")
    name = input("Digite o nome do desenvolvedor: ")
    associatedProjectId = input("Digite o ID do projeto ao qual o desenvolvedor pertence: ")
    project_found = False
    for project in projects:
        if project["id"] == associatedProjectId:
            project["desenvolvedores"].append({"id": developerId, "nome": name})
            print(f"Desenvolvedor '{name}' cadastrado para o projeto '{project['nome']}' com sucesso!")
            project_found = True
            break   
    if not project_found:
        print(f"Projeto ID {associatedProjectId} não encontrado. Desenvolvedor não cadastrado.")
    developers.append({"id": developerId, "nome": name, "Projeto Associado": associatedProjectId})

def showProject():
    print("Projetos cadastrados:")
    for project in projects:
        print(f"ID: {project['id']}")
        print(f"Nome: {project['nome']}")
        print("Desenvolvedores:")
        if project['desenvolvedores']:
            for dev in project['desenvolvedores']:
                print(f"  - ID: {dev['id']}, Nome: {dev['nome']}")
        else:
            print("  Nenhum desenvolvedor associado.")
        print()

def showDeveloper():
    print("Desenvolvedores cadastrados:")
    for dev in developers:
        print(f"ID: {dev['id']}")
        print(f"Nome: {dev['nome']}")
        print(f"Projeto Associado (ID): {dev['Projeto Associado']}")
        print()

def updateProject():
    projectId = input("Digite o ID do projeto a ser atualizado: ")
    for project in projects:
        if project["id"] == projectId:
            newProjectName = input("Digite o novo nome do projeto: ")
            project["nome"] = newProjectName
            print(f"Projeto ID {projectId} atualizado para '{newProjectName}' com sucesso!")
            return
    else:
        print(f"Projeto ID {projectId} não encontrado.")

def updateDeveloper():
    developerId = input("Digite o ID do desenvolvedor a ser atualizado: ")
    for dev in developers:
        if dev["id"] == developerId:
            newDeveloperName = input("Digite o novo nome do desenvolvedor: ")
            dev["nome"] = newDeveloperName
            print(f"Desenvolvedor ID {developerId} atualizado para '{newDeveloperName}' com sucesso!")
            for project in projects:
                for d in project["desenvolvedores"]:
                    if d["id"] == developerId:
                        d["nome"] = newDeveloperName
                        print(f"Nome do desenvolvedor atualizado no projeto '{project['nome']}'.")
            return
    else:
        print(f"Desenvolvedor ID {developerId} não encontrado.")

def deleteProject():
    projectId = input("Digite o ID do projeto a ser excluído: ")
    for project in projects[:]: 
        if project["id"] == projectId:
            projects.remove(project)
            print(f"Projeto ID {projectId} excluído com sucesso!")
            return
    else:
        print(f"Projeto ID {projectId} não encontrado.")

def deleteDeveloper():
    developerId = input("Digite o ID do desenvolvedor a ser excluído: ") 
    for dev in developers:
        if dev["id"] == developerId:
            developers.remove(dev)
            print(f"Desenvolvedor ID {developerId} excluído com sucesso!")
            break
    else:
        print(f"Desenvolvedor ID {developerId} não encontrado.")
        return   
    for project in projects:
        project["desenvolvedores"] = [d for d in project["desenvolvedores"] if d["id"] != developerId]

def show_menu():
    print("=== Menu ===")
    print("1. Cadastrar projeto de software")
    print("2. Cadastrar desenvolvedor")
    print("3. Listar projetos")
    print("4. Listar desenvolvedores")
    print("5. Atualizar projeto")
    print("6. Atualizar desenvolvedor")
    print("7. Excluir um projeto de software")
    print("8. Excluir um desenvolvedor")
    print("9. Sair do sistema")
    return input("Escolha uma opção: ")

while True:
    opcao = show_menu()

    if opcao == "1":
        registerProject()
    elif opcao == "2":
        registerDeveloper()
    elif opcao == "3":
        showProject()
    elif opcao == "4":
        showDeveloper()
    elif opcao == "5":
        updateProject()
    elif opcao == "6":
        updateDeveloper()
    elif opcao == "7":
        deleteProject()
    elif opcao == "8":
        deleteDeveloper()
    elif opcao == "9":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

