db.createCollection("pets");

db.pets.insertMany(
    [
        {
            name:"HARSHA K Y",
            age: 21,
            pets:[
                {
                    petName:"sudh",
                    petAge:24,
                    petType:"dog"
                },
                {
                    petName:"rocky",
                    petAge:5,
                    petType:"cat"
                },
                {
                    petName:"lakshmi",
                    petAge:20,
                    petType:"cow"
                }
            ]
        },
        {
            name:"RAMA",
            age: 20,
            pets:[
                {
                    petName:"rum",
                    petAge:2,
                    petType:"dog"
                },
                {
                    petName:"mocky",
                    petAge:5,
                    petType:"tiger"
                },
            ]
        },
        {
            name:"pratheek",
            age: 25,
            pets:[
                {
                    petName:"kick",
                    petAge:2,
                    petType:"rat"
                },
                {
                    petName:"loop",
                    petAge:5,
                    petType:"pig"
                },
                {
                    petName:"sudhanva",
                    petAge:20,
                    petType:"buffalo"
                }
            ]
        },
        {
            name:"shreedhar",
            age: 23,
            pets:[
                {
                    petName:"lakshmi",
                    petAge:12,
                    petType:"cow"
                },
                {
                    petName:"nagini",
                    petAge:105,
                    petType:"snake"
                },
                {
                    petName:"poco",
                    petAge:2,
                    petType:"earthworm"
                }
            ]
        },
        {
            name:"Shubham",
            age: 21,
            pets:[
                {
                    petName:"shooo",
                    petAge:2,
                    petType:"sloth"
                },
                {
                    petName:"jim",
                    petAge:5,
                    petType:"monkey"
                },
            ]
        },
        {
            name:"Pavin",
            age: 21,
            pets:[
                {
                    petName:"sammy",
                    petAge:2,
                    petType:"dog"
                },
                {
                    petName:"tiger",
                    petAge:5,
                    petType:"chimp"
                },
                {
                    petName:"loki",
                    petAge:20,
                    petType:"cat"
                }
            ]
        },
        {
            name:"rakshith",
            age: 23,
            pets:[
                {
                    petName:"dusty",
                    petAge:2,
                    petType:"dust mite"
                },
            ]
        },
        {
            name:"sathish",
            age: 21,
            pets:[
                {
                    petName:"rouge",
                    petAge:13,
                    petType:"pig"
                },
                {
                    petName:"sumush",
                    petAge:5,
                    petType:"cat"
                },
            ]
        },
        {
            name:"lakshman",
            age: 21,
            pets:[
                {
                    petName:"trigger",
                    petAge:2,
                    petType:"cockroach"
                },
                {
                    petName:"ronney",
                    petAge:5,
                    petType:"dog"
                },
                {
                    petName:"high",
                    petAge:2,
                    petType:"mosquito"
                }
            ]
        },
        {
            name:"abhi ram",
            age: 21,
            pets:[
                {
                    petName:"raymond",
                    petAge:2,
                    petType:"dog"
                },
                {
                    petName:"roco",
                    petAge:5,
                    petType:"cat"
                },
                {
                    petName:"seeta",
                    petAge:20,
                    petType:"cow"
                }
            ]
        },
    ]
)

db.pets.count({"pets.petType":"cat"})

db.pets.aggregate([
    {

    }
])

db.pets.find({"pets.petType":"dog"}).limit(2)

db.books.aggregate( [
    { $group : { _id : "$author", books: { $push: "$title" } } },
    { $out : "authors" }
] ) 

