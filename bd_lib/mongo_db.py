from pymongo import MongoClient
client = MongoClient("mongodb+srv://lusenpai:lusenpaif13gdh4@clusterlu.jf2tn.mongodb.net/shinobiworldb?retryWrites=true&w=majority")
db = client.shinobiworldb;
users = db.users;
message_data = {
    'messageId': 'f46d6a80-39fb-46bc-b602-4008074c147f',
    'authorId': '1a18bf18-4af6-4989-8b48-cd6e0854be4c',
    'message': 'Вы чем занимались?)',
    'replyTo': '0'
}
result = messages.insert_one(message_data)
print('One message: {0}'.format(result.inserted_id))
