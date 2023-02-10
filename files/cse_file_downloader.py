import pandas as pd
import time
import os
import requests
import json
from cad_tickers.exchanges.cse import get_recent_docs_from_url
from extract_doc import mk_dir, handle_logic
from io import BytesIO, StringIO
"""
1. Get the list of documents from the CSE website
2. For each document, get the document url
3. If the document url is not in the csv file, add it to the csv file
4. For each document url, download the document and add it to the docs folder
5. For each document url, make a discord request with the document url
6. For each document url, make a discord request with the document summary
"""


def fig_to_buffer(fig):
  """ returns a matplotlib figure as a buffer
  """
  buf = BytesIO()
  fig.savefig(buf, format='png')
  buf.seek(0)
  imgdata = buf.read()
  return imgdata

def make_discord_request(content, embeds = [], filename = None, file = None):
    url = os.getenv("DISCORD_WEBHOOK")
    if url == None:
        print('DISCORD_WEBHOOK Missing')
        pass
    data = {}
    data["content"] = content
    files = {'file': (filename, file, 'application/pdf')}
    if filename != None and file != None:
        resp = requests.post(
            url, data=data, files=files
        )
    elif len(embeds) != 0:
        data["embeds"] = embeds
        resp = requests.post(
            url, data=json.dumps(data), headers={"Content-Type": "application/json"}
        )
    print(resp)
    print(resp.content)

stockList = ["PKK", "IDK", "ADDC", "VPH", "VST", "ACT"]
def get_cse_tickers_data():
    url = "https://github.com/FriendlyUser/cad_tickers_list/blob/main/static/latest/cse.csv?raw=true"
    r = requests.get(url, allow_redirects=True)
    s = r.content
    return pd.read_csv(StringIO(s.decode('utf-8')))

stock_df = get_cse_tickers_data()
stock_rows = stock_df.loc[stock_df['Symbol'].isin(stockList)]
stock_rows.loc[:, 'stock'] = stock_rows['Symbol']
stock_rows.loc[:, 'url'] = stock_rows['urls']
stockUrls = stock_rows.to_dict('records')
csv_file = "docs.csv"
if os.path.isfile(csv_file):
    # read from csv
    df = pd.read_csv(csv_file)
else:
    # make new df
    df = pd.DataFrame(columns=["stock", "url", "docUrl"])

# read data from csv 
for stock in stockUrls:
    stockName = stock.get("stock")
    stockUrl = stock.get("url")
    urls = []
    try:
        urls = get_recent_docs_from_url(stockUrl)
    except Exception as e:
        pass
    
    for docUrl in urls:
        # skip malformed relative urls
        if docUrl[0] == '/':
            continue
        # add each element to list
        exists = docUrl in df["docUrl"].tolist()
        if exists == False:
            print(f"Adding {stockName}: {docUrl}")
            df.loc[len(df)] = [stockName, stockUrl, docUrl]
            # wrap in todo
            stock_doc_dir = f"docs/{stockName}"
            mk_dir(stock_doc_dir)
            stock_doc_file_path = docUrl.split("/")[-1]
            pdf_file_name = f"{stock_doc_dir}/{stock_doc_file_path}.pdf"
            companyName = stock.get("Company").\
                replace('Inc.', '').\
                replace('Pharma', '').\
                strip()
            dataDict = {
                "url": docUrl,
                "path": pdf_file_name,
                "company_name": companyName
            }
            result_obj = handle_logic(dataDict)
            file_contents = result_obj.get("contents")
            summary = "N/A"
            try:
                summary = result_obj.get("summary")[:1980]
            except TypeError as e:
                pass
            embeds = [
                {
                    "title": stockName,
                    "url": docUrl,
                    "description": summary
                }
            ]
            if file_contents != None:
                make_discord_request(f"*{stockName}*: \n {docUrl}", embeds, pdf_file_name, file_contents)
                time.sleep(2)
            else:
                make_discord_request(f"*{stockName}*: \n {docUrl}", embeds)
                time.sleep(1)
            pass

df = df.drop_duplicates()
df = df.sort_values(by=['stock'])
df.to_csv(csv_file, index=False)
