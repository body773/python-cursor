from flask import Flask

app = Flask(__name__)

developers = []


class Developer:
    def __init__(self, first_name, last_name, programming_language):
        self.first_name = first_name
        self.last_name = last_name
        self.programming_language = programming_language

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.programming_language}'

ivan = Developer('Ivan','Pidkova','VBA')
petro = Developer('Petro', 'Koloda', 'C++')
viktor = Developer('Viktor', 'Maly', 'Ruby')
gosha = Developer('Gosha', 'Kuzenko', 'Python')

developers.append(ivan)
developers.append(petro)
developers.append(viktor)
developers.append(gosha)
    
def get_list_dev():
    return '<br>'.join([str(d) for d in developers])

@app.route('/')
def developer_controller():
    developer_next = Developer('Bohdan', 'Novakivskyy', 'Python')
    return str(developer_next)


@app.route('/remove_developer')
def remove_developer():
    if not developers:
        return 'No developers in list'
    else:
        developers.pop()
        return get_list_dev()


