from fastapi import FastAPI,HTTPException
from typing import List,Dict
from schemas import GenreURLChoices,Band


app = FastAPI()

BANDS = [
    {'id': 1, 'name': 'The Kinks', 'genre': 'Rock'},
    {'id': "2", 'name': 'Aphex Twin', 'genre': 'Electronic'},
    {'id': 3, 'name': 'Slowdive', 'genre': 'metal', 'albums':[
        {'title': "Masters", 'release_date':'1972-12-12'}]},
    {'id': 4, 'name': 'Wu-Tang Clan', 'genre': 'Hip-Hop'},  
]

@app.get('/bands')
async def bands(  #set defalut value to None otherwise passing parameter is necessary
    genre:GenreURLChoices | None = None,
    has_albums:bool = False
    )->List[Band]:
    
    bandList = [Band(**b) for b in BANDS]
    
    if genre:
        bandList =  [
            b for b in bandList if b.genre.lower()==genre.value.lower()
        ]
    if has_albums:
        bandList = [
            b for b in bandList if len(b.albums)>0
        ]
    return bandList
@app.get('/bands/{band_id}')
async def band(band_id:int)->Band:
    band = next((Band(**b) for b in BANDS if str(b['id'])==str(band_id)),None)
    if band is None:
        raise HTTPException(status_code=404,detail="Could not find data for band")
    return band

@app.get('/bands/genres/{genre}')
async def bands_genre(genre:str):
    band = [x for x in BANDS if x['genre']==genre]
    if band is None:
        return HTTPException(status_code=404,detail="Could not find Genre of the band")
    return band