# SpamRadar-v1-Rev1

![Anti Spammer GIF](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fsteemitimages.com%2F0x0%2Fhttps%3A%2F%2Fmedia.giphy.com%2Fmedia%2F26uXNEHznsAMFCRby%2Fgiphy.gif&f=1&nofb=1&ipt=5bada98c60362263d88e9f0e701d8d2abce3177726127e48d3650c68c1095e24&ipo=images)

## About SpamRadar
**Spam Radar** is a machine learning tool that analyzes the content of an email or message to determine whether it is likely to be spam or not. It uses advanced algorithms and natural language processing techniques to analyze the input text and return a probability score indicating the likelihood that the email or message is spam. The API only allows users to input the email's content and does not consider any associated metadata such as sender, recipient, or subject line, although it may be added in a future revision.

## API Examples
### Python
The following is an example of using the **Python** requests library to send a HTTP GET request to our API:
``` 
import requests
print(requests.get('[API-LINK-HERE]/isspam/<email-contents>').text)
```
### JavaScript
The following is an example of using the **JavaScript** fetch function to send a HTTP GET request to our API:
```
fetch('[API-LINK-HERE]/isspam/<email-contents>')
  .then(response => response.json())
  .then(data => console.log(data))
```

## Product
I am selling the product for $100, but the associated API is free to use. The API allows users to access the functionality of the product and integrate it into their own projects and systems. It is available for use at no cost and does not require any additional fees or subscriptions. Customers who purchase the product will have full access to the model and program itself and can use it to enhance their experience with emails/enhance the experience of their customers. With the paid version of the product, you can set a custom safety level, which can go from 0.5 (Block any emails that have any *slight* chance of being spam) to 1 (Block emails with a 100% chance of being spam), or any level inbetween. Whether you are using the product on its own or in conjunction with the API, you can be confident that you are getting a high-quality and reliable solution.
