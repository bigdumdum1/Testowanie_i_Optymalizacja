from flask import Flask, request, render_template, url_for

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

def create_html_table(comments):
    table_html = """
    <table>
        <thead>
            <tr>
                <th>Nazwa użytkownika</th>
                <th>Email</th>
                <th>Treść</th>
            </tr>
        </thead>
        <tbody>
    """
    for comment in comments:
        table_html += f"""
            <tr>
                <td>{comment['name']}</td>
                <td>{comment['email']}</td>
                <td>{comment['body']}</td>
            </tr>
        """
    table_html += """
        </tbody>
    </table>
    """
    return table_html

if __name__ == '__main__':
    comments_data = get_comments()
    if comments_data:
        html_table = create_html_table(comments_data)
        print(html_table)
    else:
        print('Brak danych komentarzy.')
