import pandas as pd
from fastapi import FastAPI 

app = FastAPI()

f = "netflix.csv"
df= pd.read_csv(f)

df["date_added"] = pd.to_datetime(df["date_added"])


df.sort_values(by=['date_added'])

df["director"] = df["director"].replace("Not Given", "None")

df1 = df[df["release_year"] == 2019]
df2 = df[df["release_year"] == 2020]
df3 =df[df["release_year"] == 2021]


a= df1.reset_index().to_dict(orient="index")
b=df2.reset_index().to_dict(orient="index")
c=df3.reset_index().to_dict(orient="index")

@app.get("/")
async def index():
    return "ia stoy arta"

@app.get("/2019")
async def index():
    return a

@app.get("/2020")
async def index():
    return b
    

@app.get("/2021")
async def index():
    return c

