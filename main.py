from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
import random

app = FastAPI()

def mokdata():
    albums = ["DABDA", "천사", "PAGAN", "전설", "유령", "사이코시스 뮤", "한", "환상", "127", "꽃뱀", "NETFLIX&CHILL", "2:27", "멸망"]
    ratings = ["⭐️⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️", "⭐️⭐️", "⭐️"]

    data = []
    for album in albums:
        rating = random.choice(ratings)

        match rating:
            case "⭐️⭐️⭐️⭐️⭐️":
                icon = "🌟"
            case "⭐️⭐️⭐️⭐️":
                icon = "✨"
            case "⭐️⭐️⭐️":
                icon = "😊"
            case "⭐️⭐️":
                icon = "😐"
            case "⭐️":
                icon = "😢"
            case _:
                icon = "❓"

        data.append({
            "앨범명": album,
            "평가": rating,
            "아이콘": icon
        })

    return pd.DataFrame(data)

@app.get("/", response_class=HTMLResponse)
async def show_album_data():
    df = mokdata()
    table_html = df.to_html(index=False, escape=False, justify="center", border=1)
    html_content = f"""
    <html>
        <head>
            <title>앨범 평가</title>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; }}
                table {{ margin: 0 auto; border-collapse: collapse; width: 80%; }}
                th, td {{ padding: 10px; border: 1px solid #ddd; text-align: center; }}
                th {{ background-color: #f4f4f4; }}
            </style>
        </head>
        <body>
            <h1>앨범 평가 데이터</h1>
            {table_html}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)