from pathlib import Path
import json, csv

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

# ==========================================
# CONTROLLER DE LEADS (CRIAR, LER E BUSCAR)
# ==========================================

# LER TODOS OS LEADS
def read_leads():
    # se o arquivo nao existir ainda, retorna uma lista vazia
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

# SALVAR / CRIAR NOVO LEAD
def create_lead(lead_dict):
    leads = read_leads()
    leads.append(lead_dict)
    # salva a lista no leads.json bonitinho e formatado
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

# BUSCAR LEADS (POR NOME OU EMAIL)
def read_leads_search(query):
    """
    Recebe o texto de busca e retorna os leads encontrados
    """
    leads = read_leads()
    results = []

    for i, lead in enumerate(leads):
        # junta o nome e o email pra facilitar a busca
        txt_lead = f"{lead['name']} {lead['email']}".lower()

        if query.lower() in txt_lead:
            results.append((i, lead))

    return results

# EXPORTAR PARA CSV
def export_csv():
    """
    Salva todos os leads em um arquivo .csv e retorna o caminho dele
    """
    leads = read_leads()

    # se nao tiver nenhum lead salvo, nao tem o que exportar
    if not leads:
        return None

    path_csv = DATA_DIR / "leads.csv"

    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, leads[0].keys())
            writer.writeheader()
            for row_dict in leads:
                writer.writerow(row_dict)
        return path_csv
    except PermissionError:
        return None
