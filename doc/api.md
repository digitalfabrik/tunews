# TüNews API Endpoints
## Languages
### Method
GET
### URL
https://tunews.integreat-app.de/v1/news/languages
### Response
```json
[{
    "code": "string",
    "name": "string",
    "direction": "rtl | ltr"
}]
```
### Notes
- direction not yet available

## Tags
### Method
GET
### URL
  https://tunews.integreat-app.de/v1/news/tags
### Response
```json
[{
    "id": "integer",
    "name": "string"
}]
```
### Notes
- Maybe we can get translations at some point.
- Discuss removing the number.

## News
### Method
GET
### URL
https://tunews.integreat-app.de/v1/news/{languageCode}?page=N&count=M
### Query parameters
- Filter-tag: (not yet supported)
    - `tag`: tag id
- Filter:
    - `filter`: WORD to find in title or content, e.g `Integreat` -> items with Integreat in title or content should be returned 
- Pagination:
    - `count`: Number of items to return
    - `page`: Page of items to retun, e.g. `3` -> Items 20 - 29 should be returned
### Response
```json
[{
    "id": "integer",
    "title": "string",
    "tags": ["Category"],
    "date": "string"
}]
```
### Notes
- As excerpt, use first N characters of text.

## Single news
### Method
GET
### URL
https://tunews.integreat-app.de/v1/news/{id}
### Response
```json
{
    "id": "string",
    "title": "string",
    "tags": ["tags"],
    "date": "string",
    "content": "string",
    "enewsno": "string"
}
```
### Notes
- Show enewsno in footer
