from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt


class Webscrape:
    # get the URL
    url = "https://en.wikipedia.org/wiki/Wikipedia:Size_of_Wikipedia"
    response = requests.get(url)
    # get the html content of the webpage
    html_content = response.content
    # print(html_content)

    # get the scraped data from the html content
    soup = BeautifulSoup(html_content, 'html.parser')
    # display scraped data
    # print(soup.prettify())
    # find the correct table from the website (usually done with id, but I couldn't find one for this table)
    table = soup.find('table', style='text-align: center; line-height:1.5em;')
    # get the first 2 columns, starting from one row down to avoid having the titles in the data
    rows = table.find_all('tr')[1:]
    data = []
    for row in rows:
        cols = row.find_all(['td', 'th'])
        if len(cols) > 1:
            first_col = cols[0].text.strip()
            second_col = cols[1].text.strip()
            data.append([first_col, second_col])
            # add the data from the 1st 2 columns to an array

    # save the array as a csv file
    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)

    # read the csv file (unnecessary to do it this way, however I wanted to see how I could do it)
    df1 = pd.read_csv("data.csv")

    # Convert the "Article count" column to a numeric format
    df1["1"] = df1["1"].str.replace(",", "").astype(int)

    # Plot the data
    df1.plot(x="0", y="1", kind='line')
    plt.title("Article Count growth of Wikipedia")
    plt.xlabel("Year")
    plt.ylabel("Article count")
    plt.axis
    plt.show()
