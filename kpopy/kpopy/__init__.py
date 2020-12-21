import json
import os
import sys

all_artist = json.loads(open(os.path.join(sys.path[0], 'kpop_data.json'), encoding="utf-8").read())

# removes unnecessary things
for artist in all_artist:
    if '_id'in artist:
        del artist['_id']
    if 'T00:00:00.000Z' in artist['Date of Birth']:
        artist['Date of Birth'] = artist['Date of Birth'].replace('T00:00:00.000Z', '')

def get_all_artists():
    return all_artist


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
        numBlanks = 0
        for i in range(len(attributes)):
            if attributes[i] == '':
                numBlanks += 1
            elif attributes[i] != '' and attributes[i].lower() != artist_attributes[i].lower():
                isIn = False
                break
        if isIn and numBlanks != 17:
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
        numBlanks = 0
        for i in range(len(attributes)):
            if attributes[i] == '':
                numBlanks += 1
            elif attributes[i] != '' and attributes[i].lower() not in artist_attributes[i].lower():
                isIn = False
                break
        if isIn and numBlanks != 17:
            artists.append(artist)
    return artists