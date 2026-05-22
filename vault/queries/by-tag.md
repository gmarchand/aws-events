# Videos by Tag

```dataview
TABLE rows.title, rows.event, rows.year
FROM "vault"
WHERE tags
GROUP BY tags
SORT rows.year DESC
```
