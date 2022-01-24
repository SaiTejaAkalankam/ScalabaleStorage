db = db.getSiblingDB("userID_db");
db.userID_tb.drop();

db.userID_tb.insertMany([
    {
        "id": 1,
        "name": "Teja",
        "password":"teja",
        "branch": "CS"
    },
    {
        "id": 2,
        "name": "Ansa",
        "password":"ansa",
        "branch": "SS"
    },
    {
        "id": 3,
        "name": "Riya",
        "password":"riya",
        "branch": "CS"
    },
    {
        "id": 4,
        "name": "Deb",
        "password":"deb",
        "branch": "SS"
    },
    {
        "id": 5,
        "name": "Charan",
        "password":"charan",
        "branch": "SS"
    },
]);