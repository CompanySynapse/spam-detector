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
The product has 2 versions. It can be used purely through the API, or with the program itself (it's private at the moment, contact me at <email> if you want to buy it, although nobody will). With the API version, you can input only the email contents. With the program, you can set custom safety levels, which can go from 0.5 (Remove anythin with a chance of being spam) to 0.95 (Remove anythin that is 100% spam) or anywhere inbetween for custom levels of safety.
