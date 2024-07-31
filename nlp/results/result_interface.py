from pymongo import MongoClient
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import util

def writeResultFeedback(data):
    client = util.mongo_client()
    db = client[util.mongo_db]
    try:

        # Parsing info
        job_id = data['job_id']
        result_id = data['result_id']

        # checking if the results collection exists
        # if collection doesn't exist, creating
        collection = db['result_feedback']

        # checking if the result exists in Mongo
        query = {'result_id':result_id}
        existing_entry = collection.find_one(query)
        if existing_entry is None:
            # Writing a new result to Mongo
            collection.insert_one(data)
        else:
            # Updating existing result in Mongo
            updated_entry = data
            element = {"$set": updated_entry}
            collection.update_one(query, element)


        # returning 200 response
        return JSONResponse(content={"message":"Successfully wrote result feedback"}, status=200)
    except Exception as e:
        # returning 400 response
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        client.close()
