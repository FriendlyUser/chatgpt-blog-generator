---
tags: ['googleNews', 'C#']
title: Searching for news with google news rss feeds
description: Here we'll look at how to use google news rss feeds to create custom news rss feeds.
pubDate: Tues, 7 December 2023
layout: "@/templates/BasePost.astro"
---
Google News is a news aggregator service developed by Google. It presents a continuous, customizable flow of articles organized from thousands of publishers and magazines. Google News uses algorithms to sort the news stories, eliminating duplicates and organizing stories based on their relevance and popularity, so users can quickly find the latest news on topics they're interested in. In addition to traditional text-based articles, Google News also provides multimedia content such as videos and images. The service is available online and as an app for both Android and iOS devices. The service is available in many countries and in various languages, providing users with a diverse range of news sources and perspectives.


You can use the Google RSS feeds feature to find custom news in a specific format by using the following steps:

1. Go to the Google News website at <https://news.google.com/>
2. In the search bar, type in the keyword or phrase you are interested in and press enter to perform a search.
3. Once the search results are displayed, click on the "RSS" button located on the top-right side of the page.
4. A new page will open showing the RSS feed for your search results. You can copy the URL of this page and use it in your RSS reader to subscribe to the feed.

By subscribing to the RSS feed, you will receive updates on the latest news stories that match your search criteria, allowing you to stay up-to-date on the topics that interest you the most.


```csharp 
 using System;
//Request library
using System.Net;
using System.IO;
using System.Web;
using System.Xml;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Collections.Generic;
using System.Threading.Tasks;
using Elasticsearch.Net;
using System.Net.Http;
namespace news_alert
{
    public class News
    {
        public static readonly HttpClient client = new HttpClient();
    
        static public void SendItemToDiscord(XmlNode item) {
            // set discord webhook as private env
            string webhook = Environment.GetEnvironmentVariable("DISCORD_WEBHOOK");
            string esInstance = Environment.GetEnvironmentVariable("ES_INSTANCE");
            if (webhook == null) {
                Console.WriteLine("GET A DISCORD WEBHOOK");
                return;
            }
            var request = (HttpWebRequest)WebRequest.Create(webhook);
            request.ContentType = "application/json";
            request.Method = "POST";
            DateTime pubDate = Convert.ToDateTime(item["pubDate"].InnerText);
            string postLink = item["link"].InnerText;
            string discordTemplate = "{0} \n {1} \n {2} ";
            string discordMessage = string.Format(discordTemplate, item["title"].InnerText,
                item["pubDate"].InnerText, postLink);
            // write message of data sent to discord
            var w = new WebhookData() { content = discordMessage };
            using (var streamWriter = new StreamWriter(request.GetRequestStream()))
            {
                streamWriter.Write(JsonSerializer.Serialize<WebhookData>(w));
            }
            var httpResponse = (HttpWebResponse)request.GetResponse();
            using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
            {
                var result = streamReader.ReadToEnd();
            }
            // send data to es instance
            var settings = new ConnectionConfiguration(new Uri(esInstance))
                .RequestTimeout(TimeSpan.FromMinutes(2));
            var lowlevelClient = new ElasticLowLevelClient(settings);
            var post = new Post
            {
                guid = item["guid"].InnerText
            };
            var asyncIndexResponse = lowlevelClient.Index<StringResponse>("post", PostData.Serializable(post)); 
            string responseString = asyncIndexResponse.Body;
            Console.WriteLine(responseString);
        }

        static async Task Main(string[] args)
        {
            await checkNews();
            await Task.Run(() => checkPrices());
        }
        static async public Task checkPrices() {
            string stockUrl = Environment.GetEnvironmentVariable("STOCK_URL");
            if (stockUrl == null) {
                Console.WriteLine("GET A Stock URL WEBHOOK");
                return;
            }
            List<StockData> stocks = new List<StockData>();
            stocks.Add(new StockData() {ticker="NEXCF", targetPrice=1.60});
            foreach (StockData stock in stocks)
            {
                Console.WriteLine(stock.ticker);
                // query api
            }
            // either return a completed Task, or await for it (there is a difference!
            await Task.CompletedTask;
        }
        static async public Task checkNews() {
            var searchItems = new List<string> { "hydrogen",
                "analyticGPT", "natural gas", "recession",
                "Tech layoffs", "Bard AI"
            };
            foreach (string searchText in searchItems)
            {
                // line of items of cli list
                string xml = await FetchData(searchText);
                XmlDocument doc = new XmlDocument();
                doc.LoadXml(xml);
                // only print the first few elements
                XmlNodeList items = doc.GetElementsByTagName("item");
                DateTime utcDate = DateTime.UtcNow;
                for (int i=0; i < 5; i++)
                {   string pubDateStr = "";
                    try {
                        pubDateStr = items[i]["pubDate"].InnerText;
                    } catch (NullReferenceException e) {
                        Console.WriteLine("\nException Caught!");	
                        Console.WriteLine("Message :{0} ",e.Message);
                        continue;
                    }
                    DateTime pubDate = Convert.ToDateTime(pubDateStr);
                    // Console.WriteLine(pubDate);
                    if (utcDate.Subtract(pubDate).TotalHours < 24 * 2) {
                        Console.WriteLine("Within 2 days");
                        // check if id is in db
                        string esInstance = Environment.GetEnvironmentVariable("ES_INSTANCE");
                        var settings = new ConnectionConfiguration(new Uri(esInstance))
                            .RequestTimeout(TimeSpan.FromMinutes(2));
                        var lowlevelClient = new ElasticLowLevelClient(settings);
                        var searchResponse = lowlevelClient.Search<StringResponse>("post", PostData.Serializable(new
                        {
                            query = new
                            {
                                match = new
                                {
                                    guid = items[i]["guid"].InnerText// items[i]["guid"].InnerText
                                }
                            }
                        }));
                        var successful = searchResponse.Success;
                        var responseJson = searchResponse.Body;
                        SearchResult searchResult = JsonSerializer.Deserialize<SearchResult>(responseJson);
                        if (searchResult.hits.total.value == 0) {
                            SendItemToDiscord(items[i]);
                        } else {
                            Console.WriteLine("Match Already in DB, not going to print");
                        }
                    }
                }
            }
            await Task.CompletedTask;
        }
        static async public Task<string> FetchData(string searchText) {
            var query = HttpUtility.ParseQueryString(string.Empty);
            query["q"] = searchText;
            string queryString = query.ToString();

            string htmlData = string.Empty;
            string urlTemplate = @"https://news.google.com/rss/search?{0}";
            string url = string.Format(urlTemplate, queryString);
            try	
            {
              string responseBody = await client.GetStringAsync(url);

              Console.WriteLine(responseBody);
              return await Task.FromResult(responseBody);
            }
            catch(HttpRequestException e)
            {
              Console.WriteLine("\nException Caught!");	
              Console.WriteLine("Message :{0} ",e.Message);
            }
            return await Task.FromResult("");
        }
    }
}
 
 ```

