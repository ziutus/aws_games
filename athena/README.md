```shell
CREATE EXTERNAL TABLE sensors_data (
    timestamp timestamp,
	sensor_id tinyint,
	temperature tinyint, 
	pressure  tinyint, 
	humidity  tinyint, 
	brightness tinyint, 
	saturation tinyint
)
ROW FORMAT  serde 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://odkrywca-qa-athena-games/sensors_raw/';
```

```shell
select * from sensors_data limit 10
```
```shell
drop table sensors_data
```

```shell
SELECT "$path" FROM sensors_data
```

```shell
select "$path" from sensors_data where sensor_id=7 order by timestamp limit 10
```
