# pi-music-alarm
A music alarm on the Raspberry Pi

## Usage
Edit `config.py` to point to your music location and set alarms, then run
`./alarm.py`.

Currently the application assumes that your music_path has the structure
<artist>/<albums>/<songs> underneath.

Alarms are a triple of day specifier, hour and minute (in military time, based
on the timezone that your Pi is running in. For example,
```
('weekdays', 5, 30)
```
means Monday through Friday, 5:30 AM

Valid day specifiers are
 - `weekdays`
 - `weekend`
 - `sunday`
 - `monday`
 - `tuesday`
 - `wednesday`
 - `thursday`
 - `friday`
 - `saturday`
