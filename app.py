from model import model_lead
import control as control

def add_lead():
    print("\n--- Adicionar Novo Lead ---")
    name = input("Nome: ").strip()
    email = input("E-mail: ").strip()
    stage = input("Etapa no funil (ex: Novo, Contato, Proposta, Fechado): ").strip()

    # 1. Validando campos obrigatorios
    if not name or not email:
        print("Erro: Nome e e-mail são obrigatórios!")
        return

    # 2. Validacao simples de email
    if "@" not in email or "." not in email:
        print("Erro: Digite um e-mail válido!")
        return

    # 3. Se a etapa ficar vazia, coloca um valor padrao
    if not stage:
        stage = "Novo"

    # 4. Checa se o email ja existe na lista
    leads = control.read_leads()
    for lead in leads:
        if lead["email"].lower() == email.lower():
            print("Erro: Já existe um lead cadastrado com esse e-mail!")
            return

    # 5. Modela os dados em formato de dicionario
    novo_lead = model_lead(name, email, stage)

    # 6. Salva no arquivo atraves do controller
    control.create_lead(novo_lead)
    print(f"Sucesso: Lead '{name}' adicionado com sucesso!")

def list_leads():
    leads = control.read_leads()

    if not leads:
        print("\nNenhum lead cadastrado ainda.")
        return

    print("\n" + "=" * 60)
    print(f"## | {'Nome':<15} | {'E-mail':<22} | Etapa")
    print("-" * 60)
    for i, lead in enumerate(leads):
        stage = lead.get("stage", "Sem etapa")
        print(f"{i:02d} | {lead['name']:<15} | {lead['email']:<22} | {stage}")
    print("=" * 60)

def search_leads():
    query = input("\nBuscar por (nome ou e-mail): ").strip()
    if not query:
        print("A busca não pode ser vazia.")
        return

    search_results = control.read_leads_search(query)

    if not search_results:
        print(f"Nenhum lead encontrado para '{query}'.")
        return

    print("\n" + "=" * 60)
    print(f"## | {'Nome':<15} | {'E-mail':<22} | Etapa")
    print("-" * 60)
    for i, lead in search_results:
        stage = lead.get("stage", "Sem etapa")
        print(f"{i:02d} | {lead['name']:<15} | {lead['email']:<22} | {stage}")
    print("=" * 60)

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("\nNão há leads para exportar ou ocorreu um erro.")
    else:
        print(f"\nSucesso: Leads exportados para o arquivo: {path_csv}")

def main():
    while True:
        print("\n=== Mini CRM de Leads ===")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/e-mail)")
        print("[4] Exportar para CSV")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ").strip()

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("\nSaindo... Até mais!")
            break
        else:
            print("\nO usuário é burro.")

if __name__ == "__main__":
    main()
