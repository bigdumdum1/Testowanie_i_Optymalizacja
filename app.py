from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/komentarze')
def komentarze():
    return render_template('komentarze.html')

@app.route('/albumy')
def albumy():
    return render_template('albumy.html')

@app.route('/zdjecia')
def zdjecia():
    return render_template('zdjecia.html')

@app.route('/posty')
def posty():
    return render_template('posty.html')
def get_comments():
    url = 'https://jsonplaceholder.typicode.com/comments'
    response = request.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Błąd pobierania danych: {response.status_code}')
        return []

def create_photos(data):
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>{filename}</title>
    </head>
    <body>
        <h1>{filename}</h1>
        <table>
            <thead>
                <tr>
                    <th>Nazwa użytkownika</th>
                    <th>Zdjęcie</th>
                    <th>Opis</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
    </body>
    </html>
    """

    table_rows = ""
    for item in data:
        table_rows += f"""
        <tr>
            <td>{item['name']}</td>
            <td><img src="{item.get('url', '')}" alt="{item.get('title', '')}" width="100"></td>
            <td>{item.get('body', '')}</td>
        </tr>
        """
    template += """
        </tbody>
    </table>
    """
    return template

def create_posts(data):
    template = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>{filename}</title>
    </head>
    <body>
        <h1>{filename}</h1>
        <table>
            <thead>
                <tr>
                    <th>Nazwa użytkownika</th>
                    <th>Treść posta</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
    </body>
    </html>
    """

    table_rows = ""
    for item in data:
        table_rows += f"""
        <tr>
            <td>{item['name']}</td>
            <td>{item.get('body', '')}</td>
        </tr>
        """
    template += """
        </tbody>
    </table>
    """
    return template



def create_albums(data):
    template = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>{filename}</title>
    </head>
    <body>
        <h1>{filename}</h1>
        <table>
            <thead>
                <tr>
                    <th>Właściciel albumu</th>
                    <th>Cover albumu</th>
                    <th>Opis albumu</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
    </body>
    </html>
     """

    table_rows = ""
    for item in data:
        table_rows += f"""
        <tr>
        <td>{item['name']}</td>
        <td>{item.get('body', '')}</td>
        </tr>
        """
        template += """
        </tbody>
        </table>
        """
    return template


if __name__ == '__main__':
    data = get_comments()
    if data:
        html_table = create_albums(data)
        print(html_table)
    else:
        print('Brak danych postów.')

