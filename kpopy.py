import requests
import ast

url = "https://kpopapi-c5aa.restdb.io/rest/kpop"

headers = {
    'content-type': "application/json",
    'x-apikey': "abd017d0d9b34b7da68471cb7c47a4c9a2021",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)
all_artist = ast.literal_eval(response.text)

# removes unnecessary things
for artist in all_artist:
    if '_id'in artist:
        del artist['_id']
    if 'T00:00:00.000Z' in artist['Date of Birth']:
        artist['Date of Birth'] = artist['Date of Birth'].replace('T00:00:00.000Z', '')


def get_specific_artist(stage_name='', full_name='', korean_name='', korean_stage_name='', dob='', 
                        group='', country='', second_country='', height='', weight='', birthplace='', 
                        other_group='', former_group='', gender='', position='', instagram='', twitter=''):
    attributes = [stage_name, full_name, korean_name, korean_stage_name, dob, group, country,
                    second_country, height, weight, birthplace, other_group, former_group, gender,
                    position, instagram, twitter]
    artists = []
    for artist in all_artist:
        artist_attributes = [artist['Stage Name'], artist['Full Name'], artist['Korean Name'],
                            artist['Korean Stage Name'], artist['Date of Birth'], artist['Group'],
                            artist['Country'], artist['Second Country'], artist['Height'],
                            artist['Weight'], artist['Birthplace'], artist['Other Group'], 
                            artist['Former Group'], artist['Gender'], artist['Position'], 
                            artist['Instagram'], artist['Twitter']]
        isIn = True

        for i in range(len(attributes)):
            if attributes[i] != '' and attributes[i].lower() != artist_attributes[i].lower():
                isIn = False
                break
        if isIn:
            artists.append(artist)
    return artists
        
def get_similar_artist(stage_name='', full_name='', korean_name='', korean_stage_name='', dob='', 
                        group='', country='', second_country='', height='', weight='', birthplace='', 
                        other_group='', former_group='', gender='', position='', instagram='', twitter=''):
    attributes = [stage_name, full_name, korean_name, korean_stage_name, dob, group, country,
                    second_country, height, weight, birthplace, other_group, former_group, gender,
                    position, instagram, twitter]
    artists = []
    for artist in all_artist:
        artist_attributes = [artist['Stage Name'], artist['Full Name'], artist['Korean Name'],
                            artist['Korean Stage Name'], artist['Date of Birth'], artist['Group'],
                            artist['Country'], artist['Second Country'], artist['Height'],
                            artist['Weight'], artist['Birthplace'], artist['Other Group'], 
                            artist['Former Group'], artist['Gender'], artist['Position'], 
                            artist['Instagram'], artist['Twitter']]
        isIn = True

        for i in range(len(attributes)):
            if attributes[i] != '' and attributes[i].lower() not in artist_attributes[i].lower():
                isIn = False
                break
        if isIn:
            artists.append(artist)
    return artists
