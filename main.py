from fastapi import FastAPI,HTTPException
from typing import List,Dict

app = FastAPI()

BANDS = [
    {'id': 1, 'name': 'The Kinks', 'genre': 'Rock'},
    {'id': 2, 'name': 'Aphex Twin', 'genre': 'Electronic'},
    {'id': 3, 'name': 'Slowdive', 'genre': 'Shoegaze'},
    {'id': 4, 'name': 'Wu-Tang Clan', 'genre': 'Hip-Hop'},
]

@app.get('/bands')
async def bands()->List[Dict]:
    return BANDS
@app.get('/bands/{band_id}')
async def band(band_id:int):
    band = next((b for b in BANDS if b['id']==band_id),None)
    if band is None:
        raise HTTPException(status_code=404,detail="Could not find data for band")
    return band

@app.get('/bands/genres/{genre}')
async def bands_genre(genre:str)->List[Dict]:
    band = [x for x in BANDS if x['genre']==genre]
    if band is None:
        return HTTPException(status_code=404,detail="Could not find Genre of the band")
    return band