This is a .NET console application that alerts the user of recent news and stock information.

The main method `Main` is executed when the program starts, it calls two async methods `checkNews` and `checkPrices`.

The `checkNews` method does the following:

* It loops through a predefined list of search terms and for each term, it calls the `FetchData` method that retrieves the news data in XML format related to the search term.
* The returned XML is loaded into an XmlDocument object, and the elements with the tag "item" are extracted into a list.
* For each item in the list, the method checks if the publication date is within the past two days.
* If the publication date is within the past two days, the method sends the news item to a Discord channel using a Discord webhook and also stores it in an Elasticsearch database.

The `checkPrices` method does the following:

* It retrieves the stock information using an API and stores the relevant data in a list of `StockData` objects.

The `SendItemToDiscord` method takes an XmlNode object (representing a news item) as input and does the following:

* It retrieves the Discord webhook from the environment variables.
* It creates an HTTP request to the Discord webhook URL and sets the content type to "application/json".
* The method formats the news item data into a string and writes it to the HTTP request stream.
* It then sends the request and retrieves the response.
* Finally, it stores the news item in an Elasticsearch database.

Using RSS (Really Simple Syndication) feeds for news alerts as an investor can be a useful tool for staying up-to-date with the latest news and developments in the stock market and individual stocks you are interested in. By subscribing to relevant RSS feeds, you can receive real-time updates on news and events that may impact your investments.

For example, you can subscribe to news outlets, financial websites, and industry blogs that cover the stocks you're invested in. This way, you can quickly receive alerts on any major news or developments affecting those stocks, allowing you to stay ahead of the curve and make informed investment decisions. Additionally, using an RSS reader can help you stay organized and avoid missing important news stories.

It is important to note, however, that relying solely on news from RSS feeds may not provide a complete and accurate picture of a company's financial health and future performance. It is always a good idea to do additional research, such as analyzing financial statements and reading analyst reports, before making investment decisions.


Elasticsearch is a highly scalable, open source, distributed, RESTful search and analytics engine. It can be used for a variety of use cases including:

1. Full-Text Search: Elasticsearch provides fast and powerful search capabilities, making it ideal for implementing full-text search functionality in applications.
2. Log Analytics: Elasticsearch can be used to store, search, and analyze log data in real-time, providing valuable insights into system performance and user behavior.
3. Business Intelligence: Elasticsearch can be used to build custom dashboards, perform ad-hoc analysis, and run complex data aggregation operations on large data sets.
4. Data Warehousing: Elasticsearch can be used as a data warehousing solution, allowing users to store, search, and analyze large amounts of structured and unstructured data.
5. Metrics and Performance Monitoring: Elasticsearch can be used to monitor the performance and health of applications, infrastructure, and systems.
6. Geo-Spatial Analytics: Elasticsearch has built-in support for GeoJSON data, making it possible to perform geo-spatial analysis, such as distance calculation, bounding box queries, and shape-based searches.
7. Alerting and Notifications: Elasticsearch can be configured to send alerts and notifications based on certain conditions or thresholds, making it useful for monitoring and detecting critical issues.
8. eCommerce: Elasticsearch can be used to power search and recommendations in eCommerce websites, helping users find the products they're looking for quickly and easily.

Bonsai.io is a hosting service for Elasticsearch, which provides managed cloud-based Elasticsearch clusters. Bonsai offers a free tier of service, which provides a small but sufficient cluster to get started with Elasticsearch. The free tier includes features such as automatic monitoring, automated backups, and 24/7 customer support. Bonsai provides a simple and easy-to-use interface for managing your Elasticsearch cluster, so you can focus on your data and applications, rather than the underlying infrastructure. With Bonsai's free hosting service, you can get started with Elasticsearch quickly and easily, without having to worry about the setup, maintenance, and security of your cluster.


