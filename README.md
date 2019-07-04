# Uakari 
URL shortener with ability to process batch of links at once. 

## Usage

```
docker-compose up
```

### shorten one URL

* open admin panel at <http://localhost:8000/uakari/>
* go to _one record_ section
* press _add one record_ button 
* fill in long url and max hash length fields
* set the link expire time
* press _save_ to get the short url

### shorten batch of URLs

For this to work, you need a WebDAV server. Specify it in
docker-compose. For tests you can just use <https://requestbin.com/>
instead.

* prepare csv file filled with urls you want to shorten:
  ```
  id;long_url
  69;http://example.com/category_1/category_2/2983978298
  ...
  ```
* go to admin panel at <http://localhost:8000/uakari/>
* press _add record edit_ button 
* add a descriptive name to this batch of links
* upload your csv
* fill in max hash length fields
* set the link expire time
* press _save_
* go to <http://localhost:8000/uakari/> again and now you can download the result of processing by clicking the link at _result file_ field
  * If you use requestbin, you will have to look in your logs instead