import requests
import pandas as pd

# NewsAPI endpoint and API key
api_key = 'APIKEY'

def get_stock_news(stock_symbol):
    # Define the NewsAPI URL with query parameters for the stock symbol
    url = f"https://newsapi.org/v2/everything?q={stock_symbol}&apiKey={api_key}&language=en&sortBy=publishedAt"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        news_data = response.json()

        # Extract articles
        articles = []
        for article in news_data['articles']:
            articles.append({
                'title': article['title'],
                'description': article['description'],
                'url': article['url'],
                'source': article['source']['name'],
                'published_at': article['publishedAt']
            })

        # Return a DataFrame for easy data handling
        return pd.DataFrame(articles)
    else:
        print(f"Error: Unable to fetch news. Status Code: {response.status_code}")
        return None


# Example usage
stock_symbol = "AAPL"  # You can change this to any stock symbol (e.g., TSLA for Tesla)
df = get_stock_news(stock_symbol)

if df is not None:
    # Display the results
    print(df)

    # Optionally, save the results to a CSV file
    df.to_csv(f'{stock_symbol}_news.csv', index=False)
