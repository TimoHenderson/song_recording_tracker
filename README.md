# Contents

1. [Brief](#brief)
2. [Technologies Used](#technologies-used)
3. [Running Instructions](#running-instructions)
   <br>
   <br>

# Brief

### Recording Tracker

Build an app to track song recording progress

#### MVP

- The app should allow the user to track songs and parts they want to record and those they have recorded.
- The user should be able to create and edit songs\nEach song should have one or more parts to record
- The user should be able to create and delete entries for parts
- The app should allow the user to mark parts as recorded or still to record



#### Extensions

- Added artists, albums, and instruments
- Create, edit and delete all elements
- Part states of 1-5
- Visualization of progress of elements
- Styling to look like audio gear


<br><br>

# Technologies Used

- HTML / CSS
- Python
- Flask
- PostgreSQL and psycopg
  <br><br><br>

# Running Instructions

### Requires Postgresql

1. Clone and enter git repository

```
cd song_recording_tracker
```

2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

3. Install from requirements.txt

```
pip3 install -r requirements.txt
```

4. Create database

```
createdb recording_tracker
psql -d recording_tracker -f db/recording_tracker.sql

```

4. Run the app with flask

```
flask run
```

<br><br><br>


