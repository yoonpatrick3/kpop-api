# kpop-api
Web scraping from online database 

# https://pypi.org/project/kpopy/
```
pip install kpopy
```

# Documentation
```
import kpop as kp
```
### Getting all artists
```
kp.get_all_artists()
```
### Looking for artists with specific arguments
```
kp.get_specific_artist(stage_name='', full_name='', korean_name='', korean_stage_name='', dob='', 
                        group='', country='', second_country='', height='', weight='', birthplace='', 
                        other_group='', former_group='', gender='', position='', instagram='', twitter='')
```
### Looking for artists with relative arguments
```
kp.get_specific_artist(stage_name='', full_name='', korean_name='', korean_stage_name='', dob='', 
                        group='', country='', second_country='', height='', weight='', birthplace='', 
                        other_group='', former_group='', gender='', position='', instagram='', twitter='')
Every one of these methods return a list of dictionaries, representing the Korean artists' information