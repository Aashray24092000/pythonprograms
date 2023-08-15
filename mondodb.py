import pymongo
#connectionstring is usd to connect mongo atlas 
#connectionstring='mongodb+srv://ashraya:Ashray%40123@cluster0.selrt1b.mongodb.net/?retryWrites=true&w=majority'
if __name__=='__main__':
    client=pymongo.MongoClient('localhost:27017'#connectionstring)
    db = client['test-database5']
    # collection=db['test-collection']
    posts=db.posts
    post_id=posts.insert_one({"p":2}).inserted_id
    print(post_id)
