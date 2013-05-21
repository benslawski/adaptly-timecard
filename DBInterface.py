## python modules
from storm.locals import *
from time import *

def getDBhandle():
    dbname = 'postgres://zsvwepxgwlatsi:ds7mjUOpoc7cmF9yq6CYT2Rg4_@ec2-54-227-255-156.compute-1.amazonaws.com:5432/d29g35ktn19ke2'

    store = None
    while not store:
        try:
            database = create_database(dbname)
            store = Store(database)
        except Exception as e:
            print '[ ERROR CONNECTING TO DB ]', type(e), e.message
            sleep(.1)
    return store


def getJobs():
    db = getDBhandle()

    query = "SELECT * FROM jobs"
    while True:
        try:
            results = db.execute(query)
            results = results.get_all()
            break
        except Exception as e:
            print '[ ERROR FETCHING JOB LIST ]', type(e), e.message

    return map(lambda k: k[0], results)


def punchCard(job_name, start_t, end_t):
    db = getDBhandle()

    command = "INSERT INTO punches " \
            + "VALUES (DEFAULT, " \
                    + "'" + job_name + "', " \
                    + "'" + start_t + "', " \
                    + "'" + end_t + "')"
    print command
    while True:
        try:
            db.execute(command)
            db.commit()
            break
        except Exception as e:
            db.rollback()
            print '[ ERROR PUNCHING CARD FOR ' + job_name + ' ]', type(e), e.message
            sleep(.1)

