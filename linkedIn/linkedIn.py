import os
import requests

def scrape_linkedIn(linkedIn_profile_url, mock:bool=False):

    if mock:
        res=requests.get("https://gist.githubusercontent.com/piyushcodes07/00ffbeddfded48f4bca19006cd5a52d3/raw/788bea03da4a0193c04bc6c191913cf62a4df274/gistfile1.txt",timeout=10)

        data=res.json()

        # data={
        #     k:v
        #     for k,v in data.items()
        #     if v not in ([],"",None," ")
        #     and k not in ["certifications"]
        # }
        cleaned_data={}
        for k,v in data.items():
            if k not in ["certifications"] and v not in [[],""," ",None]:
                cleaned_data[k]=v

        return cleaned_data

    else:
        print("mock is set to false.")

if __name__=="__main__":
    data=scrape_linkedIn(mock=True)
    print(data)
