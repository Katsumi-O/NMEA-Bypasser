SELECT
'ご指定の場所の住所は,'||pref_name||city_name||','||street_name||address||'付近です。'
FROM
address
WHERE
ST_DWithin(geom2,ST_GeomFromText('POINT(139.642403 35.448575)',4326),100)
ORDER BY
ST_Distance(geom2,ST_GeomFromText('POINT(139.642403 35.448575)',4326))
LIMIT
1
;