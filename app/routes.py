from app import app
from flask import render_template, request, redirect, url_for
import os
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from app.utils import extract_tag, selectors

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST', 'GET'])
def extract():
    if request.method == "POST":
        product_code = request.form.get('product_code')
        url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
        all_opinions =[]
        while(url):
            print(url)
            response = requests.get(url)
            page_dom = BeautifulSoup(response.text, "html.parser")
            opinions = page_dom.select("div.js_product-review")
            for opinion in opinions:
                single_opinion = {}
                for key, value in selectors.items():
                    single_opinion[key] = extract_tag(opinion, *value)
                all_opinions.append(single_opinion)
            try:
                url = "https://www.ceneo.pl" + extract_tag(page_dom, "a.pagination__next", "href")
            except TypeError:
                url = None
        with open(f"./app/data/opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
            json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
        return redirect(url_for('product', product_code=product_code))
    return render_template('extract.html')

@app.route('/product/<product_code>')
def product(product_code):
    opinions = pd.read_json(f"./app/data/opinions/{product_code}.json")
    return render_template('product.html', product_code=product_code, opinions=opinions.to_html(header=1, classes='table table-striped table-success', table_id='opinions'))

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/author')
def author():
    return render_template('author.html')