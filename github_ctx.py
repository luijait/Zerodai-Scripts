import requests
from urllib.parse import urlparse, parse_qs

def github_search(input1):
    respuesta = requests.get(f'https://api.github.com/search/repositories?q={input1}')
    data = respuesta.json()
    return '\n'.join([f'URL: {item["html_url"]}\nDescripción: {item["description"]}' for item in data["items"]])
def extract_repo_info(github_url):
    """
    Extrae la información del propietario (owner) y el nombre del repositorio (repo)
    de una URL de GitHub.
    """
    path = urlparse(github_url).path
    parts = path.strip("/").split("/")
    if len(parts) >= 2:
        return parts[0], parts[1]
    else:
        raise ValueError("URL de GitHub no válida.")

def get_repo_info(owner, repo):
    """
    Obtiene información del repositorio, contenidos y README utilizando la API de GitHub.
    """
    base_url = "https://api.github.com"
    
    # Información general del repositorio
    repo_info_url = f"{base_url}/repos/{owner}/{repo}"
    repo_info = requests.get(repo_info_url).json()
    
    # Contenidos del repositorio (raíz)
    contents_url = f"{base_url}/repos/{owner}/{repo}/contents/"
    contents = requests.get(contents_url).json()
    
    # README
    readme_url = f"{base_url}/repos/{owner}/{repo}/readme"
    readme_info = requests.get(readme_url).json()
    
    # Contenido del README en formato raw
    readme_content = ""
    if 'download_url' in readme_info:
        readme_content = requests.get(readme_info['download_url']).text
    
    return repo_info, contents, readme_info, readme_content

# URL de ejemplo

    