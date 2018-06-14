from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired
import requests

class SearchForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Search')

def searchCharacterInfo(name):
    r = requests.get('https://swapi.co/api/people/')
    results = r.json()
    results = results['results']
    for result in results:
        if result['name'] in name:
            results = result
            homeworld = result['homeworld']
            hw = requests.get(homeworld)
            homeworld = hw.json()
            homeworld = homeworld['name']
            homeworld = {'homeworld' : homeworld }
            results.update(homeworld)
            films = result['films']
            film_titles = []
            for film in films:
                f = requests.get(film)
                film = f.json()
                film = film['title']
                film_titles.append(film)
            films = {'films' : film_titles}
            results.update(films)
            species = result['species']
            species_name = []
            for specie in species:
                s = requests.get(specie)
                specie = s.json()
                specie = specie['name']
                species_name.append(specie)
            species = {'species': species_name}
            results.update(species)
            vehicles = result['vehicles']
            vehicles_name = []
            for vehicle in vehicles:
                v = requests.get(vehicle)
                vehicle = v.json()
                vehicle = vehicle['name']
                vehicles_name.append(vehicle)
            vehicles = {'vehicles': vehicles_name}
            results.update(vehicles)
            starships = result['starships']
            starships_name = []
            for starship in starships:
                st = requests.get(starship)
                starship = st.json()
                starship = starship['name']
                starships_name.append(starship)
            starships = {'starships': starships_name}
            results.update(starships)
    return results

def getCharacterInfo(id):
    r = requests.get('https://swapi.co/api/people/{}'.format(id))
    results = r.json()
    homeworld = results['homeworld']
    hw = requests.get(homeworld)
    homeworld = hw.json()
    homeworld = homeworld['name']
    homeworld = {'homeworld': homeworld}
    results.update(homeworld)
    films = results['films']
    film_titles = []
    for film in films:
        f = requests.get(film)
        film = f.json()
        film = film['title']
        film_titles.append(film)
    films = {'films': film_titles}
    results.update(films)
    species = results['species']
    species_name = []
    for specie in species:
        s = requests.get(specie)
        specie = s.json()
        specie = specie['name']
        species_name.append(specie)
    species = {'species': species_name}
    results.update(species)
    vehicles = results['vehicles']
    vehicles_name = []
    for vehicle in vehicles:
        v = requests.get(vehicle)
        vehicle = v.json()
        vehicle = vehicle['name']
        vehicles_name.append(vehicle)
    vehicles = {'vehicles': vehicles_name}
    results.update(vehicles)
    starships = results['starships']
    starships_name = []
    for starship in starships:
        st = requests.get(starship)
        starship = st.json()
        starship = starship['name']
        starships_name.append(starship)
    starships = {'starships': starships_name}
    results.update(starships)
    return results
    
def getListCharacters():
    compiled_results = []
    r = requests.get('https://swapi.co/api/people/')
    results = r.json()
    results = results['results']
    for result in results:
        compiled_results.append(result)
    r = requests.get('https://swapi.co/api/people/?page=2')
    results = r.json()
    results = results['results']
    for result in results:
        compiled_results.append(result)
    r = requests.get('https://swapi.co/api/people/?page=3')
    results = r.json()
    results = results['results']
    for result in results:
        compiled_results.append(result)
    r = requests.get('https://swapi.co/api/people/?page=4')
    results = r.json()
    results = results['results']
    for result in results:
        compiled_results.append(result)
    r = requests.get('https://swapi.co/api/people/?page=5')
    results = r.json()
    results = results['results']
    for result in results:
        compiled_results.append(result)
    for result in compiled_results:
        homeworld = result['homeworld']
        hw = requests.get(homeworld)
        homeworld = hw.json()
        homeworld = homeworld['name']
        homeworld = {'homeworld': homeworld}
        result.update(homeworld)
    return compiled_results

def sortCharacters(by):
    compiled_results = getListCharacters()
    if by == 'name':
        compiled_results = sorted(compiled_results, key=lambda k: k.get(by, 0))
    else:
        for result in compiled_results:
            if result[by] == 'unknown':
                result[by] = 0
            if result[by] == '1,358':
                result[by] = 1358
            if result[by] == '78.2':
                result[by] = 78
            ints = int(result[by])
            new = {by: ints}
            result.update(new)
        compiled_results = sorted(compiled_results, key=lambda k: k.get(by, 0))
    return compiled_results

def planetResidents():
    compiled_results = {}
    r = requests.get('https://swapi.co/api/planets/')
    results = r.json()
    results = results['results']
    for result in results:
        planet = result['name']
        residents = result['residents']
        resident_names = []
        for resident in residents:
            res = requests.get(resident)
            resident = res.json()
            resident = resident['name']
            resident_names.append(resident)
        pair = {planet: resident_names}
        compiled_results.update(pair)
    r = requests.get('https://swapi.co/api/planets/?page=2')
    results = r.json()
    results = results['results']
    for result in results:
        planet = result['name']
        residents = result['residents']
        resident_names = []
        for resident in residents:
            res = requests.get(resident)
            resident = res.json()
            resident = resident['name']
            resident_names.append(resident)
        pair = {planet: resident_names}
        compiled_results.update(pair)
    r = requests.get('https://swapi.co/api/planets/?page=3')
    results = r.json()
    results = results['results']
    for result in results:
        planet = result['name']
        residents = result['residents']
        resident_names = []
        for resident in residents:
            res = requests.get(resident)
            resident = res.json()
            resident = resident['name']
            resident_names.append(resident)
        pair = {planet: resident_names}
        compiled_results.update(pair)
    r = requests.get('https://swapi.co/api/planets/?page=4')
    results = r.json()
    results = results['results']
    for result in results:
        planet = result['name']
        residents = result['residents']
        resident_names = []
        for resident in residents:
            res = requests.get(resident)
            resident = res.json()
            resident = resident['name']
            resident_names.append(resident)
        pair = {planet: resident_names}
        compiled_results.update(pair)
    r = requests.get('https://swapi.co/api/planets/?page=5')
    results = r.json()
    results = results['results']
    for result in results:
        planet = result['name']
        residents = result['residents']
        resident_names = []
        for resident in residents:
            res = requests.get(resident)
            resident = res.json()
            resident = resident['name']
            resident_names.append(resident)
        pair = {planet: resident_names}
        compiled_results.update(pair)
    r = requests.get('https://swapi.co/api/planets/?page=6')
    results = r.json()
    results = results['results']
    for result in results:
        planet = result['name']
        residents = result['residents']
        resident_names = []
        for resident in residents:
            res = requests.get(resident)
            resident = res.json()
            resident = resident['name']
            resident_names.append(resident)
        pair = {planet: resident_names}
        compiled_results.update(pair)
    r = requests.get('https://swapi.co/api/planets/?page=7')
    results = r.json()
    results = results['results']
    for result in results:
        planet = result['name']
        residents = result['residents']
        resident_names = []
        for resident in residents:
            res = requests.get(resident)
            resident = res.json()
            resident = resident['name']
            resident_names.append(resident)
        pair = {planet: resident_names}
        compiled_results.update(pair)
    return compiled_results