import urllib.request

# Remplace par ton lien "Raw" copié
URL_CSV = "https://raw.githubusercontent.com/gaetan-bv2005/P25-hackathon/main/sujet-9-clients.csv"

def lecture_cloud(url):
    with urllib.request.urlopen(url) as response:
        # On lit, on décode en texte, et on découpe par lignes
        content = response.read().decode('utf-8')
        return content.splitlines()

# Maintenant, n'importe qui avec internet peut lancer ça !
lignes = lecture_cloud(URL_CSV)
print(f"Chargement réussi : {len(lignes)} clients trouvés.")

print(lignes)

