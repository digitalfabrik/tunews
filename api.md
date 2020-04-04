# TüNews API

## Endpoints
### Languages
#### Method
GET
#### URL
https://tunews.integreat-app.de/v1/news/languages
#### Response
```
[{
    code: string,
    name: string,
    direction: "rtl" | "ltr"
}]
```

### Categories
#### Method
GET
#### URL
  https://tunews.integreat-app.de/v1/news/tags
#### Response
```
[{
    id: integer,
    name: string
}]
```
#### To discuss
- `code` instead of `id`, probably not available
- Name without the leading number, e.g. `Landkreis Tübingen und Europa` intead of `0 Landkreis Tübingen und Europa`

### News
#### Method
GET
#### URL
https://tunews.integreat-app.de/v1/news/{languageCode}?page=N&count=M
#### Query parameters
- Filter:
    - `tag`: tag id
- Search: `search`: Search query
- Pagination:
    - `count`: Number of items to return
    - `page`: Page of items to retun, e.g. `3` -> Items 20 - 29 should be returned
#### Response
```
[{
    id: integer,
    title: string,
    tags: [Category],
    date: string
}]
```
#### To discuss
- `slug` instead of `id`, probably not available
- `excerpt`: How many characters? Cut on whitespaces/points
- `languageCode`: Language code as query parameter instead of url part


### Single news
#### Method
GET
#### URL
https://tunews.integreat-app.de/v1/news/{id}
#### Response
```
{
    id: string,
    title: string,
    tags: [tags],
    date: string,
    content: string
    enewsno: string
}
```
#### To discuss
- Same as above
- `content`: Trailing date: Will be removed.

