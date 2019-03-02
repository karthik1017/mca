db.createCollection('employee');

db.employee.insertMany(
    [
        {
            emp_id:1,
            name:"karthik",
            salary:10000,
            role:"HR"
        },
        {
            emp_id:2,
            name:"adharsha",
            salary:4000,
            role:"Manager"
        },
        {
            emp_id:3,
            name:"sathish",
            salary:9000,
            role:"Manager"
        },
        {
            emp_id:4,
            name:"sudhanva",
            salary:5000,
            role:"janitor"
        },
        {
            emp_id:5,
            name:"AAA",
            salary:7999,
            role:"BBB"
        },
        {
            emp_id:6,
            name:"ccc",
            salary:7999,
            role:"ddd"
        },
        {
            emp_id:7,
            name:"karthik",
            salary:100000,
            role:"ceo"
        },
        {
            emp_id:8,
            name:"rama",
            salary:40000,
            role:"cto"
        },
        {
            emp_id:9,
            name:"krish",
            salary:4000,
            role:"security",
        },
        {
            emp_id:10,
            name:"kalyan",
            salary:70000,
            role:"creativity manager"
        }
    ]
)

db.employee.update(
    {
        name: 'AAA'
    },
    {
        $set: {
            salary: 8000
        }
    }
);

db.employee.find(
    {
        name: 'AAA'
    }
).pretty();

db.employee.updateMany(
    {
    },
    {
        $inc:{
            salary: 4500
        }
    }
);


db.employee.update(
    {
        name: 'ccc'
    },
    {
        $set:{
            role : ['head','professor']
        }
    }
)


db.employee.find({name:'ccc'}).pretty()

db.employee.update(
    {
        name: "AAA"
    },
    {
        $set:{
            remark : "vc"
        }
    }
);


db.employee.update(
    {
        name: "xxx"
    },
    {
        emp_id:11,
        name: "XXX",
        salary: 10000,
        role: "coach",
    },
    {
        upsert: true
    }
)

db.restaurants.insertMany(
    [
        {
            name: "adigas",
            address: {
                building: 1,
                coordinates:[1,2],
                street: "r v road",
                city: "bengaluru",
                zipcode: 001
            },
            cuisine: "south indian",
            ratings: {
                date: Date(),
                grade: "first class",
                score: 4.0
            }
        },
        {
            name: "shivaji",
            address: {
                building: 2,
                coordinates:[2,3],
                street: "r v road",
                city: "bengaluru",
                zipcode: 002
            },
            cuisine: "south indian",
            ratings: {
                date: Date(),
                grade: "first class",
                score: 4.5
            }
        },
        {
            name: "rasa",
            address: {
                building: 3,
                coordinates:[4,5],
                street: "r v road",
                city: "bengaluru",
                zipcode: 003
            },
            cuisine: "east indian",
            ratings: {
                date: Date(),
                grade: "first class",
                score: 3.0
            }
        },
        {
            name: "gas",
            address: {
                building: 4,
                coordinates:[6,7],
                street: "r v road",
                city: "bengaluru",
                zipcode: 004
            },
            cuisine: "north indian",
            ratings: {
                date: Date(),
                grade: "first class",
                score: 4.0
            }
        },
        {
            name: "adi",
            address: {
                building: 5,
                coordinates:[7,8],
                street: "r v road",
                city: "bengaluru",
                zipcode: 005
            },
            cuisine: "international",
            ratings: {
                date: Date(),
                grade: "first class",
                score: 4.5
            }
        },
        {
            name: "udupi",
            address: {
                building: 6,
                coordinates:[9,8],
                street: "r v road",
                city: "bengaluru",
                zipcode: 006
            },
            cuisine: "south indian",
            ratings: {
                date: Date(),
                grade: "first class",
                score: 4.3
            }
        },
        {
            name: "krishna",
            address: {
                building: 7,
                coordinates:[10,20],
                street: "r v road",
                city: "bengaluru",
                zipcode: 007
            },
            cuisine: "malabar",
            ratings: {
                date: Date(),
                grade: "first class",
                score: 4.1
            }
        },
        {
            name: "rama",
            address: {
                building: 8,
                coordinates:[13,2],
                street: "r v road",
                city: "bengaluru",
                zipcode: 006
            },
            cuisine: "south indian",
            ratings: {
                date: Date(),
                grade: "first class",
                score: 4.0
            }
        },
        {
            name: "adyar",
            address: {
                building: 9,
                coordinates:[1,2],
                street: "r v road",
                city: "bengaluru",
                zipcode: 004
            },
            cuisine: "south indian",
            ratings: {
                date: Date(),
                grade: "first class",
                score: 4.0
            }
        },
        {
            name: "ananda",
            address: {
                building: 1,
                coordinates:[1,2],
                street: "r v road",
                city: "bengaluru",
                zipcode: 001
            },
            cuisine: "south indian",
            ratings: {
                date: Date(),
                grade: "first class",
                score: 4.0
            }
        },
    ]
)

