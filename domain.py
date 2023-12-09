"""
• Criar uma tela de cadastro de informações do álbum. As seguintes
informações são necessárias: nome do álbum, ano de lançamento,
nome da banda/artista, álbum lançamento do artista (sim/não);
• Criar uma tela que liste todos os álbuns cadastrados na sua base de
dados.

"""
import datetime
import db

CURRENT_YEAR = datetime.date.today().year

def save_album(author, album, year, release):
    algum = {'author': author, 'album': album, 'year': year, 'release': release}
    db.save_on_db(db.FILE_NAME, algum)
    return True


def get_album_by(key: str, value: str, albuns: list):
    for album in albuns:
        if value.lower() in album[key].lower():
            return album


def get_all_albuns_by(key: str, value: str, albuns: list):
    filtered_albuns = []
    for album in albuns:
        if value.lower() in album[key].lower():
            filtered_albuns.append(album)
    return filtered_albuns if value else albuns


def get_album_previous_year(date, albuns):
    selected_albuns = filter(lambda item: item['year'] < date, albuns)
    return list(selected_albuns)


def get_album_same_year(date, albuns):
    selected_albuns = filter(lambda item: item['year'] == date, albuns)
    return list(selected_albuns)


def get_album_later_year(date, albuns):
    selected_albuns = filter(lambda item: item['year'] > date, albuns)
    return list(selected_albuns)


def get_albuns():
    return db.get_from_db(db.FILE_NAME)
